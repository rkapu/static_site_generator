from src.markdown.blocks import *
from src.markdown.inline import *
from src.html.parentnode import *
from src.html.leafnode import *
from src.html.htmlnode import *

def markdown_to_html(markdown):
    return markdown_to_html_node(markdown).to_html()

def markdown_to_html_node(markdown):
    return ParentNode(
        "div",
        list(
            map(
                html_node_from_block,
                markdown_to_blocks(markdown)
            )
        )
    )


def html_node_from_block(block):
    block_type = block_to_block_type(block)
    html_tag = html_tag_from_block_type(block, block_type)
    childrens = text_to_children(block, block_type)

    if len(childrens):
        return ParentNode(html_tag, childrens)

    return LeafNode(html_tag, block)

def text_to_children(block, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            return list(
                map(
                    text_node_to_html_node,
                    text_to_textnodes(block)
                )
            )
        case BlockType.HEADING:
            _, heading_text = block.split(" ", 1)

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
                    text_to_textnodes(block.strip("```"))
                )
            )

            return [ParentNode("code", code_childrens)]
        case BlockType.QUOTE:
            prepared_block = "\n".join(map(lambda x: x.lstrip("> "), block.split("\n")))
            return list(
                map(
                    text_node_to_html_node,
                    text_to_textnodes(prepared_block)
                )
            )
        case BlockType.UNORDERED_LIST:
            items = block.split("\n")
            return list(
                map(
                    lambda l: ParentNode("li", list(map(text_node_to_html_node, text_to_textnodes(l[2:])))),
                    items
                )
            )
        case BlockType.ORDERED_LIST:
            items = block.split("\n")
            return list(
                map(
                    lambda l: ParentNode("li", list(map(text_node_to_html_node, text_to_textnodes(l[3:])))),
                    items
                )
            )
        case _:
            raise ValueError(f"Unknown BlockType value {block_type}")

def html_tag_from_block_type(block, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            return "p"
        case BlockType.HEADING:
            number = len(block.split()[0])
            return "h" + str(number)
        case BlockType.CODE:
            return "pre"
        case BlockType.QUOTE:
            return "blockquote"
        case BlockType.UNORDERED_LIST:
            return "ul"
        case BlockType.ORDERED_LIST:
            return "ol"
        case _:
            raise ValueError(f"Unknown BlockType value {block_type}")

