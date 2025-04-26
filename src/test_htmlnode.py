import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node: HTMLNode = HTMLNode(None, None, None, {"href": "google.com", "target": "_blank"})
        props_text: str = node.props_to_html()
        expected_props_text: str = " href=\"google.com\" target=\"_blank\""
        self.assertEqual(props_text, expected_props_text)

    def test_props_to_html2(self):
        node: HTMLNode = HTMLNode("a", "link to google", None, {"href": "www.google.com"})
        props_text: str = node.props_to_html()
        expected_props_text: str = " href=\"www.google.com\""
