"""test WMTemplate"""
# pylint: disable=invalid-name

import pytest

from textwatermark.defines import WhiteSpaceChars
from textwatermark.template import WMTemplate
from textwatermark.templates import (
    binary_representation,
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


def _test_template(template, text, wm_final, start_at, confusables_chars_key=""):
    confusables_chars_length = WMTemplate.get_wm_base_from_tpl(
        template.CONFUSABLES_CHARS
    )

    for wm_base in range(2, confusables_chars_length + 1):
        wmt = WMTemplate(
            template.CONFUSABLES_CHARS, wm_base, template.method, confusables_chars_key
        )

        wm_text = wmt.insert_watermark(
            text=text, wm_final=wm_final, start_at=start_at, loop=False
        )

        wm_out = wmt.retrieve_watermark(
            wm_text=wm_text,
            wm_base=wmt.wm_base,
            wm_len=len(wm_final),
            start_at=start_at,
        )
        print(wm_text, wm_final, wm_out, wmt.wm_base)
        assert wm_final == wm_out


def test_template():
    """test every template"""
    _test_template(
        template=homograph_numbers,
        text="a1a2a3a4a5a6a7a8a9a0a1a2a3a4a5a6a7a89aa0",
        wm_final="101101",
        start_at=4,
    )
    _test_template(
        template=homograph_chinese, text="有八个人抱着白包往北边走", wm_final="101101", start_at=1
    )
    _test_template(
        template=homograph_letters,
        text="Monyer love you",
        wm_final="101101",
        start_at=2,
    )
    _test_template(
        template=homograph_punctuations,
        text="Mon\"yer, love, you.ve_ry-mu'ch.",
        wm_final="101101",
        start_at=1,
    )
    _test_template(
        template=space_chars,
        text="有 八 个 人 抱 着 白 包 往 北 边 走有 八 个 人 抱 ",
        wm_final="101101",
        start_at=1,
    )

    _test_template(
        template=whitespace_chars, text="从前有座庙，庙里有个老和尚", wm_final="101101", start_at=1
    )
    _test_template(
        template=invisible_chars, text="从前有座庙，庙里有个老和尚", wm_final="101101", start_at=1
    )
    _test_template(
        template=html_empty_tags, text="从前有座庙，庙里有个老和尚", wm_final="101101", start_at=1
    )

    _test_template(
        template=combining_chars,
        text="从前有座庙，庙里有个老和尚叫Monyer。",
        wm_final="101101",
        start_at=1,
    )

    _test_template(
        template=font_color,
        text="从前有座庙，庙里有个老和尚。",
        wm_final="101101",
        start_at=1,
        confusables_chars_key="black3",
    )
    _test_template(
        template=font_size,
        text="从前有座庙，庙里有个老和尚。",
        wm_final="101101",
        start_at=1,
        confusables_chars_key="110",
    )
    _test_template(
        template=font_float,
        text="从前有座庙，庙里有个老和尚。",
        wm_final="101101",
        start_at=1,
        confusables_chars_key="up3",
    )
    _test_template(
        template=font_weight,
        text="从前有座庙，庙里有个老和尚。",
        wm_final="101101",
        start_at=1,
        confusables_chars_key="100-200",
    )
    _test_template(
        template=font_style,
        text="从前有座庙，庙里有个老和尚。",
        wm_final="101101",
        start_at=1,
        confusables_chars_key="text-decoration-overline",
    )

    _test_template(
        template=binary_representation,
        text="从前有座庙，庙里有个老和尚。",
        wm_final="1000001101",
        start_at=1,
        confusables_chars_key="\u0300",
    )

    _test_template(
        template=binary_representation,
        text="从前有座庙，庙里有个老和尚。",
        wm_final="1000001101000",
        start_at=1,
        confusables_chars_key="\u0300",
    )
    with pytest.raises(ValueError):
        # no key, WMMethod.DECORATE_EACH_CHAR
        _test_template(
            template=font_style, text="从前有座庙，庙里有个老和尚。", wm_final="101101", start_at=1
        )
    with pytest.raises(ValueError):
        # text too short
        _test_template(
            template=homograph_numbers, text="a1a2", wm_final="101101", start_at=1
        )
    with pytest.raises(ValueError):
        # start_at large, and text too short
        _test_template(
            template=homograph_numbers, text="a1a2a3a4", wm_final="101", start_at=10
        )

    with pytest.raises(ValueError):
        # no key, WMMethod.APPEND_AS_BINARY
        _test_template(
            template=binary_representation,
            text="从前有座庙，庙里有个老和尚。",
            wm_final="100000110",
            start_at=0,
        )

    with pytest.raises(ValueError):
        # text too short
        _test_template(
            template=binary_representation,
            text="从前有座庙",
            wm_final="100000110",
            start_at=10,
            confusables_chars_key="\u0300",
        )


def test_clean_html_tags():
    """test clean_html_tags"""

    template = homograph_numbers
    wmt = WMTemplate(template.CONFUSABLES_CHARS, 2, template.method)
    assert wmt.clean_html_tags("<b>a1a2a3a4</b>") == "a1a2a3a4"
    assert wmt.clean_html_tags("<b>a1a2a3a4") == "a1a2a3a4"
    assert wmt.clean_html_tags("a1a2a3a4</b>") == "a1a2a3a4"


def _test_clean_text(template, text, new_text, confusables_chars_key=""):
    wmt = WMTemplate(
        template.CONFUSABLES_CHARS, 2, template.method, confusables_chars_key
    )
    assert wmt.clean_text(new_text) == text


def test_clean_text():
    """test clean_text"""
    text = "a1a2a3a4"
    # INSERT_INTO_POSITION
    new_text = text[0] + WhiteSpaceChars.NO_BREAK_SPACE_1_4.value + text[1:]
    _test_clean_text(template=whitespace_chars, text=text, new_text=new_text)

    new_text = f"<script>{text}</script><a></a>"
    _test_clean_text(template=html_empty_tags, text=text, new_text=new_text)

    new_text = text[0] + "\u034f" + text[1:]
    _test_clean_text(template=invisible_chars, text=text, new_text=new_text)

    # FIND_AND_REPLACE
    _test_clean_text(template=homograph_chinese, text=text + "敖", new_text=text + "敖")
    _test_clean_text(
        template=homograph_letters, text=text + "AAAAAAA", new_text=text + "ΑАᎪꓮ𝐀𝖠𝗔"
    )
    _test_clean_text(
        template=homograph_numbers, text=text + "000000", new_text=text + "᱐𝟘𝟎𝟢𝟬𝟶"
    )
    _test_clean_text(
        template=homograph_punctuations, text=text + "!!", new_text=text + "ǃ！"
    )
    _test_clean_text(
        template=space_chars,
        text=text + WhiteSpaceChars.SPACE_1_4.value,
        new_text=text + WhiteSpaceChars.EN_SPACE_1_2.value,
    )

    # APPEND_TO_CHAR
    new_text = text[0] + "\u0306" + text[1:]
    _test_clean_text(template=combining_chars, text=text, new_text=new_text)

    # DECORATE_EACH_CHAR
    new_text = f'<span style="color: #000">{text}</span>'
    _test_clean_text(
        template=font_color,
        text=text,
        new_text=new_text,
        confusables_chars_key="black1",
    )

    new_text = f'<span style="display: inline-block;">{text}</span>'
    _test_clean_text(
        template=font_float, text=text, new_text=new_text, confusables_chars_key="up1"
    )

    new_text = f'<span style="font-size: 100%">{text}</span>'
    _test_clean_text(
        template=font_size, text=text, new_text=new_text, confusables_chars_key="101"
    )

    new_text = f'<span style=";">{text}</span>'
    _test_clean_text(
        template=font_style,
        text=text,
        new_text=new_text,
        confusables_chars_key="text-decoration-underline",
    )

    new_text = f'<span style="font-weight: normal;">{text}</span>'
    _test_clean_text(
        template=font_weight,
        text=text,
        new_text=new_text,
        confusables_chars_key="lighter",
    )

    # APPEND_AS_BINARY
    text = "1月10日,美图公司创始人兼CEO吴欣鸿发送了一封内部全员邮件,涉及经营战略、科技创新、未来发展等多个层面"
    new_text = "1̀月10日̀,̀美̀图公̀司创̀始̀人兼̀C̀ÈÒ吴欣鸿̀发̀送了̀一封内部̀全员̀邮件̀,涉及经营战略、科技创新、未来发展等多个层面"
    _test_clean_text(
        template=binary_representation,
        text=text,
        new_text=new_text,
        confusables_chars_key="\u0300",
    )
