"""test text watermark"""
# pylint: disable=invalid-name,too-many-arguments

import os
from copy import deepcopy

import pytest

from textwatermark.main import TextWatermark, WMMode
from textwatermark.template_type import WMTemplateType
from textwatermark.templates import homograph_numbers
from textwatermark.version import __version__


def _insert_watermark(wm_str, wm_max, wm_mode):
    template = homograph_numbers

    confusables_chars_key = ""
    wm_loop = True
    start_at = 0

    wm = TextWatermark(wm_mode, 0, start_at, wm_loop)
    wm.set_tpl(template.CONFUSABLES_CHARS, template.method, confusables_chars_key)
    wm.set_wm_max(wm_max)
    wm.set_text_file(os.path.abspath(os.path.dirname(__file__) + "/text/1.txt"))

    wm_text = wm.insert_watermark(wm_str)
    # test export_params
    params = wm.export_params()
    # test retrieve_watermark
    wm_out_str = TextWatermark.retrieve_watermark(wm_text, params)
    assert wm_out_str == wm_str

    # test init_from_params
    with open(
        os.path.abspath(os.path.dirname(__file__) + "/text/1.txt"),
        "r",
        encoding="utf-8",
    ) as file:
        text = file.read()

    wm2 = TextWatermark.init_from_params(params, text)
    wm_text2 = wm2.insert_watermark(wm_str)
    assert wm_text2 == wm_text


def test_insert_watermark():
    """test insert_watermark and retrieve_watermark method"""

    _insert_watermark("123890", "9" * 9, WMMode.REAL_NUMBER)
    _insert_watermark("abcxyz", "z" * 9, WMMode.LETTERS_LOWER_CASE)
    _insert_watermark("ABCXYZ", "Z" * 9, WMMode.LETTERS_UPPER_CASE)
    _insert_watermark("abxzABXZ", "z" * 9, WMMode.LETTERS_MIXED_CASE)
    _insert_watermark("01289AZaz", "z" * 9, WMMode.ALPHA_NUMERICAL)
    _insert_watermark("09-AZ_az", "z" * 9, WMMode.ALPHA_NUMERICAL_SPECIAL)
    _insert_watermark("我知", "\uFFFF" * 5, WMMode.UNICODE)

    _insert_watermark("32", "1977326742", WMMode.REAL_NUMBER)

    with pytest.raises(ValueError):
        _insert_watermark("我" * 100, "\uFFFF" * 5, WMMode.UNICODE)

    _insert_watermark("9" * 8, "1" * 9, WMMode.REAL_NUMBER)
    _insert_watermark("1" * 9, "1" * 9, WMMode.REAL_NUMBER)
    with pytest.raises(ValueError):
        _insert_watermark("1" * 8 + "2", "1" * 9, WMMode.REAL_NUMBER)

    _insert_watermark("aba", "abb", WMMode.LETTERS_LOWER_CASE)
    with pytest.raises(ValueError):
        _insert_watermark("abc", "abb", WMMode.LETTERS_LOWER_CASE)


def _insert_watermark2(
    wm_str,
    wm_max,
    wm_mode,
    wm_flag_bit,
    start_at,
    wm_loop,
    template,
    confusables_chars_key,
):
    wm = TextWatermark(wm_mode, 0, start_at, wm_loop, wm_flag_bit)
    wm.set_tpl(template.CONFUSABLES_CHARS, template.method, confusables_chars_key)
    wm.set_wm_max(wm_max)
    wm.set_text_file(os.path.abspath(os.path.dirname(__file__) + "/text/number.txt"))

    wm_text = wm.insert_watermark(wm_str)
    # test export_params
    params = wm.export_params()
    # test retrieve_watermark
    wm_out_str = TextWatermark.retrieve_watermark(wm_text, params)
    assert wm_out_str == wm_str


def test_insert_watermark2():
    """test insert watermark"""
    _insert_watermark2(
        wm_str="32",
        wm_max="1977326742",
        wm_mode=WMMode.REAL_NUMBER,
        wm_flag_bit=False,
        start_at=0,
        wm_loop=False,
        template=homograph_numbers,
        confusables_chars_key="",
    )

    with pytest.raises(ValueError):
        _insert_watermark2(
            wm_str="32",
            wm_max="1977326742",
            wm_mode=WMMode.REAL_NUMBER,
            wm_flag_bit=True,
            start_at=0,
            wm_loop=False,
            template=homograph_numbers,
            confusables_chars_key="",
        )

    _insert_watermark2(
        wm_str="32",
        wm_max="197732",
        wm_mode=WMMode.REAL_NUMBER,
        wm_flag_bit=True,
        start_at=0,
        wm_loop=False,
        template=homograph_numbers,
        confusables_chars_key="",
    )

    with pytest.raises(ValueError):
        _insert_watermark2(
            wm_str="32",
            wm_max="1977326742",
            wm_mode=WMMode.REAL_NUMBER,
            wm_flag_bit=False,
            start_at=1,
            wm_loop=False,
            template=homograph_numbers,
            confusables_chars_key="",
        )

    _insert_watermark2(
        wm_str="32",
        wm_max="1977326742",
        wm_mode=WMMode.REAL_NUMBER,
        wm_flag_bit=False,
        start_at=0,
        wm_loop=True,
        template=homograph_numbers,
        confusables_chars_key="",
    )

    _insert_watermark2(
        wm_str="32",
        wm_max="1adD",
        wm_mode=WMMode.ALPHA_NUMERICAL,
        wm_flag_bit=False,
        start_at=0,
        wm_loop=False,
        template=homograph_numbers,
        confusables_chars_key="",
    )


def test_set_tpl_type():
    """test set_tpl_type method"""
    wm = TextWatermark(WMMode.REAL_NUMBER, 2)
    wm.set_tpl_type(WMTemplateType.HOMOGRAPH_NUMBERS)
    assert homograph_numbers.CONFUSABLES_CHARS == wm.wmt.confusables_chars
    assert wm.tpl_type == WMTemplateType.HOMOGRAPH_NUMBERS


def test_set_wm_max_exception():
    """test set_tpl_type method"""
    wm = TextWatermark(WMMode.REAL_NUMBER, 2)
    with pytest.raises(ValueError):
        wm.set_wm_max(100)


def test_text_file_not_exists():
    """test is text file do not exists"""
    wm = TextWatermark(WMMode.REAL_NUMBER, 2)
    with pytest.raises(ValueError):
        wm.set_text_file("not_exists.txt")

    with pytest.raises(OSError):
        wm.set_text_file("/tmp")


def test_save_to_file_exception():
    """test is text file do not exists"""
    wm = TextWatermark(WMMode.REAL_NUMBER, 2)

    with pytest.raises(OSError):
        wm.save_to_file("AAA", "/tmp")


def test_retrieve_watermark():
    """test retrieve watermark"""
    wm_out = TextWatermark.retrieve_watermark(
        "Ӏ2𝟑𝟒𝟓Ⳓ𝟟890",
        '{"tpl_type": "HOMOGRAPH_NUMBERS", "confusables_chars": [], \
        "confusables_chars_key": "", "wm_base": 7, "wm_loop": false, \
        "method": "FIND_AND_REPLACE", "wm_mode": "ALPHA_NUMERICAL", \
        "wm_len": 7, "start_at": 0,"wm_flag_bit": true,'
        ' "version": "' + __version__ + '"}',
    )
    assert wm_out == "123"

    wm_out = TextWatermark.retrieve_watermark(
        "Ӏ2𝟑𝟒𝟓Ⳓ𝟟890",
        '{"tpl_type": "HOMOGRAPH_NUMBERS", "confusables_chars": [], \
        "confusables_chars_key": "", "wm_base": 7, "wm_loop": false, \
        "method": "FIND_AND_REPLACE", "wm_mode": "ALPHA_NUMERICAL", \
        "wm_len": 7, "start_at": 0,"wm_flag_bit": true, "version": "0.0.0"}',
        True,
    )
    assert wm_out == "123"

    with pytest.raises(ValueError):
        TextWatermark.retrieve_watermark(
            "Ӏ2𝟑𝟒𝟓Ⳓ𝟟890",
            '{"tpl_type": "HOMOGRAPH_NUMBERS", "confusables_chars": [], \
            "confusables_chars_key": "", "wm_base": 7, "wm_loop": false, \
            "method": "FIND_AND_REPLACE", "wm_mode": "ALPHA_NUMERICAL", \
            "wm_len": 7, "start_at": 0,"wm_flag_bit": true, "version": "0.0.0"}',
        )

    with pytest.raises(ValueError):
        wm_out = TextWatermark.retrieve_watermark(
            "Ӏ2𝟑𝟒𝟓Ⳓ𝟟890",
            '{"tpl_type": "WRONG_TYPE", "confusables_chars": [], \
            "confusables_chars_key": "", "wm_base": 7, "wm_loop": false, \
            "method": "FIND_AND_REPLACE", "wm_mode": "ALPHA_NUMERICAL", \
            "wm_len": 7, "start_at": 0,"wm_flag_bit": true,'
            ' "version": "' + __version__ + '"}',
        )


def test_retrieve_watermark_with_confusables():
    """test retrieve watermark with confusables"""
    wm_out = TextWatermark.retrieve_watermark(
        "Ӏ2𝟑𝟒𝟓Ⳓ𝟟890",
        '{"tpl_type": "", "confusables_chars": '
        '{"0": "0᱐𝟘𝟎𝟢𝟬𝟶", "1": "1Ӏ𝟙𝟏𝟣𝟭𝟷", "2": "2ᒿ𝟚𝟐𝟤𝟮𝟸", "3": "3Ⳍ𝟛𝟑𝟥𝟯𝟹", "4": "4Ꮞ𝟜𝟒𝟦𝟰𝟺", '
        '"5": "5Ƽ𝟝𝟓𝟧𝟱𝟻", "6": "6Ⳓ𝟞𝟔𝟨𝟲𝟼", "7": "7ገ𝟟𝟕𝟩𝟳𝟽", "8": "8৪𝟠𝟖𝟪𝟴𝟾", "9": "9Ꝯ𝟡𝟗𝟫𝟵𝟿"}, '
        '"confusables_chars_key": "", "wm_base": 7, "wm_loop": false, '
        '"method": "FIND_AND_REPLACE", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 7, '
        '"start_at": 0,"wm_flag_bit": true, "version": "' + __version__ + '"}',
    )
    assert wm_out == "123"

    with pytest.raises(ValueError):
        wm_out = TextWatermark.retrieve_watermark(
            "Ӏ2𝟑𝟒𝟓",
            '{"tpl_type": "", "confusables_chars": '
            '{"0": "0᱐𝟘𝟎𝟢𝟬𝟶", "1": "1Ӏ𝟙𝟏𝟣𝟭𝟷", "2": "2ᒿ𝟚𝟐𝟤𝟮𝟸", "3": "3Ⳍ𝟛𝟑𝟥𝟯𝟹", "4": "4Ꮞ𝟜𝟒𝟦𝟰𝟺", '
            '"5": "5Ƽ𝟝𝟓𝟧𝟱𝟻", "6": "6Ⳓ𝟞𝟔𝟨𝟲𝟼", "7": "7ገ𝟟𝟕𝟩𝟳𝟽", "8": "8৪𝟠𝟖𝟪𝟴𝟾", "9": "9Ꝯ𝟡𝟗𝟫𝟵𝟿"}, '
            '"confusables_chars_key": "", "wm_base": 7, "wm_loop": false, '
            '"method": "FIND_AND_REPLACE", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 7, '
            '"start_at": 0,"wm_flag_bit": true, "version": "' + __version__ + '"}',
        )


def test_retrieve_watermark_from_bin():
    """test retrieve watermark from bin"""
    wm_out = TextWatermark.retrieve_watermark_from_bin(
        "10010000011000100000101000110000111",
        '{"tpl_type": "FONT_SIZE", "confusables_chars": [], "confusables_chars_key": "110", '
        '"wm_base": 2, "method": "DECORATE_EACH_CHAR", "wm_mode": "ALPHA_NUMERICAL", '
        '"wm_len": 35, "wm_loop": false, "start_at": 0, "wm_flag_bit": true, '
        '"version": "' + __version__ + '"}',
    )
    assert wm_out == "123456"

    wm_out = TextWatermark.retrieve_watermark_from_bin(
        "0010000011000100000101000110000111",
        '{"tpl_type": "FONT_SIZE", "confusables_chars": [], "confusables_chars_key": "110", '
        '"wm_base": 2, "method": "DECORATE_EACH_CHAR", "wm_mode": "ALPHA_NUMERICAL", '
        '"wm_len": 34, "wm_loop": false, "start_at": 0, "wm_flag_bit": false, '
        '"version": "' + __version__ + '"}',
    )
    assert wm_out == "123456"

    wm_out = TextWatermark.retrieve_watermark_from_bin(
        "10010000011000100000101000110000111",
        '{"tpl_type": "FONT_SIZE", "confusables_chars": [], "confusables_chars_key": "110", '
        '"wm_base": 2, "method": "DECORATE_EACH_CHAR", "wm_mode": "ALPHA_NUMERICAL", '
        '"wm_len": 35, "wm_loop": false, "start_at": 0, "wm_flag_bit": true, "version": "0.0.0"}',
        True,
    )
    assert wm_out == "123456"

    with pytest.raises(ValueError):
        wm_out = TextWatermark.retrieve_watermark_from_bin(
            "10010000011000100000101000110000",
            '{"tpl_type": "FONT_SIZE", "confusables_chars": [], "confusables_chars_key": "110", '
            '"wm_base": 2, "method": "DECORATE_EACH_CHAR", "wm_mode": "ALPHA_NUMERICAL", '
            '"wm_len": 35, "wm_loop": false, "start_at": 0, "wm_flag_bit": true, '
            '"version": "' + __version__ + '"}',
        )


def test_init_from_params():
    """test init_from_params method"""
    with open(
        os.path.abspath(os.path.dirname(__file__) + "/text/1.txt"),
        "r",
        encoding="utf-8",
    ) as file:
        text = file.read()
    # samples
    wm = TextWatermark(WMMode.REAL_NUMBER, 0, 0, True)
    wm.set_tpl_type(WMTemplateType.HOMOGRAPH_NUMBERS)
    wm.set_wm_max(999999999)
    wm.set_text_file(os.path.abspath(os.path.dirname(__file__) + "/text/1.txt"))
    wm_text = wm.insert_watermark("123456")
    # samples end

    params = (
        '{"tpl_type": "", "confusables_chars": {"0": "0᱐𝟘𝟎𝟢𝟬𝟶", "1": "1Ӏ𝟙𝟏𝟣𝟭𝟷",'
        + ' "2": "2ᒿ𝟚𝟐𝟤𝟮𝟸", "3": "3Ⳍ𝟛𝟑𝟥𝟯𝟹", "4": "4Ꮞ𝟜𝟒𝟦𝟰𝟺", "5": "5Ƽ𝟝𝟓𝟧𝟱𝟻", "6": "6Ⳓ𝟞𝟔𝟨𝟲𝟼", '
        + '"7": "7ገ𝟟𝟕𝟩𝟳𝟽", "8": "8৪𝟠𝟖𝟪𝟴𝟾", "9": "9Ꝯ𝟡𝟗𝟫𝟵𝟿", ".": ".٠۰ꓸ․ͺ᎐"}, '
        + '"confusables_chars_key": "", "wm_base": 7, "method": "FIND_AND_REPLACE", '
        + '"wm_mode": "REAL_NUMBER", "wm_len": 12, '
        + '"wm_flag_bit": true, "wm_loop": true, "wm_max": "999999999", "start_at": 0, '
        + f'"version": "{__version__}"'
        + "}"
    )

    wm2 = TextWatermark.init_from_params(params, text)
    wm_text2 = wm2.insert_watermark("123456")
    assert wm_text == wm_text2

    # raise version error
    params1 = deepcopy(params)
    params1 = params1.replace(__version__, "0.0.0")
    with pytest.raises(ValueError):
        TextWatermark.init_from_params(params1, text)

    # init from type
    params3 = (
        '{"tpl_type": "HOMOGRAPH_NUMBERS", '
        + '"confusable__chars_key": "", "wm_base": 7, "method": "FIND_AND_REPLACE", '
        + '"wm_mode": "REAL_NUMBER", "wm_len": 12, '
        + '"wm_flag_bit": true, "wm_loop": true, "wm_max": "999999999", "start_at": 0, '
        + f'"version": "{__version__}"'
        + "}"
    )
    wm3 = TextWatermark.init_from_params(params3, text)
    wm_text3 = wm3.insert_watermark("123456")
    assert wm_text == wm_text3


def test_check_if_enough_space():
    """test check_if_enough_space method"""
    text = "12345678901"
    params = {
        "tpl_type": "HOMOGRAPH_NUMBERS",
        "confusables_chars": [],
        "confusables_chars_key": "",
        "wm_base": 7,
        "method": "FIND_AND_REPLACE",
        "wm_mode": "REAL_NUMBER",
        "wm_len": 8,
        "wm_flag_bit": False,
        "wm_loop": False,
        "wm_max": "999999",
        "start_at": 0,
        "version": __version__,
    }
    ret1 = TextWatermark.check_if_enough_space(params, text)
    assert ret1 is True

    params["start_at"] = 10
    ret2 = TextWatermark.check_if_enough_space(params, text)
    assert ret2 is False

    params["method"] = "INSERT_INTO_POSITION"
    params["tpl_type"] = "INVISIBLE_CHARS"
    params["start_at"] = 15
    ret3 = TextWatermark.check_if_enough_space(params, text)
    assert ret3 is False

    params["start_at"] = 0
    ret4 = TextWatermark.check_if_enough_space(params, text)
    assert ret4 is True

    params = {
        "tpl_type": "COMBINING_CHARS",
        "confusables_chars": [],
        "confusables_chars_key": "",
        "wm_base": 36,
        "method": "APPEND_TO_CHAR",
        "wm_mode": "REAL_NUMBER",
        "wm_len": 4,
        "wm_flag_bit": False,
        "wm_loop": False,
        "wm_max": "999999",
        "start_at": 0,
        "version": __version__,
    }
    ret5 = TextWatermark.check_if_enough_space(params, text)
    assert ret5 is True

    params["start_at"] = 10
    ret6 = TextWatermark.check_if_enough_space(params, text)
    assert ret6 is False


def test_check_if_enough_space_exception():
    """test check_if_enough_space method"""
    text = "12345678901"
    params = {
        "tpl_type": "HOMOGRAPH_NUMBERS",
        "confusables_chars": [],
        "confusables_chars_key": "",
        "wm_base": 7,
        "method": "FIND_AND_REPLACE",
        "wm_mode": "REAL_NUMBER",
        "wm_len": 8,
        "wm_flag_bit": False,
        "wm_loop": False,
        "wm_max": "999999",
        "start_at": 0,
        "version": __version__,
    }

    param1 = deepcopy(params)
    param1["tpl_type"] = "NOT_EXIST"
    with pytest.raises(ValueError):
        TextWatermark.check_if_enough_space(param1, text)

    param2 = deepcopy(params)
    param2["method"] = "NOT_EXIST"
    with pytest.raises(ValueError):
        TextWatermark.check_if_enough_space(param2, text)

    param3 = deepcopy(params)
    param3["wm_mode"] = "NOT_EXIST"
    with pytest.raises(ValueError):
        TextWatermark.check_if_enough_space(param3, text)
