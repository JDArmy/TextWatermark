'''Class of Conversion'''
# pylint: disable=too-many-instance-attributes

import re

import numpy as np
from bitstring import BitArray

from textwatermark.defines import WMMode


class WMConversion:
    '''
    A class to insert watermark into plain text

    Example:
    --------
    ```py
    wm_base = 0
    wm_str = '123'
    wmc = WMConversion(WMMode.REAL_NUMBER, wm_base)
    wm_final = wmc.wm_convert_to_arbitrary_base(wm_str)
    wm_out_str = wmc.wm_restore_from_arbitrary_base(wm_final)
    assert wm_str == wm_out_str
    print(wmc.calc_max_wm_length(wm_str+wm_str), wm_final, wm_str, wm_out_str)
    ```
    '''

    def __init__(self, wm_mode: WMMode, wm_base: int):
        '''Class TextWatermark init

        If debug is set to True, the watermark processing will be printed.

        Args:
            wm_mode (WMMode): Set watermark encoding mode. 
            wm_base (int): Watermark's conversion base

        Raises:
            ValueError: If `base` is not in the range [2, 36]
        '''

        self.wm_mode = wm_mode
        '''Setting different watermark modes will effectively reduce the size of 
        the watermark string.'''

        if wm_base < 2 or wm_base > 36:
            raise ValueError(
                f'watermark convert base must be between 2 and 36: {wm_base}')

        self.wm_base = wm_base
        '''watermark conversion base must be between 2 and 36'''

    def calc_max_wm_length(self, wm_max: str):
        '''Calculate the watermark length in target base

        This method usually be used with `wm.set_fixed_wm_length` method.
        This method will calculate the length of the longest (or largest) 
        watermark string in the input string. Then call `wm.set_fixed_wm_length` 
        method set the return value to wm.wm_fixed_len.

        **It should be noted that:** *the length calculated by this method will 
        add 1 to the original length. The purpose is to quickly locate the 
        starting position of the watermark string when filling the watermark 
        string with 0, so as to ensure that the correct value is obtained and 
        restored. *

        Args:
            wm_max (str): Maximum watermark string in target base

        Returns:
            (int): Returns the length of the watermark string in the specified base
        '''

        wm_final = self.wm_convert_to_arbitrary_base(wm_max)
        return len(wm_final)

    def wm_convert_to_arbitrary_base(self, wm_str: str):
        '''Convert watermark to arbitrary base string

        Args:
            wm_str (str): Watermark string

        Returns:
            (str): Returns watermark string in arbitrary base

        Raises:
            ValueError: if `wm_str` type is not match `wm_mode`
            ValueError: if invalid watermark `wm_mode`
            ValueError: if invalid watermark `wm_base`

        '''

        if not isinstance(wm_str, str):
            wm_str = str(wm_str)

        wm_bin = ''
        match self.wm_mode:
            case WMMode.REAL_NUMBER:
                if not re.fullmatch(r'[0-9]+', wm_str):
                    raise ValueError(
                        f'ERROR: invalid watermark wm_mode: {wm_str} is not numerical ')
                wm_bin = str(bin(int(wm_str)))[2:]
            case WMMode.LETTERS_LOWER_CASE:
                if not re.fullmatch(r'[a-z]+', wm_str):
                    raise ValueError(
                        f'ERROR: invalid watermark wm_mode: {wm_str} are not lower case letters ')
                wm_bin = ''.join(
                    format(ord(i)-ord('a')+1, '05b') for i in wm_str)
            case WMMode.LETTERS_UPPER_CASE:
                if not re.fullmatch(r'[A-Z]+', wm_str):
                    raise ValueError(
                        f'ERROR: invalid watermark wm_mode: {wm_str} are not upper case letters ')
                wm_bin = ''.join(
                    format(ord(i)-ord('A')+1, '05b') for i in wm_str)
            case WMMode.LETTERS_MIXED_CASE:
                if not re.fullmatch(r'[a-zA-Z]+', wm_str):
                    raise ValueError(
                        f'ERROR: invalid watermark wm_mode: {wm_str} are not mixed case letters ')
                wm_bin = ''.join(
                    format(ord(i)-ord('A')+1, '06b') for i in wm_str)
            case WMMode.ALPHA_NUMERICAL:
                if not re.fullmatch(r'[0-9a-zA-Z]+', wm_str):
                    raise ValueError(
                        f'ERROR: invalid watermark wm_mode: {wm_str} are not mixed case letters ')
                for i in wm_str:
                    ord_i = ord(i)
                    if ord('0') <= ord_i <= ord('9'):
                        wm_bin += format(ord_i - ord('0') + 1, '06b')
                    elif ord('A') <= ord_i <= ord('Z'):
                        wm_bin += format(ord_i - ord('A') + 1 + 10, '06b')
                    elif ord('a') <= ord_i <= ord('z'):
                        wm_bin += format(ord_i - ord('a') + 1 + 36, '06b')
            case WMMode.ALPHA_NUMERICAL_SPECIAL:
                if not re.fullmatch(r'[!-~]+', wm_str):
                    raise ValueError(
                        f'ERROR: invalid watermark wm_mode: {wm_str} are not mixed case letters ')
                wm_bin = ''.join(format(ord(i), '07b') for i in wm_str)
            case WMMode.UNICODE:
                wm_bin = BitArray(wm_str.encode('UTF-8')).bin
            case _:
                raise ValueError(
                    f'ERROR: invalid watermark wm_mode: {self.wm_mode}')

        # convert wm_bin to arbitrary base string
        if self.wm_base < 2 or self.wm_base > 36:
            raise ValueError(
                f'Error: Unsupported base value. Must be between 2 and 16: {self.wm_base}')
        num = np.base_repr(int(wm_bin, 2), self.wm_base)
        return str(num)

    def _get_str_from_bin(self, wm_bin: str, bin_len: int, offset: int):
        '''Generate the watermark string from binary string.

        Args:
            wm_bin (str): watermark binary string
            bin_len (int): The number of bytes representing a watermark character
            offset (int): The number of leading bits of the binary string

        Returns:
            (str): restored watermark string
        '''

        wm_str = ''
        if len(wm_bin) % bin_len != 0:
            wm_bin = wm_bin.zfill(bin_len - len(wm_bin) %
                                  bin_len + len(wm_bin))

        for i in range(0, len(wm_bin), bin_len):
            wm_str += chr(int(wm_bin[i:i + bin_len], 2) + offset)
        return wm_str

    def wm_restore_from_arbitrary_base(self, wm_final: str):
        '''Restore watermark from arbitrary base string

        Args:
            wm_final (str): Arbitrary base watermark string

        Returns:
            (str): restored watermark string

        Raises:
            Error: If Invalid WMMode

        '''

        # convert wm_bin from arbitrary base string
        wm_bin = str(bin(int(wm_final, self.wm_base)))[2:]

        wm_str = ''
        match self.wm_mode:
            case WMMode.REAL_NUMBER:
                wm_str = str(int(wm_bin, 2))
            case WMMode.LETTERS_LOWER_CASE:
                wm_str = self._get_str_from_bin(wm_bin, 5, ord('a')-1)
            case WMMode.LETTERS_UPPER_CASE:
                wm_str = self._get_str_from_bin(wm_bin, 5, ord('A')-1)
            case WMMode.LETTERS_MIXED_CASE:
                wm_str = self._get_str_from_bin(wm_bin, 6, ord('A')-1)
            case WMMode.ALPHA_NUMERICAL:
                if len(wm_bin) % 6 != 0:
                    wm_bin = wm_bin.zfill(6 - len(wm_bin) % 6 + len(wm_bin))
                for i in range(0, len(wm_bin), 6):
                    num = int(wm_bin[i:i + 6], 2)
                    if num <= 10:
                        wm_str += chr(num + ord('0') - 1)
                    elif 10 < num <= 36:
                        wm_str += chr(num + ord('A') - 1 - 10)
                    elif 36 < num <= 62:
                        wm_str += chr(num + ord('a') - 1 - 36)
            case WMMode.ALPHA_NUMERICAL_SPECIAL:
                wm_str = self._get_str_from_bin(wm_bin, 7, 0)
            case WMMode.UNICODE:
                wm_str = BitArray(bin=wm_bin).bytes.decode(encoding='UTF-8')
            case _:
                raise ValueError(f'ERROR: Invalid WMMode: {self.wm_mode}')

        return wm_str
