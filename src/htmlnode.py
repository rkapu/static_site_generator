class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""

        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'

        return result

    def __repr__(self):
        if self.children:
            children_str = f"{len(self.children)} children"
        else:
            children_str = self.children

        return f"HTMLNode({self.tag}, {self.value}, {children_str}, {self.props})"

    def opening_tag(self):
        if self.tag is None:
            return ""

        return f"<{self.tag}{self.props_to_html()}>"

    def closing_tag(self):
        if self.tag is None:
            return ""

        return f"</{self.tag}>"
