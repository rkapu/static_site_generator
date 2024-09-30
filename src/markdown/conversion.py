from src.markdown.block import *
from src.html.parentnode import *

def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    return (
        __extract_title_from_markdown_blocks(blocks),
        __markdown_blocks_to_html_node(blocks).to_html()
    )

def markdown_to_blocks(markdown):
    return list(
        map(
            lambda x: Block(x),
            filter(
                None,
                map(
                    lambda x: x.strip(),
                    markdown.split("\n\n")
                )
            )
        )
    )

def __extract_title_from_markdown_blocks(markdown_blocks):
    h1 = None
    for block in markdown_blocks:
        if block.type == BlockType.HEADING:
            if block.text.startswith("# "):
                h1 = block.text.lstrip("# ")
                break

    if not h1:
        raise ValueError("No title found in the list of markdown blocks")

    return h1

def __markdown_blocks_to_html_node(markdown_blocks):
    return ParentNode(
        "div",
        list(
            map(
                lambda x: x.to_html_node(),
                markdown_blocks
            )
        )
    )
