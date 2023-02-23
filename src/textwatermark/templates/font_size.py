'''
Font size template can only be used when the text can be displayed in HTML mode.
Such as WEB page, Blog, EMail, etc. 

Note: Need to wrap surrounding elements
    It should be noted that all text needs to be wrapped with a layer of elements in 
    order to obtain a unified style display
    
Warning: confusables_chars_key is needed
    You can choose one of the key to insert the watermark

'''

from textwatermark.common import add_head_n_tial_to_dict
from textwatermark.defines import WMMethod

# 组合字符，如音标等
CONFUSABLES_CHARS_START_WITH = '<span style="font-size: '
CONFUSABLES_CHARS_END_WITH = '">{char}</span>'
CONFUSABLES_CHARS = {
    '80': ['100%', '80%'],
    '81': ['100%', '81%'],
    '82': ['100%', '82%'],
    '83': ['100%', '83%'],
    '84': ['100%', '84%'],
    '85': ['100%', '85%'],
    '86': ['100%', '86%'],
    '87': ['100%', '87%'],
    '88': ['100%', '88%'],
    '89': ['100%', '89%'],
    '90': ['100%', '90%'],
    '91': ['100%', '91%'],
    '92': ['100%', '92%'],
    '93': ['100%', '93%'],
    '94': ['100%', '94%'],
    '95': ['100%', '95%'],
    '96': ['100%', '96%'],
    '97': ['100%', '97%'],
    '98': ['100%', '98%'],
    '99': ['100%', '99%'],
    # '100': ['100%', '100%'],
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
