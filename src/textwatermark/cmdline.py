"""Command line interface"""
# pylint: disable=too-many-arguments,invalid-name,too-many-locals

import os
import re

import click
from click import Context

from .config import settings
from .defines import WMMethod, WMMode
from .main import TextWatermark
from .template_type import WMTemplateType
from .version import __version__


@click.group(invoke_without_command=True)
@click.pass_context
@click.option("-V", "--version", is_flag=True, help="Show version and exit.")
@click.option("-v", "--verbose", is_flag=True, help="Show more info.")
# If it's true, it will override `settings.VERBOSE`
@click.option("--debug", is_flag=True, help="Enable debug.")
# If it's true, it will override `settings.DEBUG`
def main(ctx: Context, version: str, verbose: bool, debug: bool):
    """Main commands"""
    if version:
        click.echo(__version__)
    elif ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
    else:
        if verbose:
            settings.set("VERBOSE", True)
        if debug:
            settings.set("DEBUG", True)


@main.command()
@click.option(
    "-f",
    "--text-file",
    type=str,
    required=False,
    help="Text file waiting for watermarking",
)
@click.option(
    "-o", "--out-file", type=str, required=False, help="Watermarked file to be saved"
)
@click.option(
    "-m",
    "--wm-mode",
    type=str,
    required=True,
    help="Watermark mode value in defines.WMMode",
)
@click.option(
    "-t", "--template-type", type=str, required=True, help="Template type in templates"
)
@click.option(
    "-x",
    "--wm-max",
    type=str,
    required=True,
    help="Max value or string of the watermark",
)
@click.option("-w", "--wm-str", type=str, required=True, help="Watermark string")
@click.option(
    "-b",
    "--wm-base",
    type=int,
    default=0,
    required=False,
    help="Base conversion of watermark string",
)
@click.option(
    "-k",
    "--template-chars-key",
    type=str,
    default="",
    required=False,
    help="Key of template confusables chars",
)
@click.option(
    "-l",
    "--wm-loop",
    is_flag=True,
    help="If True then inserts watermark in a loop, Defaults to False",
)
@click.option(
    "-i",
    "--start-at",
    type=int,
    default=0,
    required=False,
    help="Index of where the watermark will be inserted. Defaults to 0.",
)
@click.option(
    "-e", "--export-params", is_flag=True, help="If True then export watermark params"
)
@click.option(
    "-n",
    "--no-flag-bit",
    is_flag=True,
    help="If True then do not add a flag bit to watermark",
)
def insert(
    text_file: str,
    out_file: str,
    wm_mode: str,
    template_type: str,
    wm_max: str,
    wm_str: str,
    wm_base: int,
    template_chars_key: str,
    wm_loop: bool,
    start_at: int,
    export_params: bool,
    no_flag_bit: bool,
):
    """Insert watermark to text

    Examples:

    Insert watermark to text file:

    `textwatermark -v insert -f './tests/text/1.txt' -m ALPHA_NUMERICAL
    -t HOMOGRAPH_NUMBERS -x 999999999 -w 123456789 `

    Export params to out_file:

    `textwatermark -v insert -m ALPHA_NUMERICAL -t HOMOGRAPH_NUMBERS
    -x 999999999 -w 123456789 -e -o 'out.txt'`
    """
    verbose = settings.VERBOSE

    new_template_type = WMTemplateType[template_type]
    if (
        new_template_type.value.method
        in [WMMethod.DECORATE_EACH_CHAR, WMMethod.APPEND_AS_BINARY]
        and template_chars_key == ""
    ):
        raise ValueError("template_chars_key is required")

    if re.fullmatch(r"^\\u[0-9a-fA-F]{4}$", template_chars_key) is not None:
        template_chars_key = chr(int(template_chars_key[2:], 16))

    # # init
    wm = TextWatermark(
        WMMode[wm_mode], wm_base, start_at, wm_loop, wm_flag_bit=not no_flag_bit
    )
    wm.set_tpl_type(new_template_type, template_chars_key)
    wm.set_wm_max(wm_max=wm_max)

    if export_params:
        # wm.tpl_type = ''
        if out_file:
            out_file_path = os.path.abspath(out_file)
            with open(out_file_path, "w", encoding="utf-8") as f:
                f.write(wm.export_params())
            if verbose:
                print("Export params save to output file: " + out_file_path)
            else:
                print("ok")
        else:
            print(wm.export_params())
        return

    text_file = os.path.abspath(text_file)
    wm.set_text_file(text_file)
    wm_text = wm.insert_watermark(wm_str)
    if out_file:
        out_file_path = os.path.abspath(out_file)
        wm.save_to_file(wm_text, out_file_path)
        if verbose:
            print("Save watermarked text to output file: " + out_file_path)
            print("Orgin text length is: " + str(len(wm.text)))
            print("Watermarked text length is: " + str(len(wm_text)))
        else:
            print("ok")
    else:
        print(wm_text)


@main.command()
@click.option(
    "-f",
    "--wm-text-file",
    type=str,
    required=False,
    help="Text file already be watermarked",
)
@click.option(
    "-b", "--wm-binary", type=str, required=False, help="Watermark string in binary"
)
@click.option(
    "-p",
    "--params-json",
    type=str,
    required=True,
    help="Param json when watermarking text",
)
@click.option(
    "-F",
    "--dont-check-version",
    is_flag=True,
    help="Don't check versions between params and library",
)
def retrieve(
    wm_text_file: str, wm_binary: str, params_json: str, dont_check_version: bool
):
    """Retrieve watermark from watermarked text

    Examples:

    `textwatermark retrieve -f ./out.txt -p '{the param json string export by
    command:insert and option:--export-params}'`
    """
    verbose = settings.VERBOSE

    if not wm_text_file and not wm_binary:
        raise ValueError("No watermarked text file or watermark binary string set")

    if wm_binary:
        wm_out_str = TextWatermark.retrieve_watermark_from_bin(
            wm_binary, params_json, dont_check_version
        )

    else:
        wm_text_file = os.path.abspath(wm_text_file)
        if not os.path.exists(wm_text_file):
            raise ValueError(f"ERROR: file {wm_text_file} does not exist")
        try:
            with open(wm_text_file, "r", encoding="utf-8") as f:
                wm_text = f.read()
        except OSError as err:
            print(f"ERROR: cannot read file {wm_text_file}, err is {err.strerror}")
            raise
        wm_out_str = TextWatermark.retrieve_watermark(
            wm_text, params_json, dont_check_version
        )

    if verbose:
        print(f"The retrieved watermark is: {wm_out_str}")
    else:
        print(wm_out_str)
