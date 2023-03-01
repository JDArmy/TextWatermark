# Changelog

## 0.1.7

- Change Python restricted dependencies of `mkdocs-include-markdown-plugin` in `pyproject.toml`, so  `python = "^3.8,<3.12"` in `[tool.poetry.dependencies]` can be change to `python = "^3.8"`

## 0.1.6

- Bug fix: `TextWatermark.init_from_params` going wrong when `set_tpl` mode
- Bug fix: Error when checking if `wm_str` larger than `wm_max` in method `TextWatermark.insert_watermark`
- Bug fix: Wrong watermarked when setting `wm_flag_bit` to `False` in method `TextWatermark.insert_watermark`

## 0.1.5

- add `init_from_params` static method to `TextWatermark`, `TextWatermark` can be init from exported params.

## 0.1.4

- fixes dependencies

## 0.1.3

- add `--no-flag-bit` command to cmdline, and wm_flag_bit parameter to `__init__` method of `TextWatermark` class.

## 0.1.2

- add retrieve watermark from binary static method `retrieve_watermark_from_bin` to TextWatermark class and the cmd line.
- add examples to docs

## 0.1.0

init of `TextWatermark`
