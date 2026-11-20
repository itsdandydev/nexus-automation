import importlib.util
import pathlib

path = pathlib.Path(__file__).resolve().parent.parent / 'scripts' / 'clean-invisible.py'
spec = importlib.util.spec_from_file_location('clean_invisible', path)
clean_invisible = importlib.util.module_from_spec(spec)
spec.loader.exec_module(clean_invisible)

dirty = 'a​b﻿c­ d‮e\U000e0041f g　h'
text, count = clean_invisible.clean(dirty)
assert text == 'abc def g h', repr(text)
assert count == 7, count

plain = 'Teks biasa, "kutipan", é, 日本語.\n'
assert clean_invisible.clean(plain) == (plain, 0)
print('ok')
