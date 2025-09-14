#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from pyparsing import Word, nums, alphas

str = "foo = 23 + 42 * 10"
expr = Word(alphas) + "=" + Word(nums) + "+" + Word(nums) + "*" + Word(nums)

if __name__ == "__main__":
    res = expr.parse_string(str)
    print(res)
