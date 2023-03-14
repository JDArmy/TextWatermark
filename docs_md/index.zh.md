# 首页

## 要求

Tested on Python `>= 3.10`

## 安装

### 使用Pip

`$ pip install textwatermark`

### 从源代码

```bash
git clone https://github.com/JDArmy/TextWatermark.git

cd TextWatermark

pip install .

# or in editable mode
pip install --editable .
```

## 使用

### 命令行

#### 插入水印到文本

```console
$ textwatermark -v insert -f './tests/text/number.txt' -m ALPHA_NUMERICAL -t HOMOGRAPH_NUMBERS -x 999 -w 123

Ӏ2𝟑𝟒𝟓Ⳓ𝟟890
```

#### 保存水印参数

```console
$ textwatermark -v insert -f './tests/text/number.txt' -m ALPHA_NUMERICAL -t HOMOGRAPH_NUMBERS -x 999 -w 123 -e

{"tpl_type": "HOMOGRAPH_NUMBERS", "confusables_chars": [], "confusables_chars_key": "", "wm_base": 7, "method": "FIND_AND_REPLACE", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 7, "wm_flag_bit": true, "wm_loop": false, "wm_max": "999", "start_at": 0, "version": "0.3.0"}
```

#### 从文本提取水印

```console
$ textwatermark -v retrieve -f out.txt -p '{"tpl_type": "HOMOGRAPH_NUMBERS", "confusables_chars": [], "confusables_chars_key": "", "wm_base": 7, "method": "FIND_AND_REPLACE", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 7, "wm_flag_bit": true, "wm_loop": false, "wm_max": "999", "start_at": 0, "version": "0.3.0"}'

The retrieved watermark is: 123
```

### 代码

```py
{%
  include-markdown "../examples/sample.py"
%}
```

### 更多

参见：[用法](https://textwatermark.jd.army/usage/)

## 水印模板支持情况

{%
  include-markdown "./support.html"
%}
