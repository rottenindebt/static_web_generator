import unittest

from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_raises(self):
        node = HtmlNode()
        self.assertRaises(NotImplementedError, node.to_html)

    def test_promt_void(self):
        node = HtmlNode()
        self.assertEqual(node.props_to_html(), "")

    def test_promt_expeted_behavior(self):
        node = HtmlNode(
            props={
                "href": "https://www.boot.dev/",
                "img": "./img/pakitasalas.png",
            },
        )
        self.assertEqual(
            node.props_to_html(),
            " href=https://www.boot.dev/ img=./img/pakitasalas.png",
        )
