import unittest

from src.html.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode("h1", "something")
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html_when_none(self):
        node = HTMLNode("a", "something")
        self.assertEqual("", node.props_to_html())

    def test_props_to_html_when_present(self):
        node = HTMLNode("a", "boot.dev", props={"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(' href="https://boot.dev" target="_blank"', node.props_to_html())

    def test_representation_when_all_none(self):
        node = HTMLNode()
        self.assertEqual("HTMLNode(None, None, None, None)", str(node))

    def test_representation_when_all_present(self):
        children_node = HTMLNode("img", None, None, props={"source": "http://boot.dev/img.jpg", "alt": "test image"})
        node = HTMLNode("a", "boot.dev", [children_node], props={"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual("HTMLNode(a, boot.dev, 1 children, {'href': 'https://boot.dev', 'target': '_blank'})", str(node))

    def test_opening_tag_with_none(self):
        node = HTMLNode()
        self.assertEqual("", node.opening_tag())

    def test_opening_tag_with_props(self):
        node = HTMLNode("a", "boot.dev", None, props={"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual('<a href="https://boot.dev" target="_blank">', node.opening_tag())

    def test_opening_tag_without_props(self):
        node = HTMLNode("a", "boot.dev", None, None)
        self.assertEqual('<a>', node.opening_tag())

    def test_closing_tag_with_none(self):
        node = HTMLNode()
        self.assertEqual("", node.closing_tag())

    def test_closing_tag(self):
        node = HTMLNode("a", "boot.dev", None, None)
        self.assertEqual('</a>', node.closing_tag())

if __name__ == "__main__":
    unittest.main()
