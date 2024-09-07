import unittest

from textnode import TextNode

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

if __name__ == "__main__":
    unittest.main()
