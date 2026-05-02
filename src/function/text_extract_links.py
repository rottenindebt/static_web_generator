import re

def extract_markdown_images(text: str) -> list:
    rs = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return rs



def extract_markdown_links(text: str) -> list:
    rs = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return rs
