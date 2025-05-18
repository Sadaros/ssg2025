import unittest
from textnode import TextNode, TextType
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images,
)


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic_functionality(self):
        node = TextNode("This is a `code block` here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            result,
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" here", TextType.TEXT),
            ],
        )

    def test_no_delimiter(self):
        node = TextNode("This is a regular text.", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.TEXT)
        self.assertEqual(node, result[0])

    def test_multiple_same_delimiters(self):
        node = TextNode("Start `code1` middle `code2` end", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            result,
            [
                TextNode("Start ", TextType.TEXT),
                TextNode("code1", TextType.CODE),
                TextNode(" middle ", TextType.TEXT),
                TextNode("code2", TextType.CODE),
                TextNode(" end", TextType.TEXT),
            ],
        )

    def test_unmatched_delimiter(self):
        node = TextNode("This is `unmatched delimiter", TextType.TEXT)
        with self.assertRaises(ValueError):
            result = split_nodes_delimiter([node], "`", TextType.CODE)


class TestMarkdownLinkImageExtractor(unittest.TestCase):
    def test_valid_link(self):
        link_tuple = extract_markdown_links(
            "This is a string, with a [link](google.com) in it"
        )
        result = [("link", "google.com")]
        self.assertEqual(link_tuple, result)

    def test_multiple_links(self):
        link_tuple = extract_markdown_links(
            "first [link](google.com), second [link2](yahoo.com)"
        )
        result = [("link", "google.com"), ("link2", "yahoo.com")]
        self.assertEqual(link_tuple, result)

    def test_valid_image(self):
        image_tuple = extract_markdown_images(
            "This is a string with an ![image](logo.png)"
        )
        result = [("image", "logo.png")]
        self.assertEqual(image_tuple, result)

    def test_multiple_images(self):
        image_tuple = extract_markdown_images(
            "first ![image1](picture1.png) second ![image2](picture2.jpeg) trailing string"
        )
        result = [("image1", "picture1.png"), ("image2", "picture2.jpeg")]
        self.assertEqual(image_tuple, result)

    def test_invalid_image(self):
        test_case = extract_markdown_images("String with no image")
        result = []
        self.assertEqual(test_case, result)

    def test_invalid_link(self):
        test_case = extract_markdown_links("String with no image")
        result = []
        self.assertEqual(test_case, result)
