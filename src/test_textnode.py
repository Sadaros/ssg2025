import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node: TextNode = TextNode("This is the text", TextType.TEXT)
        node2: TextNode = TextNode("This is the text", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node: TextNode = TextNode("Texting typing", TextType.BOLD, "home.com")
        node2: TextNode = TextNode("Texting typing", TextType.BOLD, "home.com")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node: TextNode = TextNode("This is text one", TextType.TEXT)
        node2: TextNode = TextNode("This is some other text", TextType.BOLD)
        self.assertNotEqual(node, node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()
