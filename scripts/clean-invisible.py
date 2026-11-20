"""Strip invisible Unicode from a text file in place. Usage: python clean-invisible.py FILE

Removes zero-width chars, BOM, soft hyphen, bidi controls and tag chars; turns
exotic spaces (NBSP, thin, ideographic...) into a plain space. Prints the count removed.
shortcut: ZWJ/ZWNJ are removed too, fine for EN/ID articles, not for emoji sequences or Persian/Indic text.
"""
import re
import sys

INVISIBLE = re.compile('[​-‏‪-‮⁠-⁤⁦-⁩­᠎﻿\U000e0000-\U000e007f]')
SPACES = re.compile('[   -   　]')


def clean(text):
    text, n = INVISIBLE.subn('', text)
    text, m = SPACES.subn(' ', text)
    return text, n + m


if __name__ == '__main__':
    path = sys.argv[1]
    with open(path, encoding='utf-8', newline='') as f:
        text = f.read()
    text, count = clean(text)
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(text)
    print(f'cleaned {count} invisible characters in {path}')
