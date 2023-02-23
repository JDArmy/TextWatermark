'''
In concept, a combining character is a mark of some kind intended to be positioned relative to 
some other character, which is referred to as its associated base character.
'''

from textwatermark.defines import WMMethod

# 组合字符，如音标等
CONFUSABLES_CHARS = [
    '\u0300', '\u0301', '\u0302', '\u0303', '\u0304', '\u0306', '\u0307', '\u0308',
    '\u0309', '\u030a', '\u030b', '\u030c', '\u030f', '\u0311', '\u031b', '\u0323',
    '\u0324', '\u0325', '\u0326', '\u0327', '\u0328', '\u032d', '\u032e', '\u0330',
    '\u0331', '\u0338', '\u0340', '\u0341', '\u0344', '\u0487', '\u05ba', '\u08e3',
    '\u0f72', '\u0f7c', '\u0f7d', '\u0f80', '\u2cef', '\u2cf0', '\u2cf1', '\ua66f',
    '\ua674', '\ua675', '\ua676', '\ua677', '\ua678', '\ua679', '\ua67a', '\ua67b',
    '\ua67c', '\ua67d', '\ua69f',
]
method = WMMethod.APPEND_TO_CHAR
