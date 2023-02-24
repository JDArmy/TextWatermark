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


wm_mode = WMMode.REAL_NUMBER
wm_max = '9'*9

confusables_chars_key = 'red1'
text_wrap = CustomTemplate.CONFUSABLES_CHARS[confusables_chars_key][0]

# init
wm = TextWatermark(wm_mode, start_at=0, wm_loop=False)
wm.set_tpl(CustomTemplate.CONFUSABLES_CHARS,
           CustomTemplate.method,
           confusables_chars_key)

wm.set_wm_max(wm_max=wm_max)
wm.set_text_file(os.path.abspath(
    os.path.abspath('../tests/text/1.txt')))

# insert watermark

wm_str = '123456789'
wm_text = wm.insert_watermark(wm_str)


wm_text = text_wrap.replace('{char}', wm_text)
print(wm_text)

# Save the parameters to retrieve the watermark
params = wm.export_params()

# retrieve the watermark
wm_out_str = TextWatermark.retrieve_watermark(wm_text, params)

assert wm_out_str == wm_str
