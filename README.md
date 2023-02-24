# TextWatermark

TextWatermark is a library for inserting watermarks into text

Please take a look at our documentation for how to install and use TextWatermark:

- [Website](https://textwatermark.jd.army/)
- [Github](https://github.com/JDArmy/TextWatermark)
- [Usage](https://textwatermark.jd.army/usage)
- [Changelog](https://textwatermark.jd.army/changelog)
- [API Documents](https://textwatermark.jd.army/api/main/)
- [Templates](https://textwatermark.jd.army/templates/)
- [PyPI](https://pypi.org/project/textwatermark/)

## Requirements

Tested on Python `>= 3.10`

## Installation

### Using Pip

`$ pip install textwatermark`

### From Code

```bash
git clone https://github.com/JDArmy/TextWatermark.git

cd TextWatermark

pip install .

# or in editable mode
pip install --editable .
```

## Usage

### CMD Line

#### Insert watermark into text

```console
$ textwatermark -v insert -f './tests/text/number.txt' -m ALPHA_NUMERICAL -t HOMOGRAPH_NUMBERS -x 999 -w 123

Ӏ2𝟑𝟒𝟓Ⳓ𝟟890
```

#### Export watermark parameters

```console
$ textwatermark -v insert -f './tests/text/number.txt' -m ALPHA_NUMERICAL -t HOMOGRAPH_NUMBERS -x 999 -w 123 -e

{"tpl_type": "HOMOGRAPH_NUMBERS", "confusables_chars": [], "confusables_chars_key": "", "wm_base": 7, "method": 1, "wm_mode": 5, "wm_len": 7, "wm_loop": false, "start_at": 0, "version": "0.1.2"}
```

#### Retrieve the watermark from the text

```console
$ textwatermark -v retrieve -f out.txt -p '{"tpl_type": "HOMOGRAPH_NUMBERS", "confusables_chars": [], "confusables_chars_key": "", "wm_base": 7, "method": 1, "wm_mode": 5, "wm_len": 7, "wm_loop": false, "start_at": 0, "version": "0.1.2"}'

The retrieved watermark is: 123
```

### Coding

```py
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

```

## More

See: [Documents](https://textwatermark.jd.army/)
