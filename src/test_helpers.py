import unittest
from helpers import *
from textnode import TextType, TextNode

class TestHelpers(unittest.TestCase):
    def assert_all_cases(self, test_cases, test_function, transform_result_function = lambda x: x):
        for t in test_cases:
            if not isinstance(t[0], tuple):
                inputs = (t[0],)
            else:
                inputs = t[0]

            self.assertEqual(
                transform_result_function(test_function(*inputs)),
                t[1]
            )

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

        self.assert_all_cases(
            test_cases,
            text_node_to_html_node,
            lambda leaf_node: (leaf_node.tag, leaf_node.value, leaf_node.props)
        )

    def test_text_node_to_html_node_with_invalid_text_type(self):
        text_node = TextNode("test text", "divider", None)
        with self.assertRaises(ValueError) as e:
            text_node_to_html_node(text_node)
        self.assertEqual("Invalid text type: divider", str(e.exception))

    def test_split_nodes_delimiter(self):
        test_cases = [
            [
                (
                    [TextNode("This is text with a `code block` word", TextType.TEXT)],
                    "`",
                    TextType.CODE
                ),
                [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" word", TextType.TEXT),
                ]
            ],
            [
                (
                    [TextNode("This is **text** with **bold** words", TextType.TEXT)],
                    "**",
                    TextType.BOLD
                ),
                [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" with ", TextType.TEXT),
                    TextNode("bold", TextType.BOLD),
                    TextNode(" words", TextType.TEXT),
                ]
            ],
            [
                (
                    [TextNode("This is *text* with *italic* words", TextType.TEXT)],
                    "*",
                    TextType.ITALIC
                ),
                [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.ITALIC),
                    TextNode(" with ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" words", TextType.TEXT),
                ]
            ],
            [
                (
                    split_nodes_delimiter(
                        [TextNode("This is *text* with *italic* and **bold** words together", TextType.TEXT)],
                        "**",
                        TextType.BOLD
                    ),
                    "*",
                    TextType.ITALIC
                ),
                [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.ITALIC),
                    TextNode(" with ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" and ", TextType.TEXT),
                    TextNode("bold", TextType.BOLD),
                    TextNode(" words together", TextType.TEXT),
                ]
            ]
        ]

        self.assert_all_cases(test_cases, split_nodes_delimiter)

    def test_split_nodes_delimiter_invalid_markdown(self):
        text_node = [TextNode("This is *text* with **invalid markdown", TextType.TEXT)]
        with self.assertRaises(ValueError) as e:
            split_nodes_delimiter(text_node, "**", TextType.ITALIC)
        self.assertEqual("Invalid markdown, formatted section not closed", str(e.exception))

    def test_extract_markdown_images(self):
        test_cases = [
            [
                "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
                [
                    ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                    ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
                ],
            ],
            [
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                []
            ],
            [
                "This is text without images",
                []
            ]
        ]

        self.assert_all_cases(test_cases, extract_markdown_images)

    def test_extract_markdown_links(self):
        test_cases = [
            [
                "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
                [],
            ],
            [
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                [
                    ("to boot dev", "https://www.boot.dev"),
                    ("to youtube", "https://www.youtube.com/@bootdotdev")
                ]
            ],
            [
                "This is text without links",
                []
            ]
        ]

        self.assert_all_cases(test_cases, extract_markdown_links)
