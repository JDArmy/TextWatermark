"""test WMConverion"""

import pytest

from textwatermark.conversion import WMConversion
from textwatermark.defines import WMMode


def _test_conversion(wm_mode: WMMode, wm_base: int, wm_str: str):
    """test conversion"""
    wmc = WMConversion(wm_mode, wm_base)
    wm_final = wmc.wm_convert_to_arbitrary_base(wm_str)
    wm_out_str = wmc.wm_restore_from_arbitrary_base(wm_final)
    assert wm_str == wm_out_str


def test_conversion():
    """test conversion"""
    for wm_base in range(2, 37):
        _test_conversion(WMMode.REAL_NUMBER, wm_base, "1234567890")
        _test_conversion(WMMode.LETTERS_LOWER_CASE, wm_base, "abcxyz")
        _test_conversion(WMMode.LETTERS_UPPER_CASE, wm_base, "ABCXYZ")
        _test_conversion(WMMode.LETTERS_MIXED_CASE, wm_base, "aBcXyZ")
        _test_conversion(WMMode.ALPHA_NUMERICAL, wm_base, "123890abcXYZ")
        _test_conversion(WMMode.ALPHA_NUMERICAL_SPECIAL, wm_base, "123-ABC_XYZ#890")
        _test_conversion(WMMode.UNICODE, wm_base, "我知道")


@pytest.mark.parametrize(
    ["wm_mode", "wm_base", "wm_str"],
    [
        (WMMode.REAL_NUMBER, 5, "123456789a"),
        (WMMode.LETTERS_LOWER_CASE, 5, "1abcxyz"),
        (WMMode.LETTERS_UPPER_CASE, 5, "1ABCXYZ"),
        (WMMode.LETTERS_MIXED_CASE, 5, "1aBcXyZ"),
        (WMMode.ALPHA_NUMERICAL, 5, "123890-abcXYZ"),
        (WMMode.ALPHA_NUMERICAL_SPECIAL, 5, "123我"),
        (WMMode.UNICODE, 1, "我知道"),
        (WMMode.UNICODE, 37, "我知道"),
    ],
)
def test_conversion_error(wm_mode, wm_base, wm_str):
    """test conversion error"""

    with pytest.raises(ValueError):
        _test_conversion(wm_mode, wm_base, wm_str)
