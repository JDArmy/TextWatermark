'''TextWatermark's Template'''

from textwatermark.defines import WMMethod
from textwatermark.templates import (combining_chars, invisible_chars,
                                     whitespace_chars)

CONFUSABLES_CHARS_LIST = combining_chars.CONFUSABLES_CHARS + \
    invisible_chars.CONFUSABLES_CHARS + whitespace_chars.CONFUSABLES_CHARS

CONFUSABLES_CHARS = dict(zip(CONFUSABLES_CHARS_LIST, CONFUSABLES_CHARS_LIST))

method = WMMethod.APPEND_AS_BINARY
