class HtmlNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # a string for the html tag e, p, h1, etc..
        self.value = value # whats inside the tag like the usual string
        self.children = children # a list of children nodes
        self.props = props # a key-value pair like href and a url

    def to_html(self):
        raise NotImplementedError("NOT IMPLEMENTED, YET...")

    def props_to_html(self):
        form = ""
        if self.props != None:
            for pair in self.props:
                form += f" {pair}={self.props[pair]}"
        return form

    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"


    
class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.props})"
