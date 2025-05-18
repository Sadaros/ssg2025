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


def split_nodes_image(old_nodes: Sequence[TextNode]) -> Sequence[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text == "":
            continue
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        sub_list: list[TextNode] = []

        for image in images:
            extracted_text = node.text.split(f"![{image[0]}]({image[1]})", 1)
            node.text = extracted_text[1]
            sub_list.append(TextNode(extracted_text[0], TextType.TEXT))
            sub_list.append(TextNode(image[1], TextType.IMAGE, image[1]))
        if node.text != "":
            sub_list.append(TextNode(node.text, TextType.TEXT))
        new_nodes.extend(sub_list)

    return new_nodes


def split_nodes_link(old_nodes: Sequence[TextNode]) -> Sequence[TextNode]: ...


def extract_markdown_images(text: str) -> list[tuple]:
    return re.findall(r"!\[(.*?)]\((.*?)\)", text)


def extract_markdown_links(text: str) -> list[tuple]:
    return re.findall(r"\[(.*?)]\((.*?)\)", text)
