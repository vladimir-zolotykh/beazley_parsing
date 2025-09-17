#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from node import Add, Number
import visitor


class Evaluator(visitor.Visitor):
    def visit_div(self, node):
        pass

    def visit_sub(self, node):
        pass

    def visit_negate(self, node):
        return -self.visit(node.operand)

    def visit_add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_mul(self, node):
        pass

    def visit_number(self, node):
        return node.val


if __name__ == "__main__":
    t1 = Add(Number(3), Number(5))
    e = Evaluator()
    print(e.visit(t1))
