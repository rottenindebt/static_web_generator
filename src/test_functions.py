import unittest

from textnode import *
from htmlnode import *
from function.textnode_to_html import text_node_to_html_node
from function.split_node_delimiter import split_nodes_delimiter
from function.text_extract_links import extract_markdown_images, extract_markdown_links


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


    #funtions for extract links in markdown files
    def test_images(self):
        text = "you can see how cute is my rocky ![A dog sleeping](./'my dog sleeping'.png) ![my dog running](./'dog_running'.png)"
        image1 = ("A dog sleeping", "./'my dog sleeping'.png")
        image2 = ("my dog running", "./'dog_running'.png")
        list_of_images = extract_markdown_images(text)

        self.assertEqual(list_of_images[0], image1)
        self.assertEqual(list_of_images[1], image2)

    def test_links(self):
        text = "you can see images of this doggo ![rocky balboa](./cutest_dog.png) </br> in my website [ramdon](www.ramdon.es)"
        images = extract_markdown_images(text)
        url = extract_markdown_links(text)

        self.assertTrue((len(images) == 1) and (len(url) == 1))
        self.assertTrue(("ramdon", "www.ramdon.es") in url)

if __name__ == "__main__":
    unittest.main()
