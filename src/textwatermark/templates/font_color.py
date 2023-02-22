'''module docstring'''

from textwatermark.common import add_head_n_tial_to_dict
from textwatermark.defines import WMMethod

# 组合字符，如音标等
CONFUSABLES_CHARS_START_WITH = '<span style="color: '
CONFUSABLES_CHARS_END_WITH = '">{char}</span>'
CONFUSABLES_CHARS = {
    'black1': ['#000', '#111'],
    'black2': ['#000', '#222'],
    'black3': ['#000', '#333'],
    'black4': ['#000', '#444'],
    'white1': ['#fff', '#eee'],
    'white2': ['#fff', '#ddd'],
    'white3': ['#fff', '#ccc'],
    'white4': ['#fff', '#bbb'],
}

add_head_n_tial_to_dict(
    CONFUSABLES_CHARS, CONFUSABLES_CHARS_START_WITH, CONFUSABLES_CHARS_END_WITH)

method = WMMethod.DECORATE_EACH_CHAR
