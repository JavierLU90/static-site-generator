class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
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
