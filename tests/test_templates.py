"""test templates"""

from textwatermark.defines import WMMethod
from textwatermark.templates import (
    combining_chars,
    font_color,
    font_float,
    font_size,
    font_style,
    font_weight,
    homograph_chinese,
    homograph_letters,
    homograph_numbers,
    homograph_punctuations,
    html_empty_tags,
    invisible_chars,
    space_chars,
    whitespace_chars,
)


def _test_templates(template):
    if template.method == WMMethod.DECORATE_EACH_CHAR:
        for _, vals in template.CONFUSABLES_CHARS.items():
            for val in vals:
                assert val.find(template.CONFUSABLES_CHARS_START_WITH) != -1
                assert val.find(template.CONFUSABLES_CHARS_END_WITH) != -1

    elif template.method == WMMethod.FIND_AND_REPLACE:
        for key, val in template.CONFUSABLES_CHARS.items():
            # print(key, val[0], val[1], len(key), len(val))
            assert key == val[0]
    # elif template.method == WMMethod.APPEND_TO_CHAR | WMMethod.INSERT_INTO_POSITION:
    #     assert 2 <= template.CONFUSABLES_CHARS_LENGTH <= 36


def test_templates():
    """test templates"""

    templates = [
        combining_chars,
        font_color,
        font_float,
        font_size,
        font_style,
        font_weight,
        homograph_chinese,
        homograph_letters,
        homograph_numbers,
        homograph_punctuations,
        html_empty_tags,
        invisible_chars,
        space_chars,
        whitespace_chars,
    ]
    for template in templates:
        _test_templates(template)
