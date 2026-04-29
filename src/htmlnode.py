
class HtmlNode():
    def __init__(self, tag: str | None = None, value: str | None = None, children: list | None = None, props: dict | None = None):
        self.tag = tag # a string for the html tag e, p, h1, etc..
        self.value = value # whats inside the tag like the usual string
        self.children = children # a list of children nodes
        self.props = props # a key-value pair like href and a url

    def to_html(self) -> str:
        raise NotImplementedError("NOT IMPLEMENTED, YET...")

    def props_to_html(self) -> str:
        form = ""
        if self.props != None:
            for pair in self.props:
                form += f" {pair}={self.props[pair]}"
        return form

    def __eq__(self, other):
        return (self.tag == other.tag
                and self.children == other.children
                and self.value == other.value
                and self.props == other.props)

    def __repr__(self) -> str:
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"


    
class LeafNode(HtmlNode):
    def __init__(self, tag: str, value: str, props: dict | None = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self) -> str:
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self) -> str:
        return f"HtmlNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HtmlNode):
    def __init__(self, tag: str, children: list, props: dict | None = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("parentnode missing tag")
        value = f"<{self.tag}>"
        for node in self.children:
            if not node.tag:
                raise ValueError(f"missing TAG in {node}")
            if not (node.value or node.children):
                raise ValueError(f"missing VALUE of CHILD in {node}")
            value += node.to_html()
        return value + f"</{self.tag}>"

    def __repr__(self) -> str:
        return f"HtmlNode({self.tag}, {self.children}, {self.props})"
    
