import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node: TextNode = TextNode("This is the text", TextType.NORMAL_TEXT)
        node2: TextNode = TextNode("This is the text", TextType.NORMAL_TEXT)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node: TextNode = TextNode("Texting typing", TextType.BOLD_TEXT, "home.com")
        node2: TextNode = TextNode("Texting typing", TextType.BOLD_TEXT, "home.com")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node: TextNode = TextNode("This is text one", TextType.NORMAL_TEXT)
        node2: TextNode = TextNode("This is some other text", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
