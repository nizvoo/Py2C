#!/usr/bin/env python

import unittest

import py2c.dual_ast as dual_ast


class DummyNode(dual_ast.AST):
    def __init__(self, attrs=None, *args, **kwargs):
        if attrs is None:
            attrs = []
        self._attrs = attrs
        super(DummyNode, self).__init__(*args, **kwargs)


# -----------------------------------
class ASTTestCase(unittest.TestCase):
    """Tests for AST node"""

    def test_init1(self):
        "A no-subclass directly invocation of init method of AST"
        with self.assertRaises(AttributeError):
            dual_ast.AST()

    def test_equality_equal1(self):
        "Test for equality for really equal Nodes"
        attrs = [("foo", None, False), ('bar', '[]', True)]

        node1 = DummyNode(attrs)
        node2 = DummyNode(attrs)

        self.assertEqual(node1, node2)

    def test_equality_equal2(self):
        "Test for equality with node when it has children nodes"
        node1 = DummyNode(dest=DummyNode(id='foo'), values=[],
                          sep=' ', end='\n')
        node2 = DummyNode(dest=DummyNode(id='foo'), values=[],
                          sep=' ', end='\n')
        self.assertEqual(node1, node2)

    def test_equality_with_extra_attrs(self):
        "Test for (in)equality on nodes with in-equal attributes"
        node1 = DummyNode([("foo", None, False)])
        node2 = DummyNode([("foo", None, False), ("bar", None, False)])

        self.assertNotEqual(node1, node2)

    def test_equality_diff_type(self):
        "Test for inequality on the basis of type"
        node1 = DummyNode([])

        self.assertNotEqual(node1, "I'm not equal to a Node")

    # A really important and useful test. Create the node_names list!!
    def test_nodes_exist(self):
        "Checks if to see that all required nodes exist in '_dual_ast.py'"

        node_names = [
            # Python AST nodes
            "AST", "Add", "And", "Assert", "Assign", "Attribute", "AugAssign",
            "AugLoad", "AugStore", "BinOp", "BitAnd", "BitOr", "BitXor",
            "BoolOp", "Break", "Bytes", "Call", "ClassDef", "Compare",
            "Continue", "Del", "Delete", "Dict", "DictComp", "Div",
            "Ellipsis", "Eq", "ExceptHandler", "Exec", "Expr", "Expression",
            "ExtSlice", "FloorDiv", "For", "FunctionDef", "GeneratorExp",
            "Global", "Gt", "GtE", "If", "IfExp", "Import", "ImportFrom",
            "In", "Index", "Interactive", "Invert", "Is", "IsNot", "LShift",
            "Lambda", "List", "ListComp", "Load", "Lt", "LtE", "Mod",
            "Module", "Mult", "Name", "Nonlocal", "Not", "NotEq", "NotIn",
            "Num", "Or", "Param", "Pass", "Pow", "Print", "RShift", "Raise",
            "Repr", "Return", "Set", "SetComp", "Slice", "Starred", "Store",
            "Str", "Sub", "Subscript", "Suite", "Try", "TryExcept",
            "TryFinally", "Tuple", "UAdd", "USub", "UnaryOp", "While", "With",
            "Yield", "YieldFrom", "alias", "arg", "arguments", "boolop",
            "cmpop", "comprehension", "excepthandler", "expr", "expr_context",
            "keyword", "mod", "operator", "slice", "stmt", "unaryop",
            "withitem",
            # C AST nodes
        ]
        missing = []
        for name in node_names:
            if not hasattr(dual_ast, name):
                missing.append(name)
        if missing:
            msg = "The following nodes are missing: "+", ".join(missing)
            self.fail(msg)


if __name__ == '__main__':
    unittest.main()