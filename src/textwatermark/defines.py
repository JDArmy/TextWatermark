"""Defines"""

from enum import Enum, IntEnum, unique


@unique
class WMMode(IntEnum):
    """An enumerarion of watermark mode"""

    REAL_NUMBER: int = 1
    """Real numbers, which will be represented directly by binary values, 
        with the smallest length"""

    LETTERS_LOWER_CASE: int = 2
    """Lowercase letters, each letter is represented by 5 binary bytes"""

    LETTERS_UPPER_CASE: int = 3
    """Uppercase letters, each letter is represented by 5 binary bytes"""

    LETTERS_MIXED_CASE: int = 4
    """Mixed case letters, each character is represented by 6 binary bytes"""

    ALPHA_NUMERICAL: int = 5
    """Uppercase and lowercase letters + numbers, each character is represented by 6 binary bytes"""

    ALPHA_NUMERICAL_SPECIAL: int = 6
    """Uppercase and lowercase letters + numbers + special symbols, 
        each character is represented by 7 binary bytes"""

    UNICODE: int = 7
    """Arbitrary Unicode characters, expressed in UTF-8 encoding"""


@unique
class WMMethod(IntEnum):
    """Watermark insert methods"""

    # 查找特定字符并替换成水印字符
    FIND_AND_REPLACE: int = 1
    """Find specific characters and replace with watermark characters"""

    # 在指定位置插入不可见水印
    INSERT_INTO_POSITION: int = 2
    """Insert an invisible watermark at the specified position"""

    # 对文本中的字符进行修饰
    DECORATE_EACH_CHAR: int = 3
    """Decorate characters in text"""

    # 在字符后添加单个水印
    APPEND_TO_CHAR: int = 4
    """Add one watermark byte after one character"""

    # 以二进制形式在字符后面添加水印字符
    APPEND_AS_BINARY: int = 5
    """Add one watermark byte after one character, in binary"""


@unique
class WhiteSpaceChars(Enum):
    """Defines of white space chars

    From: <https://jkorpela.fi/chars/spaces.html>
    """

    SPACE_1_4: str = "\u0020"
    """Depends on font, typically 1/4 em, often adjusted"""

    NO_BREAK_SPACE_1_4: str = "\u00A0"
    """As a space, but often not adjusted"""

    EN_QUAD_1_2: str = "\u2000"
    """1 en (= 1/2 em)"""

    EM_QUAD_1: str = "\u2001"
    """	1 em (nominally, the height of the font)"""

    EN_SPACE_1_2: str = "\u2002"
    """1 en (= 1/2 em)"""

    EM_SPACE_1: str = "\u2003"
    """1 em"""

    THREE_PER_EM_SPACE_1_3: str = "\u2004"
    """1/3 em"""

    FOUR_PER_EM_SPACE_1_4: str = "\u2005"
    """1/4 em"""

    SIX_PER_EM_SPACE_1_6: str = "\u2006"
    """1/6 em"""

    FIGURE_SPACE_LIKE_DIGITS: str = "\u2007"
    """“Tabular width”, the width of digits"""

    PUNCTUATION_SPACE_LIKE_DOT: str = "\u2008"
    """The width of a period “.”"""

    THIN_SPACE_1_6: str = "\u2009"
    """	1/5 em (or sometimes 1/6 em)"""

    HAIR_SPACE_1_8: str = "\u200A"
    """Narrower than `THIN SPACE`"""

    NARROW_NO_BREAK_SPACE_1_6: str = "\u202F"
    """Narrower than `NO-BREAK SPACE` (or `SPACE`), 
    “typically the width of a thin space or a mid space”"""

    MEDIUM_MATHEMATICAL_SPACE_2_9: str = "\u205F"
    """4/18 em"""
