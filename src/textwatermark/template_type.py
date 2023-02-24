'''Template type define'''
from enum import Enum, unique

from textwatermark.templates import (binary_representation, combining_chars,
                                     font_color, font_float, font_size,
                                     font_style, font_weight,
                                     homograph_chinese, homograph_letters,
                                     homograph_numbers, homograph_punctuations,
                                     html_empty_tags, invisible_chars,
                                     space_chars, whitespace_chars)


@unique
class WMTemplateType(Enum):
    '''watermark template types'''

# WMMethod.INSERT_INTO_POSITION
    # 不可见字符
    INVISIBLE_CHARS = invisible_chars
    '''Invisible characters
    Notes: WMMethod.INSERT_INTO_POSITION
        WMMethod.INSERT_INTO_POSITION'''

    # 空白字符
    WHITESPACE_CHARS = whitespace_chars
    '''White space characters
    Notes: WMMethod.INSERT_INTO_POSITION
        WMMethod.INSERT_INTO_POSITION'''

    # HTML空白标签
    HTML_EMPTY_TAGS = html_empty_tags
    '''HTML empty tags
    Notes: WMMethod.INSERT_INTO_POSITION
        WMMethod.INSERT_INTO_POSITION'''


# WMMethod.FIND_AND_REPLACE
    SPACE_CHARS = space_chars
    '''Space characters
    Notes: WMMethod.FIND_AND_REPLACE
        WMMethod.FIND_AND_REPLACE'''

    # 同形异义字-数字
    HOMOGRAPH_NUMBERS = homograph_numbers
    '''Homograph numbers
    Notes: WMMethod.FIND_AND_REPLACE
        WMMethod.FIND_AND_REPLACE'''

    # 同形异义字-英文
    HOMOGRAPH_LETTERS = homograph_letters
    '''Homograph letters
    Notes: WMMethod.FIND_AND_REPLACE
        WMMethod.FIND_AND_REPLACE'''

    # 同形异义字-符号
    HOMOGRAPH_PUNCTUATIONS = homograph_punctuations
    '''Homograph punctuations
    Notes: WMMethod.FIND_AND_REPLACE
        WMMethod.FIND_AND_REPLACE'''

    # 同形异义字-汉字
    HOMOGRAPH_CHINESE = homograph_chinese
    '''Homograph Chinese
    Notes: WMMethod.FIND_AND_REPLACE
        WMMethod.FIND_AND_REPLACE'''

    # 繁体字
    # TRADITIONAL_CHINESE = 3007
    # 错别字-汉字
    # WRONG_CHINESE = 3008
    # 错别字-单词
    # WRONG_WORDS = 3009
    # 同义替换-数字
    # SYNONYM_NUMBERS = 3010
    # 同义替换-汉字
    # SYNONYM_CHINESE = 3011
    # 同义替换-单词
    # SYNONYM_WORDS = 3012


# WMMethod.APPEND_TO_CHAR
    # 组合字符
    COMBINING_CHARS = combining_chars
    '''Combining characters
    Notes: WMMethod.APPEND_TO_CHAR
        WMMethod.APPEND_TO_CHAR'''


# WMMethod.DECORATE_EACH_CHAR
    # 字体颜色
    FONT_COLOR = font_color
    '''Font color
    Notes: WMMethod.DECORATE_EACH_CHAR
        WMMethod.DECORATE_EACH_CHAR'''

    # 字体大小
    FONT_SIZE = font_size
    '''Font size
    Notes: WMMethod.DECORATE_EACH_CHAR
        WMMethod.DECORATE_EACH_CHAR'''
    # 字体粗细
    FONT_WEIGHT = font_weight
    '''Font weight
    Notes: WMMethod.DECORATE_EACH_CHAR
        WMMethod.DECORATE_EACH_CHAR'''

    # 字体浮动
    FONT_FLOAT = font_float
    '''Font float
    Notes: WMMethod.DECORATE_EACH_CHAR
        WMMethod.DECORATE_EACH_CHAR'''

    # 字体样式
    FONT_STYLE = font_style
    '''Font style
    Notes: WMMethod.DECORATE_EACH_CHAR
        WMMethod.DECORATE_EACH_CHAR'''

# WMMethod.APPEND_AS_BINARY

    BINARY_REPRESENTATION = binary_representation
    '''Delete character
    Notes: WMMethod.APPEND_AS_BINARY
        WMMethod.APPEND_AS_BINARY'''
