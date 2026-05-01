import unittest

from textnode import *
from htmlnode import *
from function.textnode_to_html import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        test_node = LeafNode("b", "important")
        text_node = TextNode("important", TextType.BOLD)

        self.assertEqual(test_node.to_html(), text_node_to_html_node(text_node).to_html())

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("code something", TextType.LINK, "https://www.boot.dev/")
        self.assertEqual(
            text_node_to_html_node(node).to_html(),
            '<a href="https://www.boot.dev/">code something</a>',
        )

if __name__ == "__main__":
    unittest.main()
