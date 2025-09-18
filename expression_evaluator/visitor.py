#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class Visitor:
    @classmethod
    def get_meth_name(cls, node):
        typ = type(node).__name__.lower()
        return f"visit_{typ}"

    @classmethod
    def visit(cls, node):
        meth = getattr(cls, cls.get_meth_name(node), cls.visit_generic)
        return meth(node)

    @classmethod
    def visit_generic(cls, node):
        raise TypeError(f"No {cls.get_meth_name(node)} method found for {node}")
