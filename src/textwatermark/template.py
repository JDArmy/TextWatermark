'''
WMTemplate is mainly used to load template, set related parameters, 
and insert watermark into text
'''
# pylint: disable=consider-using-enumerate


import re
from typing import Union

import numpy as np

from textwatermark.defines import WMMethod


class WMTemplate:
    '''Class of WMTemplate

    Example
    --------
    ```py 
    wmt = WMTemplate(
        template.confusables_chars,
        template.confusables_chars_length,
        template.method,
        confusables_chars_key)

    wm_text = wmt.insert_watermark(
        text=text,
        wm_final=wm_final,
        start_at=start_at,
        loop=False)

    wm_final = wmt.retrieve_watermark(
        wm_text=wm_text,
        wm_base=wmt.wm_base,
        wm_len=len(wm_final),
        start_at=start_at)
    ```
    '''

    def __init__(self, confusables_chars: Union[dict, list], wm_base: int, method: WMMethod,
                 confusables_chars_key: str = ''):
        '''Init of WMTemplate

        Args:
            confusables_chars (Union[dict, list]): The default template is in templates, 
                you can your the modified custom template 
            wm_base (int): Watermark convert base. Must be less than 
                or equal to confusables_chars_length 
            method (WMMethod):  Watermark insertion method, 
                see defines.WMMethod for details 
            confusables_chars_key (str): Key must be set when
                WMMethod is DECORATE_EACH_CHAR

        Note: Note of wm_base
            The value of wm_base will affect the range of watermark characters taken 
                from confusables_chars

        '''

        self.confusables_chars = confusables_chars
        '''The default template is in templates, 
                you can your the modified custom template '''
        if wm_base == 0:
            self.wm_base = WMTemplate.get_wm_base_from_tpl(
                self.confusables_chars)
            '''Watermark convert base. Must be less than or equal to confusables_chars_length '''
        else:
            self.wm_base = wm_base

        self.method = method
        '''Watermark insertion method, see defines.WMMethod for details '''

        if self.method in [WMMethod.DECORATE_EACH_CHAR, WMMethod.APPEND_AS_BINARY] and \
                confusables_chars_key not in self.confusables_chars:
            raise ValueError(
                'When WMMethod in [DECORATE_EACH_CHAR,APPEND_AS_BINARY], confusables_chars_key: '
                f'{confusables_chars_key} must can be found in confusables_chars\'s keys.')

        self.confusables_chars_key = confusables_chars_key
        '''Key must be set when WMMethod is DECORATE_EACH_CHAR'''

    @ staticmethod
    def get_wm_base_from_tpl(confusables_chars):
        '''get wm_base from template's confusables chars

        Args:
            confusables_chars (dict): confusables chars template

        Returns:
            (int): wm_base

        '''
        if isinstance(confusables_chars, list):
            wm_base = len(confusables_chars)
        elif isinstance(confusables_chars, dict):
            wm_base = len(list(confusables_chars.values())[0])
        else:
            raise TypeError('confusables_chars must be list or dict')

        wm_base = max(wm_base, 2)
        wm_base = min(wm_base, 36)

        return wm_base
    ################################# Clean watermark#################################

    def clean_html_tags(self, html):
        '''Clean html tags from watermark.

        Args:
            html (str): HTML code

        Returns:
            (str): Cleaned HTML code
        '''
        return re.sub(r'<[^<]+?>', '', html)

    def clean_text(self, text: str):
        '''clean confusables chars from text

        Args:
            text (str): Text to clean

        Returns:
            (str): Cleaned text

        Raises:
            ValueError: If unknown method

        '''
        text = self.clean_html_tags(text)

        match self.method:
            case WMMethod.FIND_AND_REPLACE:
                for key, vals in self.confusables_chars.items():
                    if isinstance(vals, list):
                        vals = ''.join(vals)
                    vals = vals.replace(key, '')
                    for val in vals:
                        text = text.replace(val, key)
            case WMMethod.DECORATE_EACH_CHAR:
                # use self.clean_html_tags by default
                pass
            case WMMethod.INSERT_INTO_POSITION | WMMethod.APPEND_TO_CHAR:
                for val in self.confusables_chars:
                    text = text.replace(val, '')
            case WMMethod.APPEND_AS_BINARY:
                text = text.replace(
                    self.confusables_chars[self.confusables_chars_key], '')
            case _:
                raise ValueError(f'Unknown WMMethod: {self.method}')
        # print(text)
        return text

    ################################# Insert watermark#################################

    def insert_watermark(self, text: str, wm_final: str, start_at: int = 0, loop: bool = False):
        '''Insert watermark into text

        Args:
            text (str): Text to be watermarked
            wm_final (str): The final watermark string
            start_at (int): The offset position for insert watermark
            loop (bool): Whether to insert the watermark in a loop

        Returns:
            (str): Watermarked text

        Raises:
            ValueError: If start_at is larger than text length
            ValueError: If there is not enough space to insert a watermark
            VaueError: If unknown watermark method

        '''
        if start_at > len(text):
            raise ValueError(
                f'Start_at is {start_at}, larger than text length: {len(text)}')

        text = self.clean_text(text=text)

        if start_at > 0:
            out_text = text[0:start_at]
            text = text[start_at:]
        else:
            out_text = ''

        match self.method:
            case WMMethod.FIND_AND_REPLACE:
                times = self.check_find_and_replace_space(
                    text, len(wm_final))
                if times < 1:
                    raise ValueError(
                        f'There is not enough space to insert a watermark: {wm_final}')

                out_text += self._find_and_replace(
                    text=text, wm_final=wm_final, loop=loop)
            case WMMethod.DECORATE_EACH_CHAR:
                if len(wm_final) > len(text):
                    raise ValueError(
                        f'There is not enough space to insert a watermark: {wm_final}')

                out_text += self._decorate_each_char(
                    text=text, wm_final=wm_final, loop=loop)
            case WMMethod.INSERT_INTO_POSITION:
                out_text += self._insert_into_position(
                    text=text, wm_final=wm_final)
            case WMMethod.APPEND_TO_CHAR:
                if len(wm_final) > len(text):
                    raise ValueError(
                        f'There is not enough space to insert a watermark: {wm_final}')

                out_text += self._append_to_char(
                    text=text, wm_final=wm_final, loop=loop)
            case WMMethod.APPEND_AS_BINARY:
                if len(wm_final) > len(text):
                    raise ValueError(
                        f'There is not enough space to insert a watermark: {wm_final}')

                out_text += self._append_as_binary(
                    text=text, wm_final=wm_final, loop=loop)
            case _:
                raise ValueError(f'Unknown watermark method: {self.method}')

        return out_text

    def check_find_and_replace_space(self, text: str, wm_len: int):
        '''Check if enough space for insert watermark

        Args:
            text (str): text to check
            wm_len (int): watermark length
        Returns:
            (int): number of times can insert watermark

        Note: Why use this method?
            Because WMMethod.FIND_AND_REPLACE mode must need enough space 
            to find special char and replace to watermarked char
        '''
        actual_len = 0
        confusables_chars_keys = ''.join(self.confusables_chars.keys())
        # 计算可插入的水印空间大小
        for char in text:
            if confusables_chars_keys.find(char) != -1:
                actual_len += 1
        times = actual_len // wm_len
        return times

    def _find_and_replace(self, text: str, wm_final: str, loop: bool):
        confusables_chars_keys = ''.join(self.confusables_chars.keys())
        wm_idx = 0
        wm_text = ''
        for idx in range(len(text)):
            if not loop and wm_idx >= len(wm_final):
                wm_text += text[idx:]
                break
            # 查找并替换成水印字符
            if confusables_chars_keys.find(text[idx]) != -1:
                offset = wm_final[wm_idx % len(wm_final)]
                wm_text += self.confusables_chars[text[idx]][int(offset)]
                wm_idx += 1
            else:
                wm_text += text[idx]
        return wm_text

    def _decorate_each_char(self, text: str, wm_final: str, loop: bool):
        wm_idx = 0
        wm_text = ''
        for idx in range(len(text)):
            if not loop and wm_idx >= len(wm_final):
                wm_text += text[idx:]
                break
            offset = wm_final[wm_idx % len(wm_final)]
            wm_text += self.confusables_chars[self.confusables_chars_key][int(
                offset)].replace('{char}', text[idx])

            wm_idx += 1

        return wm_text

    def _insert_into_position(self, text: str, wm_final: str):
        wm_out_str = ''
        for wm_char in wm_final:
            wm_out_str += self.confusables_chars[int(
                wm_char, self.wm_base)]
        return wm_out_str + text

    def _append_to_char(self, text: str, wm_final: str, loop: bool):
        wm_idx = 0
        wm_text = ''
        for idx in range(len(text)):
            if not loop and wm_idx >= len(wm_final):
                wm_text += text[idx:]
                break
            # 在每个字符串后添加字符
            offset = wm_final[wm_idx % len(wm_final)]
            wm_text += text[idx] + \
                self.confusables_chars[int(str(offset), self.wm_base)]
            wm_idx += 1
        return wm_text

    def _append_as_binary(self, text: str, wm_final: str, loop: bool):
        wm_idx = 0
        wm_text = ''
        for idx in range(len(text)):
            if not loop and wm_idx >= len(wm_final):
                wm_text += text[idx:]
                break
            # 在每个字符串后添加字符
            offset = wm_final[wm_idx % len(wm_final)]
            if offset == '0':
                wm_text += text[idx]
            else:
                wm_text += text[idx] + \
                    self.confusables_chars[self.confusables_chars_key]
            wm_idx += 1
        return wm_text

    ################################# Retrieve watermark#################################

    def retrieve_watermark(self, wm_text: str, wm_base: int, wm_len: int, start_at: int = 0):
        '''Retrieve watermark from watermarked text

        Args:
            wm_text (str): Text which has be watermarked
            wm_base (int): The encoding base of the watermark string
            wm_len (int): The fixed length of watermark
            start_at (int): The offset position of insert watermark

        Returns:
            (str): The final watermark retrieved from text

        Raises:
            ValueError: If `start_at` is larger than `wm_text` length
            ValueError: If the length of retrieve watermark is not larger then `wm_len`
            ValueError: If unknown watermark method

        '''
        if start_at > len(wm_text):
            raise ValueError(
                f'start_at: {start_at} is larger than wm_text length: {len(wm_text)}')

        if start_at > 0:
            wm_text = wm_text[start_at:]

        wm_str = ''
        match self.method:
            case WMMethod.FIND_AND_REPLACE:
                wm_str = self._retrieve_find_and_replace(
                    wm_text, wm_len)
            case WMMethod.DECORATE_EACH_CHAR:
                wm_str = self._retrieve_decorate_each_char(
                    wm_text, wm_base, wm_len)
            case WMMethod.INSERT_INTO_POSITION:
                wm_str = self._retrieve_insert_into_position(
                    wm_text, wm_base, wm_len)
            case WMMethod.APPEND_TO_CHAR:
                wm_str = self._retrieve_append_to_char(
                    wm_text, wm_base, wm_len)
            case WMMethod.APPEND_AS_BINARY:
                wm_str = self._retrieve_append_as_binary(
                    wm_text, wm_len)
            case _:
                raise ValueError(f'Unknown watermark method: {self.method}')

        if len(wm_str) < wm_len:
            raise ValueError(
                f'Watermark is: {wm_str}, length is less than {wm_len}')

        return wm_str[0: wm_len]

    def _retrieve_find_and_replace(self, wm_text: str, wm_len: int):
        vals = self.confusables_chars.values()
        confusables_chars_length = len(list(vals)[0])
        confusables_chars_values = ''
        for val in vals:
            if isinstance(val, list):
                confusables_chars_values += ''.join(val)
            if isinstance(val, str):
                confusables_chars_values += val
        wm_temp = ''
        for char in wm_text:
            distances = confusables_chars_values.find(char)
            if distances != -1:
                offset = int(distances % confusables_chars_length)
                # print(distances, offset)
                wm_temp += str(offset)
            if len(wm_temp) > wm_len:
                break
        return wm_temp

    def _retrieve_decorate_each_char(self, wm_text: str, wm_base: int, wm_len: int):
        confusables_chars = self.confusables_chars[self.confusables_chars_key]
        for idx in range(len(confusables_chars)):
            offset = int(idx % wm_base)
            regex = confusables_chars[idx].replace('{char}', '.*?')
            wm_text = re.sub(regex, f'<wm_char>{offset}</wm_char>', wm_text)

        matched = re.findall(r'<wm_char>(.*?)</wm_char>', wm_text)
        return ''.join(matched)[0:wm_len]

    def _retrieve_insert_into_position(self, wm_text: str, wm_base: int, wm_len: int):
        for idx in range(len(self.confusables_chars)):
            wm_val = np.base_repr(idx, wm_base)
            wm_text = wm_text.replace(
                self.confusables_chars[idx], f'<wm_char>{wm_val}</wm_char>')

        matched = re.findall(r'<wm_char>(.*?)</wm_char>', wm_text)
        return ''.join(matched)[0:wm_len]

    def _retrieve_append_to_char(self, wm_text: str, wm_base: int, wm_len: int):
        '''retrieve watermark from append to char'''
        return self._retrieve_insert_into_position(wm_text, wm_base, wm_len)

    def _retrieve_append_as_binary(self, wm_text: str, wm_len: int):
        '''retrieve watermark from append char as binary'''
        confusables_char = self.confusables_chars[self.confusables_chars_key]
        wm_start = False
        wm_final = ''

        for idx, char in enumerate(wm_text):
            if len(wm_final) == wm_len:
                break
            if char == confusables_char and wm_start is False:
                wm_start = True
            if wm_start is False:
                continue

            if char == confusables_char:
                wm_final += '1'
                continue

            if char != confusables_char and \
                    (idx+1 >= len(wm_text) or wm_text[idx+1] != confusables_char):
                wm_final += '0'
                continue
        if len(wm_final) != wm_len:
            raise ValueError(
                f'Retrieved watermark {wm_final}, length is not equal to {wm_len}')

        return wm_final
