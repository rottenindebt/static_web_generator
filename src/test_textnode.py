import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_inequality(self):
        node = TextNode("just do some code", TextType.LINK, "https://www.boot.dev/")
        node2 = TextNode("just do some code", TextType.LINK, "https://www.boot.dev/")
        node3 = TextNode("tomorrow", TextType.TEXT)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)

    def test_type(self):
        node = TextNode("just do some code", TextType.LINK, "https://www.boot.dev/")
        node2 = TextNode("just do some code", TextType.IMAGEN, "https://www.boot.dev/")
        node3 = TextNode("_now kiss_", TextType.ITALIC)
        node4 = TextNode("_now kiss_", TextType.ITALIC)
        self.assertNotEqual(node, node2)
        self.assertEqual(node3, node4)


if __name__ == "__main__":
    unittest.main()
