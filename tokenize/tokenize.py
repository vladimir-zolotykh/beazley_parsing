#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import re

st = "foo = 23 + 42 * 10"
tokens = [
    r"(?P<NAME>[A-Za-z]\w*)",
    r"(?P<NUM>\d+)",
    r"(?P<EQ>=)",
    r"(?P<PLUS>\+)",
    r"(?P<MUL>\*)",
    r"(?P<WS>\s)",
]

master_pat = "|".join(tokens)

if __name__ == "__main__":
    for match in re.finditer(master_pat, st):
        if (m := match.group(0)) and not m.isspace():
            print(m)
