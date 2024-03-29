"""Watermark template of invisible chars.

All of the chars below are invisible on most of the text editors and WEB view.

In most cases, using this template is a pretty good choice.
"""

from ..defines import WMMethod

CONFUSABLES_CHARS: list = [
    "\u034f",
    "\u180b",
    "\u180c",
    "\u180d",
    "\u180e",
    "\u200b",
    "\u200e",
    "\u202a",
    "\u202b",
    "\u202c",
    "\u202d",
    "\ufe00",
    "\ufe01",
    "\ufe02",
    "\ufe03",
    "\ufe04",
    "\ufe05",
    "\ufe06",
    "\ufe07",
    "\ufe08",
    "\ufe09",
    "\ufe0a",
    "\ufe0b",
    "\ufe0c",
    "\ufe0d",
    "\ufe0e",
]

method: WMMethod = WMMethod.INSERT_INTO_POSITION
