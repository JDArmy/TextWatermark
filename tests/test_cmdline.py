"""Test cmdline"""
from __future__ import annotations

import json
import os  # PEP 585

import pytest
from click.testing import CliRunner

from textwatermark import __version__
from textwatermark.cmdline import main

TMP_FILE = '/tmp/tmp_for_test_textwatermark.txt'


@pytest.mark.parametrize(
    ['invoke_args', 'exit_code', 'output_keyword'],
    [
        ([], 0, 'help'),
        (['--help'], 0, 'help'),
        (['--version'], 0, __version__),
        (['-V'], 0, __version__),
        (['--help', 'insert'], 0, 'Insert'),
        (['--help', 'retrieve'], 0, 'Retrieve'),
    ]
)
def test_main(
        clicker: CliRunner,
        invoke_args: list[str],
        exit_code: int,
        output_keyword: str,
):
    """Test main cmdline"""
    result = clicker.invoke(main, invoke_args)
    assert result.exit_code == exit_code
    assert output_keyword in result.output


def test_insert():
    '''test insert command'''
    runner = CliRunner()
    with open(TMP_FILE, 'w', encoding="utf-8") as file:
        file.write('1234567890')
    # 输出到终端
    cmd = f'insert -f "{TMP_FILE}" -m ALPHA_NUMERICAL -t HOMOGRAPH_NUMBERS -x 999 -w 123'
    result = runner.invoke(main, cmd)
    assert 'Ӏ2𝟑𝟒𝟓Ⳓ𝟟890' in result.output

    # 输出到文件
    cmd += f' -o "{TMP_FILE}.out"'
    result = runner.invoke(main, cmd)
    with open(TMP_FILE+'.out', 'r', encoding="utf-8") as file:
        wm_str = file.read()
    assert 'Ӏ2𝟑𝟒𝟓Ⳓ𝟟890' in wm_str
    os.unlink(TMP_FILE)
    os.unlink(TMP_FILE+'.out')


def test_insert_n_retrieve():
    '''test insert command'''
    runner = CliRunner()
    with open(TMP_FILE, 'w', encoding="utf-8") as file:
        file.write('a'*30)
    # 输出到终端
    cmd = f'insert -f "{TMP_FILE}" -m ALPHA_NUMERICAL '\
        f'-t FONT_COLOR -k black4 -x 999 -w 123 -i 2 -l '

    runner.invoke(main, cmd + f' -o "{TMP_FILE}.out"')
    param_result = runner.invoke(main, cmd+' -e')

    retrieve_result = runner.invoke(
        main, f'retrieve -f {TMP_FILE}.out -p \'{param_result.output}\'')
    assert '123' in retrieve_result.output


def test_retrieve():
    '''test retrieve command'''
    runner = CliRunner()
    with open(TMP_FILE, 'w', encoding="utf-8") as file:
        file.write('Ӏ2𝟑𝟒𝟓Ⳓ𝟟890')

    params_json = '{"tpl_type": "HOMOGRAPH_NUMBERS", "confusables_chars": [], \
        "confusables_chars_key": "", "wm_base": 7, "method": 1, "wm_mode": 5, \
            "wm_len": 7, "wm_loop": false, "start_at": 0,"wm_flag_bit": true,\
                  "version": "'+__version__+'"}'
    result = runner.invoke(
        main, f'retrieve -f {TMP_FILE} -p \'{params_json}\'')
    assert '123' in result.output

    params_json1 = '{"tpl_type": "HOMOGRAPH_NUMBERS", "confusables_chars": [], \
        "confusables_chars_key": "", "wm_base": 7, "method": 1, "wm_mode": 5, \
            "wm_len": 7, "wm_loop": false, "start_at": 0,"wm_flag_bit": true,\
                  "version": "0.0.0"}'
    result = runner.invoke(
        main, f'retrieve -f {TMP_FILE} -p \'{params_json1}\'')
    assert 'Result ValueError' in str(result)

    params_json = '{"tpl_type": "HOMOGRAPH_NUMBERS", "confusables_chars": [], \
        "confusables_chars_key": "", "wm_base": 7, "method": 1, "wm_mode": 5, \
            "wm_len": 7, "wm_loop": false, "start_at": 0,"wm_flag_bit": true,\
                  "version": "0.0.0"}'
    result = runner.invoke(
        main, f'retrieve -f {TMP_FILE} -p \'{params_json}\' -F')
    assert '123' in result.output

    os.unlink(TMP_FILE)


def test_retrieve_bin():
    '''test retrieve bin command'''
    runner = CliRunner()

    params_json = '{"tpl_type": "FONT_SIZE", "wm_flag_bit": true, "confusables_chars": [], '\
        '"confusables_chars_key": "110", "wm_base": 2, "method": 3, "wm_mode": 5,'\
        ' "wm_len": 35, "wm_loop": false, "start_at": 0, "version": "'+__version__+'"}'
    result = runner.invoke(
        main, f'retrieve -b "10010000011000100000101000110000111" -p \'{params_json}\'')
    assert '123456' in result.output

    params_json = '{"tpl_type": "FONT_SIZE", "wm_flag_bit": true, "confusables_chars": [], '\
        '"confusables_chars_key": "110", "wm_base": 2, "method": 3, "wm_mode": 5, '\
        '"wm_len": 35, "wm_loop": false, "start_at": 0, "version": "0.0.0"}'
    result = runner.invoke(
        main, f'retrieve -b "10010000011000100000101000110000111" -p \'{params_json}\' -F')
    assert '123456' in result.output

    result = runner.invoke(
        main, f'retrieve -b "10010000011000100000101000110000111" -p \'{params_json}\'')
    assert 'Result ValueError' in str(result)


def test_export_params():
    '''test export params command'''
    runner = CliRunner()

    params_json = '{"tpl_type": "HOMOGRAPH_NUMBERS", "confusables_chars": [],\
        "confusables_chars_key": "", "wm_base": 7, "method": 1, "wm_mode": 5, \
            "wm_len": 7, "wm_loop": false, "start_at": 0,"wm_flag_bit": true,\
                  "version": "'+__version__+'"}'

    cmd = 'insert -m ALPHA_NUMERICAL -t HOMOGRAPH_NUMBERS -x 999 -w 123 -e'
    result = runner.invoke(main, cmd)
    assert json.loads(result.output) == json.loads(params_json)

    cmd += f' -o {TMP_FILE}'
    result = runner.invoke(main, cmd)
    with open(TMP_FILE, 'r', encoding="utf-8") as file:
        out_param_json = file.read()
        os.unlink(TMP_FILE)

    assert json.loads(out_param_json) == json.loads(params_json)


def test_insert_watermark_no_flag_bit():
    '''test insert watermark with no_flag_bit command set'''
    runner = CliRunner()
    with open(TMP_FILE, 'w', encoding="utf-8") as file:
        file.write('12345678901')
    # 输出到终端
    cmd = f'insert -f "{TMP_FILE}" -m REAL_NUMBER '\
        f'-t HOMOGRAPH_NUMBERS -x "1977326742" -w "1977326741" -n'

    runner.invoke(main, cmd + f' -o "{TMP_FILE}.out"')
    param = runner.invoke(main, cmd+' -e')

    retrieve_result = runner.invoke(
        main, f'retrieve -f {TMP_FILE}.out -p \'{param.output.strip()}\'')
    assert '1977326741' in retrieve_result.output
