from typing import Optional, Sequence


class HTMLNode:

    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[Sequence["HTMLNode"]] = None,
        props: Optional[dict[str, str]] = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Use a ParentNode or a LeafNode")

    def props_to_html(self) -> str:
        if self.props is None or not self.props:
            return ""

        props_string: str = ""

        for k, v in self.props.items():
            props_string += f' {k}="{v}"'

        return props_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"