'''Main Class of TextWatermark'''
# pylint: disable=too-many-instance-attributes,too-many-arguments

import json
import os
import sys
from typing import Union

from textwatermark import __version__
from textwatermark.conversion import WMConversion
from textwatermark.defines import WMMethod, WMMode
from textwatermark.template import WMTemplate
from textwatermark.template_type import WMTemplateType


class TextWatermark:
    '''
    A class to insert watermark into plain text

    Example:
    --------
    ```py
    import os

    from textwatermark.defines import WMMode
    from textwatermark.main import TextWatermark
    from textwatermark.templates import homograph_numbers

    wm_mode = WMMode.REAL_NUMBER
    template = homograph_numbers
    wm_max = '9'*9
    confusables_chars_key = ''

    # init
    wm = TextWatermark(wm_mode)


    wm = set_tpl(template.CONFUSABLES_CHARS,
                 template.method,
                 confusables_chars_key)
    wm.set_wm_max(wm_max)
    wm.set_text_file(os.path.abspath(
        os.path.dirname(__file__)+'/../tests/text/1.txt'))

    # Insert watermark to text
    wm_str = '123456789'

    wm_text = wm.insert_watermark(wm_str)

    # Save the parameters to retrieve the watermark
    params = wm.export_params()

    # retrieve the watermark
    wm_out_str = TextWatermark.retrieve_watermark(wm_text, params)
    print(wm_text)

    assert wm_out_str == wm_str
    ```

    '''

    text: str
    '''Text to be watermarked.

        Set text by `self.set_text(text)` or `self.set_text_file(file_path)`
    '''

    wmc: WMConversion
    '''Instance of WMConverison'''
    wmt: WMTemplate
    '''Instance of WMTemplate'''

    wm_max: str
    '''Maximum watermark string.'''

    wm_fixed_len: int = 0
    '''The longest (or largest) watermark string. 
        When wm_flag_bit is true,
        The value of wm_max_len is 1 larger the actual value '''

    tpl_type: str = ''
    '''template type in WMTemplateType'''

    wm_flag_bit: bool = True
    '''If set a flag bit when insert watermark or not'''

    def __init__(self, wm_mode: WMMode, wm_base: int = 0, start_at: int = 0,
                 wm_loop: bool = False, wm_flag_bit: bool = True):
        '''Class TextWatermark init

        Args:
            wm_mode (WMMode): WMMode to be set
            wm_base (int): Watermark convert base.
            start_at (int, optional): index where the watermark will be inserted. Defaults to 0.
            wm_loop (bool, optional): If watermark will be repeated until it is inserted to end.
                Defaults to False.
            wm_flag_bit (bool, optional): If True, add a flag bit to watermark. Defaults to True.

        Raises:
            ValueError: if `base` is not in the range [2, 36]
        '''

        self.wm_mode = wm_mode
        '''Watermark encoding mode. Setting different watermark modes will effectively
        reduce the size of the watermark string.'''

        self.wm_base = wm_base
        '''watermark convert base must be between 2 and 36,
            and less or euqal than len(list({template}.CONFUSABLES_CHARS.values())[0])
        '''

        self.start_at = start_at
        '''index where the watermark will be inserted. Defaults to 0.'''
        self.wm_loop = wm_loop
        '''If watermark will be repeated until it is inserted to end.
                Defaults to False.'''
        self.wm_flag_bit = wm_flag_bit
        '''If True, add a flag bit to watermark. Defaults to True.'''

    def set_tpl(self, confusables_chars: Union[dict, list],
                method: WMMethod, confusables_chars_key: str = ''):
        '''Set template arguments and get instance of WMTemplate

        Args:
            confusables_chars (Union[dict, list]): Confusables chars
            method (WMMethod): Method of watermark
            confusables_chars_key (str): Confusables chars key

        '''

        self.wmt = WMTemplate(
            confusables_chars, self.wm_base, method, confusables_chars_key)

        if self.wm_base == 0:
            self.wm_base = self.wmt.wm_base

    def set_tpl_type(self, tpl_type: WMTemplateType, confusables_chars_key: str = ''):
        '''Set template type

        Args:
            tpl_type (WMTemplateType): Template type
            confusables_chars_key (str): Confusables chars key

        '''
        template = tpl_type.value

        self.wmt = WMTemplate(template.CONFUSABLES_CHARS, self.wm_base,
                              template.method, confusables_chars_key)

        if self.wm_base == 0:
            self.wm_base = self.wmt.wm_base

        self.tpl_type = tpl_type.name

    def set_wm_max(self, wm_max: str):
        '''Set the length of the longest (or largest) watermark string.

            Since the input watermark string is variable in length,
            this will bring trouble to the retrieval of the watermark:
            it will be difficult for us to determine the boundary of the watermark,
            or judge the loss of the watermark. Therefore, in this library,
            we will calculate and set the length of the longest (or largest)
            watermark string as the default length of the watermark string.

        Args:
            wm_max (str): The longest (or largest) watermark string.

        '''
        if not hasattr(self, 'wmt') or not self.wmt:
            raise ValueError(
                'Set up template with set_tpl or set_tpl_type first please.')

        self.wmc = WMConversion(self.wm_mode, self.wmt.wm_base)
        self.wm_max = wm_max

        wm_max_len = self.wmc.calc_max_wm_length(wm_max)
        if self.wm_flag_bit:
            self.wm_fixed_len = wm_max_len + 1
        else:
            self.wm_fixed_len = wm_max_len

    def set_text(self, text: str):
        '''Set text string to watermark

        Args:
            text (str): text to be watermarked
        '''
        self.text = text

    def set_text_file(self, path: str):
        '''Set text string from read file.

        Args:
            path (str): Text file path

        Raises:
            ValueError: If file not found
            OSError: If file cannnot by read
        '''
        path = os.path.abspath(path)

        if not os.path.exists(path):
            raise ValueError(f'ERROR: file {path} does not exist')

        try:
            with open(path, 'r', encoding='utf-8') as file:
                self.set_text(file.read())
        except OSError as err:
            print(f'ERROR: cannot read file {path}, err is {err.strerror}')
            sys.exit()

    def insert_watermark(self,  wm_str: str):
        '''Insert watermark to text

        Args:
            wm_str (str): Watermark string

        Returns:
            (str): Watermarked text

        Raises:
            ValueError: If watermark string is larger than wm_max
            ValueError: If there is not enough space to insert a watermark
        '''
        if wm_str > self.wm_max:
            raise ValueError(
                f'ERROR: watermark:{wm_str} if larger than wm_max: {self.wm_max}')

        wm_final = self.wmc.wm_convert_to_arbitrary_base(wm_str)
        wm_final = wm_final.zfill(self.wm_fixed_len-1)

        if self.wm_flag_bit:
            wm_final = '1' + wm_final

        if len(wm_final) > self.wm_fixed_len:
            raise ValueError(
                f'ERROR: watermark {wm_str} (convert to: {wm_final}) \
                    is too long: {len(wm_final)}, max length is {self.wm_fixed_len}')
        #
        wm_text = self.wmt.insert_watermark(
            text=self.text,
            wm_final=wm_final,
            start_at=self.start_at,
            loop=self.wm_loop)
        return wm_text

    def save_to_file(self, wm_text: str, path: str):
        '''Save watermarked text string to a file

        Args:
            wm_text (str): text to be watermarked
            path (str): save to text file path

        Raises:
            OSError: If file cannnot be created

        '''
        path = os.path.abspath(path)

        try:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(wm_text)
        except OSError as err:
            print(f'ERROR: cannot write to file {path}, err is {err.strerror}')
            sys.exit()

    def export_params(self):
        '''Export watermark params to json string

        Returns:
            (str): Exported JSON string

        '''
        if self.tpl_type != '' and self.wmt.confusables_chars \
                == WMTemplateType[self.tpl_type].value.CONFUSABLES_CHARS:
            confusables_chars = []
        else:
            confusables_chars = self.wmt.confusables_chars

        params = {
            'tpl_type': self.tpl_type,
            'confusables_chars': confusables_chars,
            'confusables_chars_key': self.wmt.confusables_chars_key,
            'wm_base': self.wmt.wm_base,
            'method': self.wmt.method.value,
            'wm_mode': self.wm_mode,
            'wm_len': self.wm_fixed_len,
            'wm_flag_bit': self.wm_flag_bit,
            'wm_loop': self.wm_loop,
            'start_at': self.start_at,
            'version': __version__,
        }
        # print(params)

        return json.dumps(params, ensure_ascii=False)

    @ staticmethod
    def retrieve_watermark_from_bin(wm_bin: str, params: json,
                                    force_check_version: bool = False):
        '''
        Retrieve watermark from binary string.

        Args:
            wm_bin (str): watermark binary string
            params (json): params containing the watermark options

        Returns:
            (str): watermark string.

        '''
        params = json.loads(params)
        wm_len = params['wm_len']
        wmc = WMConversion(params['wm_mode'], params['wm_base'])

        ver = params['version']
        if ver != __version__ and force_check_version is False:
            raise ValueError(f'Not the same version, params version is {ver},'
                             f' library version is {__version__}.'
                             'If you confirm that you want to use a different version to'
                             ' retrieve the watermark, please set force_check_version to True')

        if len(wm_bin) < wm_len:
            raise ValueError(f'Watermark length is short than {wm_len}')

        if params['wm_flag_bit'] is True:
            wm_temp = wm_bin[1:wm_len]
        else:
            wm_temp = wm_bin[0:wm_len]

        wm_temp = wm_temp.lstrip('0')

        wm_out_str = wmc.wm_restore_from_arbitrary_base(wm_temp)
        return wm_out_str

    @ staticmethod
    def retrieve_watermark(wm_text: str, params: json,
                           force_check_version: bool = False):
        '''Retrieve watermark from watermarked text
        Note: This is a static method
            You can call this method by `TextWatermark.retrieve_watermark`

        Warning: Retrieve watermark method is not a silver bullet
            In many cases, the watermarked text may be transferred several times,
            which may cause the watermark to change or disappear. At this time,
            the watermark information cannot be retrieved through this function.
            In the case of screen capture and screen capture, manual judgment is
            required to find out the watermark information.

        Args:
            wm_text (str): watermarked text
            params (json): params containing the watermark options

        Returns:
            (str): Watermark string.

        '''

        params = json.loads(params)
        # print(params)
        wm_len = params['wm_len']
        ver = params['version']
        if len(wm_text) < wm_len:
            raise ValueError(f'Watermark length is too short: '
                             f'len of wm_text is {len(wm_text)}, wm_len is {wm_len}')

        if ver != __version__ and force_check_version is False:
            raise ValueError(f'Not the same version, params version is {ver},'
                             f' library version is {__version__}.'
                             'If you confirm that you want to use a different version to'
                             ' retrieve the watermark, please set force_check_version to True')

        wmc = WMConversion(params['wm_mode'], params['wm_base'])

        if not params['confusables_chars']:
            tpl_type = params['tpl_type']
            if tpl_type not in WMTemplateType.__members__:
                raise ValueError(f'Invalid WMTemplateType: {tpl_type}')
            params['confusables_chars'] = WMTemplateType[tpl_type].value.CONFUSABLES_CHARS

        wmt = WMTemplate(
            params['confusables_chars'],
            params['wm_base'],
            params['method'],
            params['confusables_chars_key'])

        wm_out = wmt.retrieve_watermark(
            wm_text=wm_text,
            wm_base=wmt.wm_base,
            wm_len=wm_len,
            start_at=params['start_at'])

        if params['wm_flag_bit'] is True:
            wm_temp = wm_out[1:wm_len]
        else:
            wm_temp = wm_out[0:wm_len]

        wm_temp = wm_temp.lstrip('0')
        wm_out_str = wmc.wm_restore_from_arbitrary_base(wm_temp)
        return wm_out_str
