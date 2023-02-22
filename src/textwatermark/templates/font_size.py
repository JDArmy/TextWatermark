'''module docstring'''

from textwatermark.common import add_head_n_tial_to_dict
from textwatermark.defines import WMMethod

# 组合字符，如音标等
CONFUSABLES_CHARS_START_WITH = '<span style="font-size: '
CONFUSABLES_CHARS_END_WITH = '">{char}</span>'
CONFUSABLES_CHARS = {
    '101': ['100%', '101%'],
    '102': ['100%', '102%'],
    '103': ['100%', '103%'],
    '104': ['100%', '104%'],
    '105': ['100%', '105%'],
    '106': ['100%', '106%'],
    '107': ['100%', '107%'],
    '108': ['100%', '108%'],
    '109': ['100%', '109%'],
    '110': ['100%', '110%'],
    '111': ['100%', '111%'],
    '112': ['100%', '112%'],
    '113': ['100%', '113%'],
    '114': ['100%', '114%'],
    '115': ['100%', '115%'],
    '116': ['100%', '116%'],
    '117': ['100%', '117%'],
    '118': ['100%', '118%'],
    '119': ['100%', '119%'],
    '120': ['100%', '120%'],
}

add_head_n_tial_to_dict(
    CONFUSABLES_CHARS, CONFUSABLES_CHARS_START_WITH, CONFUSABLES_CHARS_END_WITH)

method = WMMethod.DECORATE_EACH_CHAR
