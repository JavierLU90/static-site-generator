class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:  # Specifically handle None
            return None
        if self.props:  # Handles non-empty dictionaries
            string = ""
            for key, value in self.props.items():
                string += f' {key}="{value}"'
            return string
        return ''  # Handles empty dictionaries
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        
        if self.tag is None:
            return self.value
        
        props_string = self.props_to_html()
        if props_string is None:
            props_string = ''
        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, "", children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        
        if self.children is None:
            raise ValueError("ParentNode must have children")
        
        props_html = self.props_to_html()
        if props_html is None:
            props_html = ''
        opening_tag = f"<{self.tag}{props_html}>"
        closing_tag = f"</{self.tag}>"

        html_content = ""
        for child in self.children:
            html_content += child.to_html()
        return opening_tag + html_content + closing_tag
