'''module docstring'''

from textwatermark.common import add_head_n_tial_to_dict
from textwatermark.defines import WMMethod

# 组合字符，如音标等
CONFUSABLES_CHARS_START_WITH = '<span style="'
CONFUSABLES_CHARS_END_WITH = ';">{char}</span>'
CONFUSABLES_CHARS = {
    'text-decoration-underline': ['text-decoration:none', 'text-decoration:underline'],
    'text-decoration-line-through': ['text-decoration: none', 'text-decoration: line-through'],
    'text-decoration-overline': ['text-decoration: none', 'text-decoration: overline']
}

add_head_n_tial_to_dict(
    CONFUSABLES_CHARS, CONFUSABLES_CHARS_START_WITH, CONFUSABLES_CHARS_END_WITH)

method = WMMethod.DECORATE_EACH_CHAR
