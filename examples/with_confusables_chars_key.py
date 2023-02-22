'''example'''
import os

from textwatermark.defines import WMMode
from textwatermark.main import TextWatermark
from textwatermark.template_type import WMTemplateType

wm_mode = WMMode.REAL_NUMBER
wm_max = '9'*9
# init
wm = TextWatermark(wm_mode)
wm.set_tpl_type(WMTemplateType.INVISIBLE_COMBINING_CHARS, '\u0300')
wm.set_wm_max(wm_max=wm_max)
wm.set_text_file(os.path.abspath('../tests/text/1.txt'))

# insert watermark
wm_str = '123456789'
wm_text = wm.insert_watermark(wm_str)
print(wm_text)

# Save the parameters to retrieve the watermark
params = wm.export_params()

# retrieve the watermark
wm_out_str = TextWatermark.retrieve_watermark(wm_text, params)

assert wm_out_str == wm_str
