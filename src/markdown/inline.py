import re
from .textnode import *

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

def split_nodes_image(old_nodes):
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

def split_nodes_link(old_nodes):
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

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes

# Private functions

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
        if head != "":
            splits.append(TextNode(head, TextType.TEXT))
        splits.append(TextNode(text, text_type, link))

    if search_text != "":
        splits.append(TextNode(search_text, TextType.TEXT))

    return splits
