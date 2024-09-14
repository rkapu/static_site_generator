import re

from textnode import TextType, TextNode
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError(f"Invalid text type: {text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for index, section in enumerate(sections):
            if section == "":
                continue
            if index % 2 == 0:
                split_nodes.append(TextNode(section, TextType.TEXT))
            else:
                split_nodes.append(TextNode(section, text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(
            _split_links_in_text_node(
                node,
                extract_markdown_images,
                "![{:s}]({:s})",
                TextType.IMAGE
            )
        )

    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(
            _split_links_in_text_node(
                node,
                extract_markdown_links,
                "[{:s}]({:s})",
                TextType.LINK
            )
        )

    return new_nodes

def _split_links_in_text_node(node, extract_func, split_format, text_type):
    if node.text_type != TextType.TEXT:
        return [node]

    links = extract_func(node.text)
    if len(links) == 0:
        return [node]

    splits = []
    search_text = node.text
    for text, link in links:
        head, search_text = search_text.split(split_format.format(text, link), 1)
        splits.append(TextNode(head, TextType.TEXT))
        splits.append(TextNode(text, text_type, link))

    return splits

