'''module docstring'''

from textwatermark.common import add_head_n_tial_to_dict
from textwatermark.defines import WMMethod

# 组合字符，如音标等
CONFUSABLES_CHARS_START_WITH = '<span style="display: inline-block;position: relative;'
CONFUSABLES_CHARS_END_WITH = ';">{char}</span>'
CONFUSABLES_CHARS = {
    'up1': ['top:0', 'top:-1px'],
    'up2': ['top:0', 'top:-2px'],
    'up3': ['top:0', 'top:-3px'],
    'bottom1': ['bottom:0', 'bottom:-1px'],
    'buttom2': ['bottom:0', 'bottom:-2px'],
    'bottom3': ['bottom:0', 'bottom:-3px'],
}

add_head_n_tial_to_dict(
    CONFUSABLES_CHARS, CONFUSABLES_CHARS_START_WITH, CONFUSABLES_CHARS_END_WITH)

method = WMMethod.DECORATE_EACH_CHAR
