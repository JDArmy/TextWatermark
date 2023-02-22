# Usage

## The whole example code

```py
{%
  include-markdown "../examples/sample.py"
%}
```

There are 5 steps to insert a watermark into text.

### 1. Init TextWatermark instance

```py
from textwatermark.defines import WMMode
from textwatermark.main import TextWatermark

# Get instance of TextWatermark Class
wm_mode = WMMode.REAL_NUMBER
wm = TextWatermark(wm_mode=wm_mode)
```

TextWatermark's init takes 4 parameters:

`__init__(wm_mode, wm_base=0, start_at=0, wm_loop=False)`

`wm_mode`  is required.

`wm_mode` can be set to any attribute of `WMMode`, see [defines.WMMode](/api/defines/#textwatermark.defines.WMMode) for more.
Why does `wm_mode` need to set a value?

For minify the size of the watermark string.

The existence of `wm_base` is to specify the base for the final watermark string.

It is not necessary to set this value if you don't know what means. The default value of `wm_base` in `__init__` is 0 at first,
then will be set to `{template}.CONFUSABLES_CHARS` item length in `templates` folder when calling `wm.set_tpl_type` or `wm.set_tpl` method.

The value of `wm_base` must be greater than or equal to `2` and less than or equal to `36`, and cannot be greater than the value of `CONFUSABLES_CHARS` item length in the selected template.

`start_at` is used to specify the starting position of the inserted watermark. Default is `0`

`wm_loop` is used to identify whether the watermark needs to be inserted in the text in a loop or not. Default is `False`

### 2. Choose a watermark template

```py
from textwatermark.template_type import WMTemplateType

# Use set_tpl_type method to set a watermark template
wm.set_tpl_type(tpl_type=WMTemplateType.HOMOGRAPH_NUMBERS)

# Or

from textwatermark.templates import homograph_numbers

# Use set_tpl method to set a watermark template
wm.set_tpl(confusables_chars=homograph_numbers.CONFUSABLES_CHARS, 
           method=homograph_numbers.method, confusables_chars_key='')
```

There are two ways to choose and set a watermark template.

One is to use the `set_tpl_type(tpl_type, confusables_chars_key='')` method from the `TextWatermark` instance. There are two parameters for this method: `tpl_type` can be set to any attribute of `WMTemplateType`, see [template_type.WMTemplateType](/api/defines/#textwatermark.template_type.WMTemplateType) for more. `confusables_chars_key` only needs to be set when the template's method is `WMMethod.DECORATE_EACH_CHAR` or `WMMethod.APPEND_AS_BINARY`

The other way is to use the `set_tpl(confusables_chars, method, confusables_chars_key='')` method from the `TextWatermark` instance. The existence of this method is for anybody to custom template themselves. `set_tpl` method takes 3 parameters: `confusables_chars` is a list or dictionary like below:

```py
# confusables_chars example in list type
confusables_chars = ['\u0300', '\u0301', '\u0302', '\u0303', '\u0304']

# Or

# confusables_chars example in dictionary type
confusables_chars = {
    'black1': ['#000', '#111'],
    'black2': ['#000', '#222'],
}
```

The `method` parameter can be set to one of the attributes of `WMMethod`, see [defines.WMMethod](/api/defines/#textwatermark.defines.WMMethod) for more.

If the `method` is set to `WMMethod.FIND_AND_REPLACE` means the template will use to find some chars same as the key of `confusables_chars` and replace it with the value of `confusables_chars` in a sort. So  `confusables_chars` must be a dictionary type.

If the `method` is set to `WMMethod.INSERT_INTO_POSITION` means the watermark will be wholly inserted into a specified location of the text in a sort. The key is not necessary, so `confusables_chars` is a list type.

If the `method` is set to `WMMethod.DECORATE_EACH_CHAR` means different decorations will be around each char of the text. There are several decorations in each template, using keys to distinguish them. So `confusables_chars` is a dictionary type.

If the `method` is set to `WMMethod.APPEND_TO_CHAR` means different chars of the template will be appended to each char of the text in a sort. The key is not necessary, so `confusables_chars` is a list type.

If the `method` is set to `WMMethod.APPEND_AS_BINARY` means a char in the template will be appended to some chars of the text in binary mode. If the watermark char is behind a text char, the code is `1`, else `0`. There are a lot of chars that can append to another char in imperceptible differents. So a key is necessary, `confusables_chars` is a dictionary type.

When `confusables_chars` is a dictionary type, `confusables_chars_key` must be set to select an item from the `confusables_chars`.

### 3. Set the maximum value of the watermark string

```py
# Set the maximum value as string in the watermark
wm.set_wm_max(wm_max='999999999')
```

`set_wm_max` is used to set the longest (or largest) string among all the watermarks.

Since the input watermark string is variable in length, this will bring trouble to the retrieval of the watermark: It will be difficult to determine the boundary of the watermark or judge the loss of the watermark. Therefore, in this library, we will calculate and set the longest (or largest) length of the watermark string as default.

For example, if we budget the watermark string as an id between 1 to 999999999, we need to set the `wm_max` value to string `'999999999'`.

### 4. Set the text to be watermarked

```py
# Set the text want to be watermarked from a text file
wm.set_text_file(path=os.path.abspath('../tests/text/1.txt'))

# Or

# Set the text want to be watermarked from string
wm.set_text(text='text string')
```

There are two ways to set a value to `text` which wants to be watermarked. The first way is to set a text file path to the `set_text_file` method, the other way is to set a text string to the `set_text` method. Choose which you want.

### 5. Insert watermark string to text

```py
# Insert watermark into text
wm_text = wm.insert_watermark(wm_str='123456789')
print(wm_text)
```

The last step is to insert a watermark into the text by using the `insert_watermark` method.

## One more thing

Save watermark settings and retrieve the watermark

### Save watermark settings

```py
params = wm.export_params()
```

Since there may be different `TextWatermark` instances and configurations, or the template changes due to package upgrades, eventually the watermark content cannot be retrieved due to lost parameters. For this reason, this package provides a parameters export function `export_params`, you can store the exported JSON string in any position so that you can easily retrieve the watermark content in the text when necessary.

### Retrieve the watermark

```py
wm_out_str = TextWatermark.retrieve_watermark(wm_text=wm_text, params=params)

assert wm_out_str == wm_str
```

Once you export the parameters JSON string, you can use it to retrieve the watermark from the watermarked text by using `TextWatermark.retrieve_watermark` method anytime. This method is static, you do not need to init a `TextWatermark` instance first.
