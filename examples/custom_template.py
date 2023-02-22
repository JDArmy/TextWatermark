'''example'''
import os

from textwatermark.common import add_head_n_tial_to_dict
from textwatermark.defines import WMMethod, WMMode
from textwatermark.main import TextWatermark


class CustomTemplate:
    CONFUSABLES_CHARS_START_WITH = '<span style="color: '
    CONFUSABLES_CHARS_END_WITH = '">{char}</span>'
    CONFUSABLES_CHARS = {
        'red1': ['#FF0000', '#CC0000'],
    }
    add_head_n_tial_to_dict(
        CONFUSABLES_CHARS, CONFUSABLES_CHARS_START_WITH, CONFUSABLES_CHARS_END_WITH)

    method = WMMethod.DECORATE_EACH_CHAR
    CONFUSABLES_CHARS_LENGTH = len(list(CONFUSABLES_CHARS.values())[0])


wm_mode = WMMode.REAL_NUMBER

template = CustomTemplate
confusables_chars_key = 'red1'
text_wrap = template.CONFUSABLES_CHARS[confusables_chars_key][0]

wm_base = template.CONFUSABLES_CHARS_LENGTH
wm_max = '9'*9

# init
wm = TextWatermark(wm_mode, wm_base)
wm.set_wm_max(wm_max=wm_max)
wm.set_tpl(template.CONFUSABLES_CHARS,
           template.CONFUSABLES_CHARS_LENGTH,
           template.method,
           confusables_chars_key)
wm.set_text_file(os.path.abspath(
    os.path.dirname(__file__)+'/../tests/text/1.txt'))

# insert watermark
wm_loop = False
start_at = 0
wm_str = '123456789'

wm_text = wm.insert_watermark(wm_str, start_at, wm_loop)


wm_text = text_wrap.replace('{char}', wm_text)

print(wm_text)

# Save the parameters to retrieve the watermark
params = wm.export_params(start_at, wm_loop)

# retrieve the watermark
wm_out_str = TextWatermark.retrieve_watermark(wm_text, params)

assert wm_out_str == wm_str
