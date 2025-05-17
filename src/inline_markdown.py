import re
from typing import Sequence

from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: Sequence[TextNode], delimiter: str, text_type: TextType
) -> Sequence[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError(f"{node} does not contain matching delimiter: {delimiter}")

        sub_list: list[TextNode] = []
        for index, word in enumerate(split_text):
            if word == "":
                continue
            if index % 2 == 0:
                sub_list.append(TextNode(word, TextType.TEXT))
            else:
                sub_list.append(TextNode(word, text_type))
        new_nodes.extend(sub_list)
    return new_nodes


def extract_markdown_images(text: str) -> list[tuple]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str) -> list[tuple]:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
