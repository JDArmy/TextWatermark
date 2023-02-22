'''module docstring'''

from textwatermark.common import add_head_n_tial_to_dict
from textwatermark.defines import WMMethod

# 组合字符，如音标等
CONFUSABLES_CHARS_START_WITH = '<span style="font-weight: '
CONFUSABLES_CHARS_END_WITH = ';">{char}</span>'
CONFUSABLES_CHARS = {
    'lighter': ['normal', 'lighter'],
    'bolder': ['normal', 'bolder'],
    '100-200': ['100', '200'],
    '200-300': ['200', '300'],
    '300-400': ['300', '400'],
    '400-500': ['400', '500'],
    '500-600': ['500', '600'],
    '600-700': ['600', '700'],
    '700-800': ['700', '800'],
    '800-900': ['800', '900'],
}

add_head_n_tial_to_dict(
    CONFUSABLES_CHARS, CONFUSABLES_CHARS_START_WITH, CONFUSABLES_CHARS_END_WITH)

method = WMMethod.DECORATE_EACH_CHAR
