import re
from enum import Enum

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

def markdown_to_blocks(markdown):
    return list(
        filter(
            None,
            map(
                lambda x: x.strip(),
                markdown.split("\n\n")
            )
        )
    )

def block_to_block_type(block):
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
