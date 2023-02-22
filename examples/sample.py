'''Sample Example'''
import os

from textwatermark.defines import WMMode
from textwatermark.main import TextWatermark
from textwatermark.template_type import WMTemplateType

# 1.Init TextWatermark instance
wm_mode = WMMode.REAL_NUMBER
wm = TextWatermark(wm_mode=wm_mode)

# 2.Choose a watermark template
wm.set_tpl_type(tpl_type=WMTemplateType.HOMOGRAPH_NUMBERS)

# 3.Set the maximum value of the watermark string
wm_max = '9'*9
wm.set_wm_max(wm_max=wm_max)

# 4.Set the text to be watermarked
wm.set_text_file(path=os.path.abspath('../tests/text/1.txt'))

# 5.Insert watermark string to text
wm_str = '123456789'
wm_text = wm.insert_watermark(wm_str=wm_str)
print(wm_text)

##############################################################

# Save the parameters to retrieve the watermark
params = wm.export_params()

# retrieve the watermark
wm_out_str = TextWatermark.retrieve_watermark(wm_text=wm_text, params=params)

assert wm_out_str == wm_str
