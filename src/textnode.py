from enum import Enum
from typing import Optional

from src.htmlnode import LeafNode


class TextType(Enum):
    TEXT = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    final_node: Optional[LeafNode] = None
    match text_node.text_type:
        case TextType.TEXT:
            final_node = LeafNode(None, text_node.text)
        case TextType.BOLD:
            final_node = LeafNode("b", text_node.text)
        case TextType.ITALIC:
            final_node = LeafNode("i", text_node.text)
        case TextType.CODE:
            final_node = LeafNode("code", text_node.text)
        case TextType.LINK:
            final_node = LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            final_node = LeafNode(
                "img", "", {"src": text_node.url, "alt": text_node.text}
            )

    return final_node
