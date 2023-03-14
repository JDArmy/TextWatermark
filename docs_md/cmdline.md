# Run textwatermark from the CMD line

## textwatermark --help

```console
$ textwatermark --help

Usage: textwatermark [OPTIONS] COMMAND [ARGS]...

  Main commands

Options:
  -V, --version  Show version and exit.
  -v, --verbose  Show more info.
  --debug        Enable debug.
  --help         Show this message and exit.

Commands:
  insert    Insert watermark to text
  retrieve  Retrieve watermark from watermarked text
```

## Insert Watermark To Text

### textwatermark insert --help

```console
$ textwatermark insert --help

Usage: textwatermark insert [OPTIONS]

  Insert watermark to text

  Examples:

  Insert watermark to text file:

  `textwatermark -v insert -f './tests/text/1.txt' -m ALPHA_NUMERICAL -t
  HOMOGRAPH_NUMBERS -x 999999999 -w 123456789 `

  Export params to out_file:

  `textwatermark -v insert -m ALPHA_NUMERICAL -t HOMOGRAPH_NUMBERS -x
  999999999 -w 123456789 -e -o 'out.txt'`

Options:
  -f, --text-file TEXT           Text file waiting for watermarking
  -o, --out-file TEXT            Watermarked file to be saved
  -m, --wm-mode TEXT             Watermark mode value in defines.WMMode
                                 [required]
  -t, --template-type TEXT       Template type in templates  [required]
  -x, --wm-max TEXT              Max value or string of the watermark
                                 [required]
  -w, --wm-str TEXT              Watermark string  [required]
  -b, --wm-base INTEGER          Base conversion of watermark string
  -k, --template-chars-key TEXT  Key of template confusables chars
  -l, --wm-loop                  If True then inserts watermark in a loop,
                                 Defaults to False
  -i, --start-at INTEGER         Index of where the watermark will be
                                 inserted. Defaults to 0.
  -e, --export-params            If True then export watermark params
  -n, --no-flag-bit              If True then do not add a flag bit to
                                 watermark
  --help                         Show this message and exit.
```

### Insert Watermark Example

#### Print Watermarked Text To The Console

```console
$ textwatermark -v insert -f './tests/text/number.txt' -m ALPHA_NUMERICAL -t HOMOGRAPH_NUMBERS -x 999 -w 123

Ӏ2𝟑𝟒𝟓Ⳓ𝟟890
```

#### Save Watermarked Text To File

```console
$ textwatermark -v insert -f './tests/text/number.txt' -m ALPHA_NUMERICAL -t HOMOGRAPH_NUMBERS -x 999 -w 123 -o out.txt

Save watermarked text to output file: /Projects/JDArmy/TextWatermark/textwatermark/out.txt
Orgin text length is: 10
Watermarked text length is: 10
```

### Export Parameters Example

#### Export Parameters To The Console

```console
$ textwatermark -v insert -f './tests/text/number.txt' -m ALPHA_NUMERICAL -t HOMOGRAPH_NUMBERS -x 999 -w 123 -e

{"tpl_type": "HOMOGRAPH_NUMBERS", "confusables_chars": [], "confusables_chars_key": "", "wm_base": 7, "method": "FIND_AND_REPLACE", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 7, "wm_flag_bit": true, "wm_loop": false, "wm_max": "999", "start_at": 0, "version": "0.3.0"}
```

#### Export Parameters To File

```console
$ textwatermark -v insert -f './tests/text/number.txt' -m ALPHA_NUMERICAL -t HOMOGRAPH_NUMBERS -x 999 -w 123 -e -o out.txt

Export params save to output file: /Projects/JDArmy/TextWatermark/textwatermark/out.txt
```

## Retrieve Watermark From Text

### textwatermark retrieve --help

```console
$ textwatermark retrieve --help

Usage: textwatermark retrieve [OPTIONS]

  Retrieve watermark from watermarked text

  Examples:

  `textwatermark retrieve -f ./out.txt -p '{the param json string export by
  command:insert and option:--export-params}'`

Options:
  -f, --wm-text-file TEXT    Text file already be watermarked
  -b, --wm-binary TEXT       Watermark string in binary
  -p, --params-json TEXT     Param json when watermarking text  [required]
  -F, --dont-check-version   Don't check versions between params and
                             library
  --help                     Show this message and exit.
```

### Retrieve Watermark From Text Example

```console
$ textwatermark -v retrieve -f out.txt -p '{"tpl_type": "HOMOGRAPH_NUMBERS", "confusables_chars": [], "confusables_chars_key": "", "wm_base": 7, "method": "FIND_AND_REPLACE", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 7, "wm_flag_bit": true, "wm_loop": false, "wm_max": "999", "start_at": 0, "version": "0.3.0"}'

The retrieved watermark is: 123
```

### Retrieve Watermark From Binary String

Most of the time, such as taking screenshots or photographs, we can not retrieve watermarks automatically.
We can only manually compare text features to extract watermarks.
Watermarks will be expressed in binary to any encoded base (0-9, A-Z) of characters.

Then we can use `--wm-binary` parameter to retrieve the watermark.

```console
$ textwatermark -v retrieve -b 10010000011000100000101000110000111 -p '{"tpl_type": "FONT_SIZE", "confusables_chars": [], "confusables_chars_key": "110", "wm_base": 2, "method": "DECORATE_EACH_CHAR", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 35, "wm_loop": false,"wm_flag_bit": true, "start_at": 0, "version": "0.3.0"}' -F

The retrieved watermark is: 123456
```
