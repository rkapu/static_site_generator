import unittest

from tests.helpers import *
from src.markdown.textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq_without_url(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", "bold", "https://boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq_with_different_url(self):
        node = TextNode("This is a text node", "bold", "http://test.dev")
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq_with_different_text_type(self):
        node = TextNode("This is a text node", "bold", "https://boot.dev")
        node2 = TextNode("This is a text node", "italic", "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq_with_different_text(self):
        node = TextNode("This is a text node", "bold", "https://boot.dev")
        node2 = TextNode("This is a different text node", "bold", "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_representation(self):
        node = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertEqual(str(node), "TextNode(This is a text node, bold, https://boot.dev)")

class TestTextNodeFunctions(unittest.TestCase):
    def test_text_node_to_html_node_with_valid_text_types(self):
        test_cases = [
            [
                TextNode("test text", TextType.TEXT, None),
                (None, "test text", None)
            ],
            [
                TextNode("test text", TextType.BOLD, None),
                ("b", "test text", None)
            ],
            [
                TextNode("test text", TextType.ITALIC, None),
                ("i", "test text", None)
            ],
            [
                TextNode("test text", TextType.CODE, None),
                ("code", "test text", None)
            ],
            [
                TextNode("test text", TextType.LINK, "https://boot.dev"),
                ("a", "test text", {"href": "https://boot.dev"})
            ],
            [
                TextNode("test image text", TextType.IMAGE, "https://boot.dev"),
                ("img", "", {"src": "https://boot.dev", "alt": "test image text"})
            ]
        ]

        assert_all_cases(
            self,
            test_cases,
            text_node_to_html_node,
            lambda leaf_node: (leaf_node.tag, leaf_node.value, leaf_node.props)
        )

    def test_text_node_to_html_node_with_invalid_text_type(self):
        text_node = TextNode("test text", "divider", None)
        with self.assertRaises(ValueError) as e:
            text_node_to_html_node(text_node)
        self.assertEqual("Invalid text type: divider", str(e.exception))

if __name__ == "__main__":
    unittest.main()
