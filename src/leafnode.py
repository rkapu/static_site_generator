from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value

        starting_tag = f"<{self.tag}{self.props_to_html()}>"
        closing_tag = f"</{self.tag}>"

        return starting_tag + self.value + closing_tag

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
