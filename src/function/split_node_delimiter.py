from htmlnode import *
from textnode import *
from function.text_extract_links import *

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: TextType) -> list:
    rs = []
    
    for node in old_nodes:
        if node.text_type.value != "text":
            rs.append(node)
            continue

        space = node.text.split(delimiter)
        for index, x in enumerate(space):
            if x:
                new_node = TextNode(x, text_type if index % 2 == 1 else TextType.TEXT)
                rs.append(new_node)
        
    return rs
                    
                
def split_nodes_image(old_nodes: list) -> list:
    rs = []

    for node in old_nodes:
        if node.text_type.value != "text":
            rs.append(node)
            continue

        images = extract_markdown_images(node.text)
        if not images:
            rs.append(node)
            continue
            
        text_node = node.text
        
        for imagen in images:
            node_split = text_node.split(f"![{imagen[0]}]({imagen[1]})", 1)
            text_node = node_split[1]
            
            if node_split[0]:
                rs.append(TextNode(node_split[0], TextType.TEXT))
                
            rs.append(TextNode(imagen[0], TextType.IMAGEN, imagen[1]))
            
        if text_node:
            rs.append(TextNode(text_node, TextType.TEXT))
            
            
    return rs


def split_nodes_url(old_nodes: list) -> list:
    rs = []

    for node in old_nodes:
        if node.text_type.value != "text":
            rs.append(node)
            continue

        links = extract_markdown_links(node.text)
        if not links:
            rs.append(node)
            continue
            
        text_node = node.text
        
        for link in links:
            node_split = text_node.split(f"[{link[0]}]({link[1]})", 1)
            text_node = node_split[1]
            
            if node_split[0]:
                rs.append(TextNode(node_split[0], TextType.TEXT))
                
            rs.append(TextNode(link[0], TextType.LINK, link[1]))
            
        if text_node:
            rs.append(TextNode(text_node, TextType.TEXT))
            
            
    return rs
