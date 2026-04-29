import unittest

from htmlnode import HtmlNode, LeafNode, ParentNode

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

    def test_leaf_node(self):
        leaf = LeafNode("li", "TODO one more unittest")
        leaf2 = LeafNode("li", "TODO one more unittest")
        leaf3 = LeafNode("li", "END this class", { "color": "#1e1e1e" })

        self.assertEqual(leaf, leaf2)
        self.assertNotEqual(leaf, leaf3)

    def test_leaf_prompt(self):
        leaf = LeafNode("b", "IMPORTANT", { "color": "red" })
        leaf2 = LeafNode("li", "END this class", { "color": "#1e1e1e" })

        self.assertNotEqual(leaf.to_html(), leaf2.to_html())
        self.assertTrue(isinstance(leaf2.to_html(), str))

    def test_leaf_eq(self):
        leaf = LeafNode("b", "IMPORTANT", { "color": "red", "font": "iosevka" })
        self.assertEqual(leaf.to_html(), "<b color=red font=iosevka>IMPORTANT</b>")

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
        

    def test_parent_error(self):
        child_node = LeafNode(None, "IMPORTANT")
        parent_node = ParentNode("p", [child_node])

        self.assertRaises(ValueError, parent_node.to_html)
