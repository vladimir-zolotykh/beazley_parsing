#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class Visitor:
    def visit(self, node):
        typ = type(node).__name__.lower()
        self.meth_name = f"visit_{typ}"
        meth = getattr(self, self.meth_name, self.visit_generic)
        return meth(node)

    def visit_generic(self, node):
        raise TypeError(f"No {self.meth_name} method found for {node}")
