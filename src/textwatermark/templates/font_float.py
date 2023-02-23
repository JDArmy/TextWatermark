'''
Font float template can only be used when the text can be displayed in HTML mode.
Such as WEB page, Blog, EMail, etc. 
You can customize your own float pairs following the template format.

Note: Need to wrap surrounding elements
    It should be noted that all text needs to be wrapped with a layer of elements in 
    order to obtain a unified style display

Warning: confusables_chars_key is needed
    You can choose one of the key to insert the watermark
'''

from textwatermark.common import add_head_n_tial_to_dict
from textwatermark.defines import WMMethod

# 组合字符，如音标等
CONFUSABLES_CHARS_START_WITH = '<span style="display: inline-block;position: relative;'
CONFUSABLES_CHARS_END_WITH = ';">{char}</span>'
CONFUSABLES_CHARS = {
    'up1': ['top:0', 'top:-1px'],
    'up2': ['top:0', 'top:-2px'],
    'up3': ['top:0', 'top:-3px'],
    'up4': ['top:0', 'top:-4px'],
    'up5': ['top:0', 'top:-5px'],
    'down1': ['bottom:0', 'bottom:-1px'],
    'down2': ['bottom:0', 'bottom:-2px'],
    'down3': ['bottom:0', 'bottom:-3px'],
    'down4': ['bottom:0', 'bottom:-4px'],
    'down5': ['bottom:0', 'bottom:-5px'],
    'left1': ['left:0', 'left:-1px'],
    'left2': ['left:0', 'left:-2px'],
    'left3': ['left:0', 'left:-3px'],
    'left4': ['left:0', 'left:-4px'],
    'left5': ['left:0', 'left:-5px'],
    'right1': ['right:0', 'right:-1px'],
    'right2': ['right:0', 'right:-2px'],
    'right3': ['right:0', 'right:-3px'],
    'right4': ['right:0', 'right:-4px'],
    'right5': ['right:0', 'right:-5px'],
}

add_head_n_tial_to_dict(
    CONFUSABLES_CHARS, CONFUSABLES_CHARS_START_WITH, CONFUSABLES_CHARS_END_WITH)

method = WMMethod.DECORATE_EACH_CHAR
