'''
Font color template can only be used when the text can be displayed in HTML mode.
Such as WEB page, Blog, EMail, etc. 
You can customize your own color pairs following the template format.

Note: Need to wrap surrounding elements
    It should be noted that all text needs to be wrapped with a layer of elements in 
    order to obtain a unified style display

Warning: confusables_chars_key is needed
    You can choose one of the key to insert the watermark

'''

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
    'black5': ['#000', '#555'],
    'black6': ['#000', '#666'],
    'white1': ['#fff', '#eee'],
    'white2': ['#fff', '#ddd'],
    'white3': ['#fff', '#ccc'],
    'white4': ['#fff', '#bbb'],
    'white5': ['#fff', '#aaa'],
    'white6': ['#fff', '#999'],
}

add_head_n_tial_to_dict(
    CONFUSABLES_CHARS, CONFUSABLES_CHARS_START_WITH, CONFUSABLES_CHARS_END_WITH)

method = WMMethod.DECORATE_EACH_CHAR
