'''
This template will replace the regular space char with the other width of space chars.

Since spaces are rare in Chinese, this template is mainly suitable for English text.
'''

from textwatermark.defines import WhiteSpaceChars, WMMethod

# 空格字符
CONFUSABLES_CHARS = {
    '\u0020': [
        WhiteSpaceChars.SPACE_1_4.value,
        # WhiteSpaceChars.NO_BREAK_SPACE_1_4.value,
        # WhiteSpaceChars.EN_QUAD_1_2.value,
        # WhiteSpaceChars.EM_QUAD_1.value,
        WhiteSpaceChars.EN_SPACE_1_2.value,
        WhiteSpaceChars.EM_SPACE_1.value,
        WhiteSpaceChars.THREE_PER_EM_SPACE_1_3.value,
        # WhiteSpaceChars.FOUR_PER_EM_SPACE_1_4.value,
        WhiteSpaceChars.SIX_PER_EM_SPACE_1_6.value,
        # WhiteSpaceChars.FIGURE_SPACE_LIKE_DIGITS.value,
        # WhiteSpaceChars.PUNCTUATION_SPACE_LIKE_DOT.value,
        # WhiteSpaceChars.THIN_SPACE_1_6.value,
        WhiteSpaceChars.HAIR_SPACE_1_8.value,
        # WhiteSpaceChars.NARROW_NO_BREAK_SPACE_1_6.value,
        # WhiteSpaceChars.MEDIUM_MATHEMATICAL_SPACE_2_9.value,
    ]
}

method = WMMethod.FIND_AND_REPLACE
