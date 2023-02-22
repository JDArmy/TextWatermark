# 用法

## 整个示例代码

```py
{%
  include-markdown "../examples/sample.py"
%}
```

将水印插入文本有 5 个步骤。

### 1.初始化TextWatermark实例

```py
from textwatermark.defines import WMMode
from textwatermark.main import TextWatermark

# 获取 TextWatermark 类的实例
wm_mode = WMMode.REAL_NUMBER
wm = TextWatermark(wm_mode=wm_mode)
```

TextWatermark 的初始化有 4 个参数：

`__init__(wm_mode, wm_base=0, start_at=0, wm_loop=False)`

`wm_mode`  是必需的。

`wm_mode` 可以设置为 `WMMode` 的任何属性，请参阅 [defines.WMMode](/api/defines/#textwatermark.defines.WMMode) 了解更多信息。
为什么`wm_mode`需要设置一个值？

用于缩小水印字符串的大小。

`wm_base`的存在是为了指定最终水印字符串的基数。

如果您不知道什么意思，则没有必要设置此值。 `__init__`中的`wm_base`默认值为0，
然后在调用`wm.set_tpl_type` 或`wm.set_tpl` 方法时将设置为`templates` 文件夹中的`{template}.CONFUSABLES_CHARS` 项目长度。

`wm_base`的值必须大于或等于`2`且小于或等于`36`，并且不能大于所选模板中的`CONFUSABLES_CHARS`项长度的值。

`start_at`用于指定插入水印的起始位置。 默认为“0”

`wm_loop` 用于标识水印是否需要循环插入到文本中。 默认为`False`

### 2.选择水印模板

```py
from textwatermark.template_type import WMTemplateType

# 使用set_tpl_type方法设置水印模板
wm.set_tpl_type(tpl_type=WMTemplateType.HOMOGRAPH_NUMBERS)

# 或者

from textwatermark.templates import homograph_numbers

# 使用set_tpl方法设置水印模板
wm.set_tpl(confusables_chars=homograph_numbers.CONFUSABLES_CHARS, 
           method=homograph_numbers.method, confusables_chars_key='')
```

有两种方法可以选择和设置水印模板。

一种是使用 `TextWatermark` 实例中的 `set_tpl_type(tpl_type, confusables_chars_key='')` 方法。 此方法有两个参数： `tpl_type` 可以设置为 `WMTemplateType` 的任何属性，请参阅 [template_type.WMTemplateType](/api/defines/#textwatermark.template_type.WMTemplateType) 了解更多信息。 `confusables_chars_key` 只有当模板的方法是 `WMMethod.DECORATE_EACH_CHAR` 或 `WMMethod.APPEND_AS_BINARY` 时才需要设置

另一种方法是使用 `TextWatermark` 实例中的 `set_tpl(confusables_chars, method, confusables_chars_key='')` 方法。 这种方法的存在是为了任何人都可以自己定制模板。 `set_tpl` 方法有 3 个参数： `confusables_chars` 是一个列表或字典，如下所示：

```py
# confusables_chars 列表类型示例
confusables_chars = ['\u0300', '\u0301', '\u0302', '\u0303', '\u0304']

# 或者

# 字典类型的 confusables_chars 示例
confusables_chars = {
    'black1': ['#000', '#111'],
    'black2': ['#000', '#222'],
}
```

`method` 参数可以设置为 `WMMethod` 的属性之一，有关更多信息，请参阅 [defines.WMMethod](/api/defines/#textwatermark.defines.WMMethod)。

如果 `method` 设置为 `WMMethod.FIND_AND_REPLACE` 意味着模板将使用查找一些与 `confusables_chars` 的键相同的字符，并将其替换为排序中的 `confusables_chars` 的值。 所以 `confusables_chars` 必须是字典类型。

如果 `method` 设置为 `WMMethod.INSERT_INTO_POSITION` 意味着水印将以某种方式全部插入到文本的指定位置。 key 不是必需的，所以 `confusables_chars` 是一个列表类型。

如果 `method` 设置为 `WMMethod.DECORATE_EACH_CHAR` 意味着不同的装饰将围绕文本的每个字符。 每个模板中有几个装饰，使用键来区分它们。 所以 `confusables_chars` 是一个字典类型。

如果 `method` 设置为 `WMMethod.APPEND_TO_CHAR` 意味着模板的不同字符将按排序附加到文本的每个字符。 key 不是必需的，所以 `confusables_chars` 是一个列表类型。

如果 `method` 设置为 `WMMethod.APPEND_AS_BINARY` 意味着模板中的一个字符将以二进制模式附加到文本的某些字符。 如果水印字符在文本字符后面，则代码为 `1`，否则为 `0`。有很多字符可以以难以察觉的差异附加到另一个字符。 所以一个键是必要的，`confusables_chars`是一个字典类型。

当 `confusables_chars` 为字典类型时，必须设置 `confusables_chars_key` 以从 `confusables_chars` 中选择一项。

### 3.设置水印字符串的最大值

```py
# 设置水印字符串中的最大值
wm.set_wm_max(wm_max='999999999')
```

`set_wm_max` 用于设置所有水印中最长（或最大）的字符串。

由于输入的水印字符串长度是可变的，这会给水印的检索带来麻烦：难以确定水印的边界或判断水印的丢失。 因此，在这个库中，我们将计算并设置水印字符串的最长（或最大）长度为默认值。

例如，如果我们将水印字符串预算为 `1` 到 `999999999` 之间的 id，我们需要将`wm_max`值设置为字符串`999999999`。

### 4.设置要加水印的文字

```py
# 从文本文件中设置要加水印的文本
wm.set_text_file(path=os.path.abspath('../tests/text/1.txt'))

# 或者

# 从字符串中设置要加水印的文本
wm.set_text(text='text string')
```

有两种方法可以为要加水印的“文本”设置值。 第一种方式是将文本文件路径设置为 `set_text_file` 方法，另一种方式是将文本字符串设置为 `set_text` 方法。 选择你想要的。

### 5.向文本插入水印字符串

```py
# 在文本中插入水印
wm_text = wm.insert_watermark(wm_str='123456789')
print(wm_text)
```

最后一步是使用 insert_watermark 方法在文本中插入水印。

## 还有一件事

保存水印设置并找回水印

### 保存水印设置

```py
params = wm.export_params()
```

由于可能存在不同的`TextWatermark`实例和配置，或者由于包升级导致模板发生变化，最终导致水印内容因丢失参数而无法找回。 为此，本包提供了一个参数导出函数`export_params`，您可以将导出的JSON字符串存储在任意位置，以便您在需要时方便地检索文本中的水印内容。

### 找回水印

```py
wm_out_str = TextWatermark.retrieve_watermark(wm_text=wm_text, params=params)

assert wm_out_str == wm_str
```

导出参数 JSON 字符串后，您可以随时使用`TextWatermark.retrieve_watermark`方法从带水印的文本中检索水印。 这个方法是静态的，你不需要先初始化一个 `TextWatermark` 实例。
