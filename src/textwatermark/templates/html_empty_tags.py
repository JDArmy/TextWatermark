'''
HTML empty tags template can only be used when the text can be displayed in HTML mode.
Such as WEB page, Blog, EMail, etc. 

All the tags below are inline tags.

Note: Some of HTML editor will remove empty or outside of list tags.
    Therefore, this template is not a relatively stable template, 
    and it is not recommended to use it in most cases.
'''

from textwatermark.defines import WMMethod

# 空格字符
CONFUSABLES_CHARS = [
    '<a></a>',
    '<abbr></abbr>',
    '<b></b>',
    '<bdo></bdo>',
    '<big></big>',
    '<cite></cite>',
    '<code></code>',
    '<dfn></dfn>',
    '<em></em>',
    '<i></i>',
    '<kbd></kbd>',
    '<var></var>',
    '<samp></samp>',
    '<span></span>',
    '<strong></strong>',
    '<small></small>',
    '<sub></sub>',
    '<sup></sup>',
    '<tt></tt>',
    '<u></u>',
]

method = WMMethod.INSERT_INTO_POSITION
