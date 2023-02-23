'''
Font style template can only be used when the text can be displayed in HTML mode.
Such as WEB page, Blog, EMail, etc. 
You can customize your own style pairs following the template format.

Note: Need to wrap surrounding elements
    It should be noted that all text needs to be wrapped with a layer of elements in 
    order to obtain a unified style display

Warning: confusables_chars_key is needed
    You can choose one of the key to insert the watermark

'''

from textwatermark.common import add_head_n_tial_to_dict
from textwatermark.defines import WMMethod

# 组合字符，如音标等
CONFUSABLES_CHARS_START_WITH = '<span style="'
CONFUSABLES_CHARS_END_WITH = ';">{char}</span>'
CONFUSABLES_CHARS = {
    'text-decoration-underline': ['text-decoration:none', 'text-decoration:underline'],
    'text-decoration-line-through': ['text-decoration: none', 'text-decoration: line-through'],
    'text-decoration-overline': ['text-decoration: none', 'text-decoration: overline'],
    'background-color-white-gray-1': ['background-color:#fff', 'background-color:#eee'],
    'background-color-white-gray-2': ['background-color:#fff', 'background-color:#ddd'],
    'background-color-white-red-1': ['background-color:#fff', 'background-color:#eff'],
    'background-color-white-red-2': ['background-color:#fff', 'background-color:#dff'],
    'background-color-white-green-1': ['background-color:#fff', 'background-color:#fef'],
    'background-color-white-green-2': ['background-color:#fff', 'background-color:#fdf'],
    'background-color-white-blue-1': ['background-color:#fff', 'background-color:#ffe'],
    'background-color-white-blue-2': ['background-color:#fff', 'background-color:#ffd'],
    'background-color-black-gray-1': ['background-color:#000', 'background-color:#111'],
    'background-color-black-gray-2': ['background-color:#000', 'background-color:#222'],
    'background-color-black-red-1': ['background-color:#000', 'background-color:#100'],
    'background-color-black-red-2': ['background-color:#000', 'background-color:#200'],
    'background-color-black-green-1': ['background-color:#000', 'background-color:#010'],
    'background-color-black-green-2': ['background-color:#000', 'background-color:#020'],
    'background-color-black-blue-1': ['background-color:#000', 'background-color:#001'],
    'background-color-black-blue-2': ['background-color:#000', 'background-color:#002'],
    'border-top-white-dashed-1': ['border-top: ;', 'border-top: 1px dashed #eee;'],
    'border-top-white-dashed-2': ['border-top: ;', 'border-top: 1px dashed #ddd;'],
    'border-top-white-dashed-3': ['border-top: ;', 'border-top: 1px dashed #ccc;'],
    'border-bottom-white-dashed-1': ['border-bottom: ;', 'border-bottom: 1px dashed #eee;'],
    'border-bottom-white-dashed-2': ['border-bottom: ;', 'border-bottom: 1px dashed #ddd;'],
    'border-bottom-white-dashed-3': ['border-bottom: ;', 'border-bottom: 1px dashed #ccc;'],
    'border-left-white-dashed-1': ['border-left: ;', 'border-left: 1px dashed #eee;'],
    'border-left-white-dashed-2': ['border-left: ;', 'border-left: 1px dashed #ddd;'],
    'border-left-white-dashed-3': ['border-left: ;', 'border-left: 1px dashed #ccc;'],
    'border-right-white-dashed-1': ['border-right: ;', 'border-right: 1px dashed #eee;'],
    'border-right-white-dashed-2': ['border-right: ;', 'border-right: 1px dashed #ddd;'],
    'border-right-white-dashed-3': ['border-right: ;', 'border-right: 1px dashed #ccc;'],
    'border-top-white-solid-1': ['border-top: ;', 'border-top: 1px solid #eee;'],
    'border-top-white-solid-2': ['border-top: ;', 'border-top: 1px solid #ddd;'],
    'border-top-white-solid-3': ['border-top: ;', 'border-top: 1px solid #ccc;'],
    'border-bottom-white-solid-1': ['border-bottom: ;', 'border-bottom: 1px solid #eee;'],
    'border-bottom-white-solid-2': ['border-bottom: ;', 'border-bottom: 1px solid #ddd;'],
    'border-bottom-white-solid-3': ['border-bottom: ;', 'border-bottom: 1px solid #ccc;'],
    'border-left-white-solid-1': ['border-left: ;', 'border-left: 1px solid #eee;'],
    'border-left-white-solid-2': ['border-left: ;', 'border-left: 1px solid #ddd;'],
    'border-left-white-solid-3': ['border-left: ;', 'border-left: 1px solid #ccc;'],
    'border-right-white-solid-1': ['border-right: ;', 'border-right: 1px solid #eee;'],
    'border-right-white-solid-2': ['border-right: ;', 'border-right: 1px solid #ddd;'],
    'border-right-white-solid-3': ['border-right: ;', 'border-right: 1px solid #ccc;'],
    'font-style-italic': ['font-style:normal', 'font-style:italic']

}

add_head_n_tial_to_dict(
    CONFUSABLES_CHARS, CONFUSABLES_CHARS_START_WITH, CONFUSABLES_CHARS_END_WITH)

method = WMMethod.DECORATE_EACH_CHAR
