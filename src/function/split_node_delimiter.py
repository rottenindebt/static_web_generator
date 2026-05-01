from htmlnode import *
from textnode import *

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: TextType) -> list:
    for node in old_nodes:
