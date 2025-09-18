#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> t1 = Add(Number(3), Number(5))
>>> t2 = Sub(Number(10), Number(4))
>>> t3 = Div(t2, t1)
>>> Evaluator.visit(t3)
0.75

# Representation of 1 + 2 * (3 - 4) / 5
>>> t1 = Sub(Number(3), Number(4))
>>> t2 = Mul(Number(2), t1)
>>> t3 = Div(t2, Number(5))
>>> t4 = Add(Number(1), t3)
>>> Evaluator.visit(t4)
0.6
"""
from node import Add, Sub, Mul, Div, Number  # noqa: F401
import visitor


class Evaluator(visitor.Visitor):
    @classmethod
    def visit_div(cls, node):
        return cls.visit(node.left) / cls.visit(node.right)

    @classmethod
    def visit_sub(cls, node):
        return cls.visit(node.left) - cls.visit(node.right)

    @classmethod
    def visit_negate(cls, node):
        return -cls.visit(node.operand)

    @classmethod
    def visit_add(cls, node):
        return cls.visit(node.left) + cls.visit(node.right)

    @classmethod
    def visit_mul(cls, node):
        return cls.visit(node.left) * cls.visit(node.right)

    @classmethod
    def visit_number(cls, node):
        return node.val


if __name__ == "__main__":
    import doctest

    doctest.testmod()
