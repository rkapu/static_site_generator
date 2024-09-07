import unittest
from helpers import text_node_to_html_node
from textnode import TextType, TextNode

class TestHelpers(unittest.TestCase):
    def test_text_node_to_html_node_with_valid_text_types(self):
        test_cases = [
            [("test text", TextType.TEXT, None), (None, "test text", None)],
            [("test text", TextType.BOLD, None), ("b", "test text", None)],
            [("test text", TextType.ITALIC, None), ("i", "test text", None)],
            [("test text", TextType.CODE, None), ("code", "test text", None)],
            [("test text", TextType.LINK, "https://boot.dev"), ("a", "test text", {"href": "https://boot.dev"})],
            [("test image text", TextType.IMAGE, "https://boot.dev"), ("img", "", {"src": "https://boot.dev", "alt": "test image text"})],
        ]

        for t in test_cases:
            text_node = TextNode(*t[0])
            leaf_node = text_node_to_html_node(text_node)
            self.assertEqual(
                (leaf_node.tag, leaf_node.value, leaf_node.props),
                (t[1])
            )

    def test_text_node_to_html_node_with_invalid_text_type(self):
        text_node = TextNode("test text", "divider", None)
        with self.assertRaises(ValueError) as e:
            text_node_to_html_node(text_node)
        self.assertEqual("Invalid text type: divider", str(e.exception))
