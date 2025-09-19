#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import re
import node


tokens = [
    r"(?P<VAR>[a-zA-Z_]\w*)",
    r"(?P<NUM>\d+)",
    r"(?P<PLUS>\+)",
    r"(?P<MINUS>\-)",
    r"(?P<MUL>\*)",
    r"(?P<DIV>/)",
    r"(?P<WS>\s*)",
]

master_pat = "|".join(tokens)


def yield_tokens(input_str: str):
    for tok in re.finditer(master_pat, input_str):
        yield tok


class ExpressionEvaluator:
    def parse(self, text):
        return self.expr()

    def _advance(self):
        pass

    def _accept(self, toktype):
        pass

    def _expect(self, toktype):
        pass

    def expr(self):
        pass

    def term(self):
        pass

    def factor(self):
        pass


class ParseExpr:
    """
    expr   ::= expr + term | expr - term | term
    term   ::= term * factor | term / factor | factor
    factor ::= ( expr ) | NUM

    """

    def __init__(self, input_str: str):
        self.input_str = input_str
        self.matches = [
            m.group(0)
            for m in re.finditer(master_pat, input_str)
            if not m.group(0).isspace()
        ]

    def parse_expr(self, matches: list) -> node.Node:
        pass

    def parse_term(self) -> node.Node:
        pass

    def parse_factor(self) -> node.Node:
        pass
