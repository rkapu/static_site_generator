import unittest

from src.html.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_none_value(self):
        node = LeafNode(None, None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_without_tag(self):
        node = LeafNode(None, "This is a paragraph of text.")
        self.assertEqual("This is a paragraph of text.", node.to_html())

    def test_to_html_with_tag(self):
        node = LeafNode("h1", "This is a paragraph of text.")
        self.assertEqual("<h1>This is a paragraph of text.</h1>", node.to_html())

    def test_to_html_with_tag_and_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual('<a href="https://www.google.com">Click me!</a>', node.to_html())

    def test_representation(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual("LeafNode(a, Click me!, {'href': 'https://www.google.com'})", str(node))

if __name__ == "__main__":
    unittest.main()
