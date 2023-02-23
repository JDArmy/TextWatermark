'''Homographs in numbers'''

from textwatermark.defines import WMMethod

# 同形异义-数字
CONFUSABLES_CHARS = {
    '0': '᱐𝟘𝟎𝟢𝟬𝟶',
    '1': 'Ӏ𝟙𝟏𝟣𝟭𝟷',
    '2': 'ᒿ𝟚𝟐𝟤𝟮𝟸',
    '3': 'Ⳍ𝟛𝟑𝟥𝟯𝟹',
    '4': 'Ꮞ𝟜𝟒𝟦𝟰𝟺',
    '5': 'Ƽ𝟝𝟓𝟧𝟱𝟻',
    '6': 'Ⳓ𝟞𝟔𝟨𝟲𝟼',
    '7': 'ገ𝟟𝟕𝟩𝟳𝟽',
    '8': '৪𝟠𝟖𝟪𝟴𝟾',
    '9': 'Ꝯ𝟡𝟗𝟫𝟵𝟿',
    '.': '٠۰ꓸ․ͺ᎐',
}

for ikey, ival in CONFUSABLES_CHARS.items():
    CONFUSABLES_CHARS[ikey] = ikey + ival
method = WMMethod.FIND_AND_REPLACE
