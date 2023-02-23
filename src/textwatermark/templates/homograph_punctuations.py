'''Homographs in Punctuations'''
from textwatermark.defines import WMMethod

# 同形异义-标点
CONFUSABLES_CHARS = {
    '!': 'ǃ！',
    '"': 'ʺ＂',
    '%': '٪⁒',
    '\'': 'ꞌ᾽',
    '*': '⁎∗',
    ',': '٫‚',
    '-': '‐‑',
    '.': 'ꓸ․',
    '/': 'Ⳇ∕',
    ':': '˸∶',
    '?': 'ʔॽ',
    ';': ';；',
    '\\': '∖⧵',
    '~': '⁓∼',
    '‧': '··',
    '¯': 'ˉ‾',
    # '“': '‟‶',
    # '”': 'ˮ″',
    # '‘': 'ʻ‵',
    # '’': 'ʼ′',
    # '(': '❨﴾',
    # ')': '❩﴿',
    # '<': '˂❮',
    # '>': '˃❯',
}

for ikey, ival in CONFUSABLES_CHARS.items():
    CONFUSABLES_CHARS[ikey] = ikey + ival
method = WMMethod.FIND_AND_REPLACE
