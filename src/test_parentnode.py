import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_none_tag(self):
        node = ParentNode(None, None)
        with self.assertRaises(ValueError) as e:
            node.to_html()
        self.assertEqual("Should have tag", str(e.exception))

    def test_to_html_with_none_children(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError) as e:
            node.to_html()
        self.assertEqual("Should have children", str(e.exception))

    def test_to_html_with_leaf_childrens(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html())

    def test_to_html_with_parent_childrens(self):
        child_parent_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode("i", "italic text"),
            ]
        )
        node = ParentNode(
            "div",
            [
                child_parent_node,
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual("<div><p><b>Bold text</b><i>italic text</i></p>Normal text</div>", node.to_html())
