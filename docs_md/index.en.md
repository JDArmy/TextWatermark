# Home

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

```session
$ textwatermark -v insert -f './tests/text/number.txt' -m ALPHA_NUMERICAL -t HOMOGRAPH_NUMBERS -x 999 -w 123

Ӏ2𝟑𝟒𝟓Ⳓ𝟟890
```

#### Retrieve the watermark from the text

```session
$ textwatermark -v retrieve -f out.txt -p '{"tpl_type": "HOMOGRAPH_NUMBERS", "confusables_chars": [], "confusables_chars_key": "", "wm_base": 7, "method": 1, "wm_mode": 5, "wm_len": 7, "wm_loop": false, "start_at": 0, "version": "0.1.0"}'

The retrieved watermark is: 123
```

### Coding

```py
{%
  include-markdown "../examples/sample.py"
%}
```

### More

See: [Usage](https://textwatermark.jd.army/usage/)

## TextWatermark Templates Support and Compatibility

<table border="1" style="font-size:50%">
  <tr>
    <th rowspan="2" style="text-align:center">Template Name</th>
    <th rowspan="2" style="text-align:center">WMTemplateType</th>
    <th colspan="3" style="text-align:center">Applicable scene</th>
    <th colspan="4" style="text-align:center">Text featureless</th>
    <th colspan="4" style="text-align:center">Support characters</th>
    <th rowspan="2" style="text-align:center">Plain Text</th>
    <th rowspan="2" style="text-align:center">Concealment</th>
  </tr>
  <tr>
    <td>Paste</td>
    <td>Screenshot</td>
    <td>photograph</td>
    <td>Format</td>
    <td>Style</td>
    <td>Shape</td>
    <td>Mean</td>
    <td>Number</td>
    <td>Letter</td>
    <td>Chinese</td>
    <td>Special</td>
  </tr>
  <tr>
    <td>不可见字符</td>
    <td><a href="/templates/#invisible_chars">INVISIBLE_CHARS</a></td>
    <td>✓</td>
    <td>×</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>High</td>
  </tr>
  <tr>
    <td>空白字符</td>
    <td><a href="/templates/#whitespace_chars">WHITESPACE_CHARS</a></td>
    <td>✓</td>
    <td>×</td>
    <td>×</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>Medium</td>
  </tr>
  <tr>
    <td>空格字符</td>
    <td><a href="/templates/#space_chars">SPACE_CHARS</a></td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>Medium</td>
  </tr>
  <tr>
    <td>组合字符</td>
    <td><a href="/templates/#combining_chars">COMBINING_CHARS</a></td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>Medium</td>
  </tr>
  <tr>
    <td>同形异义-数字</td>
    <td><a href="/templates/#homograph_numbers">HOMOGRAPH_NUMBERS</a></td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>×</td>
    <td>×</td>
    <td>✓</td>
    <td>Low</td>
  </tr>
  <tr>
    <td>同形异义-字母</td>
    <td><a href="/templates/#homograph_letters">HOMOGRAPH_LETTERS</a></td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>×</td>
    <td>×</td>
    <td>✓</td>
    <td>Low</td>
  </tr>
  <tr>
    <td>同形异义-中文</td>
    <td><a href="/templates/#homograph_chinese">HOMOGRAPH_CHINESE</a></td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>×</td>
    <td>×</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>Low</td>
  </tr>
  <tr>
    <td>同形异义-标点</td>
    <td><a href="/templates/#homograph_punctuations">HOMOGRAPH_PUNCTUATIONS</a></td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>×</td>
    <td>×</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>Medium</td>
  </tr>
  <tr>
    <td>字体颜色</td>
    <td><a href="/templates/#font_color">FONT_COLOR</a></td>
    <td>⍻</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>Medium</td>
  </tr>
  <tr>
    <td>字体大小</td>
    <td><a href="/templates/#font_size">FONT_SIZE</a></td>
    <td>⍻</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>Low</td>
  </tr>
  <tr>
    <td>字体粗细</td>
    <td><a href="/templates/#font_weight">FONT_WEIGHT</a></td>
    <td>⍻</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>Low</td>
  </tr>
  <tr>
    <td>字体浮动</td>
    <td><a href="/templates/#font_float">FONT_FLOAT</a></td>
    <td>⍻</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>Low</td>
  </tr>
  <tr>
    <td>自定义样式</td>
    <td><a href="/templates/#font_style">FONT_STYLE</a></td>
    <td>⍻</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>Low</td>
  </tr>
  <tr>
    <td>空HTML实体</td>
    <td><a href="/templates/#html_empty_tags">HTML_EMPTY_TAGS</a></td>
    <td>⍻</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>Low</td>
  </tr>
  <tr>
    <td>二进制表示</td>
    <td><a href="/templates/#binary_representation">BINARY_REPRESENTATION</a></td>
    <td>✓</td>
    <td>⍻</td>
    <td>⍻</td>
    <td>⍻</td>
    <td>✓</td>
    <td>⍻</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>High</td>
  </tr>
  <!--
  <tr>
    <td>同义替换-汉字</td>
    <td>synonym-chinese</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>×</td>
    <td>×</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>High</td>
  </tr>
  <tr>
    <td>同义替换-数字</td>
    <td>synonym-numbers</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>×</td>
    <td>×</td>
    <td>×</td>
    <td>✓</td>
    <td>Medium</td>
  </tr>
  <tr>
    <td>同义替换-单词</td>
    <td>synonym-words</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>×</td>
    <td>✓</td>
    <td>×</td>
    <td>×</td>
    <td>✓</td>
    <td>High</td>
  </tr>
  <tr>
    <td>错别字-汉字</td>
    <td>wrong-chinese</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>错别字-单词</td>
    <td>wrong-words</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>-->
</table>
