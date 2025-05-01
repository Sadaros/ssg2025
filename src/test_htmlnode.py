import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node: HTMLNode = HTMLNode("p", "This is text", None, None)
        node2 :HTMLNode = HTMLNode("p", "This is text", None, None)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node: HTMLNode = HTMLNode()
        node2: object = object()
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node: HTMLNode = HTMLNode("p", "1")
        node2: HTMLNode = HTMLNode("div", "2")
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node: HTMLNode = HTMLNode(None, None, None, {"href": "google.com", "target": "_blank"})
        props_text: str = node.props_to_html()
        expected_props_text: str = " href=\"google.com\" target=\"_blank\""
        self.assertEqual(props_text, expected_props_text)

    def test_props_to_html2(self):
        node: HTMLNode = HTMLNode("a", "link to google", None, {"href": "www.google.com"})
        props_text: str = node.props_to_html()
        expected_props_text: str = " href=\"www.google.com\""
        self.assertEqual(props_text, expected_props_text)

class TestLeafNode(unittest.TestCase):
    def test_props_empty(self):
        node: LeafNode = LeafNode(None, "no props")
        test_case: str = ""
        self.assertEqual(node.props_to_html(), test_case)

    def test_to_html(self):
        node: LeafNode = LeafNode("h1", "TestString", {"class": "heading"})
        test_case: str = '<h1 class="heading">TestString</h1>'
        self.assertEqual(node.to_html(), test_case)

    def test_to_html_exception(self):
        node: Leafnode = LeafNode(None) # type: ignore
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_no_props(self):
        node: LeafNode = LeafNode("p", "No props")
        test_case: str = "<p>No props</p>"
        self.assertEqual(node.to_html(), test_case)

    def test_to_html_no_tag(self):
        node: LeafNode = LeafNode(None, "No tags")
        test_case: str = "No tags"
        self.assertEqual(node.to_html(), test_case)

    def test_to_html_html_escape(self):
        node: LeafNode = LeafNode("p", "2 > \" '1 & 3 < 4")
        test_case: str = "<p>2 &gt; &quot; &#x27;1 &amp; 3 &lt; 4</p>"
        self.assertEqual(node.to_html(), test_case)

    def test_to_html_html_escape_no_tag(self):
        node: LeafNode = LeafNode(None, "2 > 1")
        test_case: str = "2 &gt; 1"
        self.assertEqual(node.to_html(), test_case)

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )