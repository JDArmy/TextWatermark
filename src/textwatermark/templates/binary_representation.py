'''
Insert the selected character after the text to represent a 1 in binary, otherwise 0.

The characters are from [combining_chars][], [invisible_chars][] and [whitespace_chars][].

Warning: confusables_chars_key is needed
    You can choose one of the characters to insert the watermark

Info: Differents between combining_chars, invisible_chars and whitespace_chars
    [combining_chars][]: Small but recognizable difference in characters 
    before and after watermarking

    [invisible_chars][]: You can't see the difference between before 
    and after inserting the watermark

    [whitespace_chars][]: There is a small but recognizable difference in 
    the spacing of characters before and after watermarking

'''

from textwatermark.defines import WMMethod
from textwatermark.templates import (combining_chars, invisible_chars,
                                     whitespace_chars)

CONFUSABLES_CHARS_LIST = combining_chars.CONFUSABLES_CHARS + \
    invisible_chars.CONFUSABLES_CHARS + whitespace_chars.CONFUSABLES_CHARS + \
    ['\u007F']

CONFUSABLES_CHARS = dict(
    zip(CONFUSABLES_CHARS_LIST, CONFUSABLES_CHARS_LIST))

method = WMMethod.APPEND_AS_BINARY
