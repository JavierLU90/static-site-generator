import unittest
from htmlnode import HTMLNode

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

if __name__ == '__main__':
    unittest.main()