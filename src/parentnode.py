from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Should have tag")
        if self.children is None:
            raise ValueError("Should have children")

        result = ""
        for child in self.children:
            result += child.to_html()

        return self.opening_tag() + result + self.closing_tag()
