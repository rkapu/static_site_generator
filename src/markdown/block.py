import re
from enum import Enum
from src.markdown.inline import *
from src.html.parentnode import *
from src.html.leafnode import *
from src.html.htmlnode import *

BlockType = Enum(
    "BlockType",
    [
        "PARAGRAPH",
        "HEADING",
        "CODE",
        "QUOTE",
        "UNORDERED_LIST",
        "ORDERED_LIST"
    ]
)

class Block:
    def __init__(self, text):
        self.text = text
        self.type = self.__get_block_type(text)

    def to_html_node(self):
        html_tag = self.__get_html_tag()
        childrens = self.__get_html_childrens()

        if len(childrens):
            return ParentNode(html_tag, childrens)

        return LeafNode(html_tag, self.text)

    def __eq__(self, obj):
        return (
                self.text == obj.text
                and self.type == obj.type
        )

    def __get_html_tag(self):
        match self.type:
            case BlockType.PARAGRAPH:
                return "p"
            case BlockType.HEADING:
                number = len(self.text.split()[0])
                return "h" + str(number)
            case BlockType.CODE:
                return "pre"
            case BlockType.QUOTE:
                return "blockquote"
            case BlockType.UNORDERED_LIST:
                return "ul"
            case BlockType.ORDERED_LIST:
                return "ol"

    def __get_html_childrens(self):
        match self.type:
            case BlockType.PARAGRAPH:
                return list(
                    map(
                        text_node_to_html_node,
                        text_to_textnodes(self.text)
                    )
                )
            case BlockType.HEADING:
                _, heading_text = self.text.split(" ", 1)

                return list(
                    map(
                        text_node_to_html_node,
                        text_to_textnodes(heading_text)
                    )
                )
            case BlockType.CODE:
                code_childrens = list(
                    map(
                        text_node_to_html_node,
                        text_to_textnodes(self.text.strip("```"))
                    )
                )

                return [ParentNode("code", code_childrens)]
            case BlockType.QUOTE:
                prepared_block = "\n".join(map(lambda x: x.lstrip("> "), self.text.split("\n")))
                return list(
                    map(
                        text_node_to_html_node,
                        text_to_textnodes(prepared_block)
                    )
                )
            case BlockType.UNORDERED_LIST:
                items = self.text.split("\n")
                return list(
                    map(
                        lambda i: ParentNode("li", list(map(text_node_to_html_node, text_to_textnodes(i[2:])))),
                        items
                    )
                )
            case BlockType.ORDERED_LIST:
                items = self.text.split("\n")
                return list(
                    map(
                        lambda i: ParentNode("li", list(map(text_node_to_html_node, text_to_textnodes(i[3:])))),
                        items
                    )
                )

    def __get_block_type(self, block):
        lines = block.split("\n")

        if re.match(r"#{1,6} ", block):
            return BlockType.HEADING

        if len(lines) > 1 and block.startswith("```") and block.endswith("```"):
            return BlockType.CODE

        if block.startswith(">"):
            for line in lines:
                if not line.startswith(">"):
                    return BlockType.PARAGRAPH
            return BlockType.QUOTE

        if block.startswith("* "):
            for line in lines:
                if not line.startswith("* "):
                    return BlockType.PARAGRAPH
            return BlockType.UNORDERED_LIST

        if block.startswith("- "):
            for line in lines:
                if not line.startswith("- "):
                    return BlockType.PARAGRAPH
            return BlockType.UNORDERED_LIST

        if block.startswith("1. "):
            number = 1
            for line in lines:
                if not line.startswith(f"{number}. "):
                    return BlockType.PARAGRAPH
                number += 1
            return BlockType.ORDERED_LIST

        return BlockType.PARAGRAPH
