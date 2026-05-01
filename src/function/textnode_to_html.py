
from textnode import *
from htmlnode import *


def text_node_to_html_node(node: TextNode):
    match node.text_type.value:
        case "text":
            return LeafNode(None, node.text)
        case "bold":
            return LeafNode("b", node.text)
        case "italic":
            return LeafNode("i", node.text)
        case "code":
            return LeafNode("code", node.text)
        case "link":
            return LeafNode("a", node.text, { "href": node.url })
        case "imagen":
            return LeafNode("img", "", {
                "alt": node.text,
                "src": node.url,
            })
        case _:
            raise ValueError("Unknown type")
