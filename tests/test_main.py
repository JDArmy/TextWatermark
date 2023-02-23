'''test text watermark'''
# pylint: disable=invalid-name

import os

import pytest

from textwatermark import __version__
from textwatermark.main import TextWatermark, WMMode
from textwatermark.template_type import WMTemplateType
from textwatermark.templates import homograph_numbers


def _insert_watermark(wm_str, wm_max, wm_mode):
    template = homograph_numbers

    confusables_chars_key = ''
    wm_loop = True
    start_at = 0

    wm = TextWatermark(wm_mode, 0, start_at, wm_loop)
    wm.set_tpl(template.CONFUSABLES_CHARS,
               template.method, confusables_chars_key)
    wm.set_wm_max(wm_max)
    wm.set_text_file(os.path.abspath(os.path.dirname(__file__)+'/text/1.txt'))

    wm_text = wm.insert_watermark(wm_str)
    params = wm.export_params()
    wm_out_str = TextWatermark.retrieve_watermark(wm_text, params)
    assert wm_out_str == wm_str


def test_insert_watermark():
    '''test insert_watermark and retrieve_watermark method'''

    _insert_watermark('123890', '9'*9, WMMode.REAL_NUMBER)
    _insert_watermark('abcxyz', 'z'*9, WMMode.LETTERS_LOWER_CASE)
    _insert_watermark('ABCXYZ', 'Z'*9, WMMode.LETTERS_UPPER_CASE)
    _insert_watermark('abxzABXZ', 'z'*9, WMMode.LETTERS_MIXED_CASE)
    _insert_watermark('01289AZaz', 'z'*9, WMMode.ALPHA_NUMERICAL)
    _insert_watermark('09-AZ_az', 'z'*9, WMMode.ALPHA_NUMERICAL_SPECIAL)
    _insert_watermark('我知', '\uFFFF'*5, WMMode.UNICODE)

    with pytest.raises(ValueError):
        _insert_watermark('我'*100, '\uFFFF'*5, WMMode.UNICODE)


def test_set_tpl_type():
    '''test set_tpl_type method'''
    wm = TextWatermark(WMMode.REAL_NUMBER, 2)
    wm.set_tpl_type(WMTemplateType.HOMOGRAPH_NUMBERS)
    assert homograph_numbers.CONFUSABLES_CHARS == wm.wmt.confusables_chars
    assert wm.tpl_type == WMTemplateType.HOMOGRAPH_NUMBERS.name


def test_text_file_not_exists():
    '''test is text file do not exists'''
    wm = TextWatermark(WMMode.REAL_NUMBER, 2)
    with pytest.raises(ValueError):
        wm.set_text_file('not_exists.txt')


def test_retrieve_watermark():
    '''test retrieve watermark'''
    wm_out = TextWatermark.retrieve_watermark(
        'Ӏ2𝟑𝟒𝟓Ⳓ𝟟890', '{"tpl_type": "HOMOGRAPH_NUMBERS", "confusables_chars": [], \
        "confusables_chars_key": "", "wm_base": 7, "wm_loop": false, "method": 1, \
        "wm_mode": 5, "wm_len": 7, "start_at": 0, "version": "'+__version__+'"}')
    assert wm_out == '123'

    wm_out = TextWatermark.retrieve_watermark(
        'Ӏ2𝟑𝟒𝟓Ⳓ𝟟890', '{"tpl_type": "HOMOGRAPH_NUMBERS", "confusables_chars": [], \
        "confusables_chars_key": "", "wm_base": 7, "wm_loop": false, "method": 1, \
        "wm_mode": 5, "wm_len": 7, "start_at": 0, "version": "0.0.0"}', True)
    assert wm_out == '123'

    with pytest.raises(ValueError):
        TextWatermark.retrieve_watermark(
            'Ӏ2𝟑𝟒𝟓Ⳓ𝟟890', '{"tpl_type": "HOMOGRAPH_NUMBERS", "confusables_chars": [], \
            "confusables_chars_key": "", "wm_base": 7, "wm_loop": false, "method": 1, \
            "wm_mode": 5, "wm_len": 7, "start_at": 0, "version": "0.0.0"}')


def test_retrieve_watermark_with_confusables():
    '''test retrieve watermark with confusables'''
    wm_out = TextWatermark.retrieve_watermark(
        'Ӏ2𝟑𝟒𝟓Ⳓ𝟟890', '{"tpl_type": "", "confusables_chars": '
        '{"0": "0᱐𝟘𝟎𝟢𝟬𝟶", "1": "1Ӏ𝟙𝟏𝟣𝟭𝟷", "2": "2ᒿ𝟚𝟐𝟤𝟮𝟸", "3": "3Ⳍ𝟛𝟑𝟥𝟯𝟹", "4": "4Ꮞ𝟜𝟒𝟦𝟰𝟺", '
        '"5": "5Ƽ𝟝𝟓𝟧𝟱𝟻", "6": "6Ⳓ𝟞𝟔𝟨𝟲𝟼", "7": "7ገ𝟟𝟕𝟩𝟳𝟽", "8": "8৪𝟠𝟖𝟪𝟴𝟾", "9": "9Ꝯ𝟡𝟗𝟫𝟵𝟿"}, '
        '"confusables_chars_key": "", "wm_base": 7, "wm_loop": false, "method": 1, '
        '"wm_mode": 5, "wm_len": 7, "start_at": 0, "version": "'+__version__+'"}')
    assert wm_out == '123'


def test_retrieve_watermark_from_bin():
    '''test retrieve watermark from bin'''
    wm_out = TextWatermark.retrieve_watermark_from_bin(
        '10010000011000100000101000110000111',
        '{"tpl_type": "FONT_SIZE", "confusables_chars": [], "confusables_chars_key": "110", '
        '"wm_base": 2, "method": 3, "wm_mode": 5, "wm_len": 35, "wm_loop": false, '
        '"start_at": 0, "version": "'+__version__+'"}')
    assert wm_out == '123456'

    wm_out = TextWatermark.retrieve_watermark_from_bin(
        '10010000011000100000101000110000111',
        '{"tpl_type": "FONT_SIZE", "confusables_chars": [], "confusables_chars_key": "110", '
        '"wm_base": 2, "method": 3, "wm_mode": 5, "wm_len": 35, "wm_loop": false, '
        '"start_at": 0, "version": "0.0.0"}', True)
    assert wm_out == '123456'

    with pytest.raises(ValueError):
        wm_out = TextWatermark.retrieve_watermark_from_bin(
            '10010000011000100000101000110000',
            '{"tpl_type": "FONT_SIZE", "confusables_chars": [], "confusables_chars_key": "110", '
            '"wm_base": 2, "method": 3, "wm_mode": 5, "wm_len": 35, "wm_loop": false, '
            '"start_at": 0, "version": "'+__version__+'"}')
