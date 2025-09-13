#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import pyparsing as pp

input_str = "foo = 23 + 42 * 10"
pp_expr = (
    pp.Word(pp.alphas)
    + "="
    + pp.Word(pp.nums)
    + "+"
    + pp.Word(pp.nums)
    + "*"
    + pp.Word(pp.nums)
)


if __name__ == "__main__":
    print(pp_expr(input_str))
