from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        
        return (self.text == other.text and 
            self.text_type == other.text_type and 
            self.url == other.url)

    def __repr__(self):
        text_type_str = self.text_type.value
        return f"TextNode({self.text}, {text_type_str}, {self.url})"
    
    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextType.TEXT:
                return LeafNode(tag=None, value=text_node.text)
            case TextType.BOLD:
                return LeafNode(tag="b", value=text_node.text)
            case TextType.ITALIC:
                return LeafNode(tag="i", value=text_node.text)
            case TextType.CODE:
                return LeafNode(tag="code", value=text_node.text)
            case TextType.LINK:
                return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
            case TextType.IMAGE:
                props_dict = {
                    "src": text_node.url,
                    "alt": text_node.text
                }
                return LeafNode(tag="img", value="", props=props_dict)
            case _:
                raise Exception("Invalid text type")
