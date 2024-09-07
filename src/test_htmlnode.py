import unittest

from htmlnode import HTMLNode

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
