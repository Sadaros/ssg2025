from typing import Optional, Sequence

import html



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

    def to_html(self) -> str:
        raise NotImplementedError("Use a ParentNode or a LeafNode")

    def props_to_html(self) -> str:
        if self.props is None or not self.props:
            return ""

        props_string: str = ""

        for k, v in self.props.items():
            props_string += f' {k}="{html.escape(v)}"'

        return props_string

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )

class LeafNode(HTMLNode):

    def __init__(
            self,
            tag: Optional[str] = None,
            value: Optional[str] = None,
            props: Optional[dict[str, str]] = None
    ):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None or not self.value:
            raise ValueError("All LeafNodes must have a value.")
        if not self.tag:
            result = html.escape(self.value)
        else:
            result = f"<{self.tag}{self.props_to_html()}>{html.escape(self.value)}</{self.tag}>"
        return result

class ParentNode(HTMLNode):

    def __init__(
            self,
            tag: Optional[str] = None,
            children: Optional[Sequence[HTMLNode]] = None,
            props: Optional[dict[str, str]] = None
    ):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("All ParentNode must have a tag")
        if not self.children:
            raise ValueError("All ParentNode must have children")

        result: list[str] = [f"<{self.tag}{self.props_to_html()}>"]

        for node in self.children:
            result.append(node.to_html())

        result.append(f"</{self.tag}>")

        result_string: str = "".join(result)
        return result_string