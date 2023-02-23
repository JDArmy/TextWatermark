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

{%
  include-markdown "./support.html"
%}
