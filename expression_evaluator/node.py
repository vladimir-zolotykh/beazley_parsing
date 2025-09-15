#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK

# expr   ::= expr + term | expr - term | term
# term   ::= term * factor | term / factor | factor
# factor ::= ( expr ) | NUM


class Node:
    pass


class UnaryOperator(Node):
    pass


class BinaryOperator(Node):
    pass


class Number(Node):
    pass
