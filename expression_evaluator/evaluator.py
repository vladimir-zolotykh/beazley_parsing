#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> e = Evaluator()
>>> t1 = Add(Number(3), Number(5))
>>> t2 = Sub(Number(10), Number(4))
>>> t3 = Div(t2, t1)
>>> e.visit(t3)
0.75

# Representation of 1 + 2 * (3 - 4) / 5
>>> t1 = Sub(Number(3), Number(4))
>>> t2 = Mul(Number(2), t1)
>>> t3 = Div(t2, Number(5))
>>> t4 = Add(Number(1), t3)
>>> e.visit(t4)
0.6
"""
from node import Add, Sub, Mul, Div, Number
import visitor


class Evaluator(visitor.Visitor):
    def visit_div(self, node):
        return self.visit(node.left) / self.visit(node.right)

    def visit_sub(self, node):
        return self.visit(node.left) - self.visit(node.right)

    def visit_negate(self, node):
        return -self.visit(node.operand)

    def visit_add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_mul(self, node):
        return self.visit(node.left) * self.visit(node.right)

    def visit_number(self, node):
        return node.val


if __name__ == "__main__":
    import doctest

    doctest.testmod()
