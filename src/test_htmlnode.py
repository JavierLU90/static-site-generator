import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_valid_props(self):
        node = HTMLNode(props={"class": "btn", "id": "submit-button"})
        result = node.props_to_html()
        self.assertEqual(result, ' class="btn" id="submit-button"')
    
    def test_props_to_html_with_no_props(self):
        node = HTMLNode(props=None)
        result = node.props_to_html()
        self.assertIsNone(result)

    def test_props_to_html_with_empty_props(self):
        node = HTMLNode(props={})
        result = node.props_to_html()
        self.assertEqual(result, '')

    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={"class": "container"})
        result = repr(node)
        self.assertEqual(result, 'HTMLNode(div, Hello, [], {\'class\': \'container\'})')
    
    def test_node_with_children(self):
        child_node = HTMLNode(tag="span", value="Child")
        parent_node = HTMLNode(tag="div", children=[child_node])
        result = repr(parent_node)
        self.assertTrue("HTMLNode(span, Child" in result)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Content in a div")
        self.assertEqual(node.to_html(), "<div>Content in a div</div>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click here", {"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://example.com" target="_blank">Click here</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_leaf_to_html_empty_props(self):
        node = LeafNode("span", "Text with empty props", {})
        self.assertEqual(node.to_html(), "<span>Text with empty props</span>")

    def test_leaf_to_html_raises_value_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == '__main__':
    unittest.main()