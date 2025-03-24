import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_parent_with_mixed_children(self):
        parent = ParentNode(
            "div",
            [
                LeafNode("h1", "Title"),
                ParentNode("section", [
                    LeafNode("p", "Paragraph 1"),
                    LeafNode("p", "Paragraph 2")
                ]),
                LeafNode("footer", "Page Footer")
            ]
        )
        expected = "<div><h1>Title</h1><section><p>Paragraph 1</p><p>Paragraph 2</p></section><footer>Page Footer</footer></div>"
        self.assertEqual(parent.to_html(), expected)
    
    def test_parent_with_props(self):
        parent = ParentNode(
            "nav", 
            [LeafNode("a", "Home")], 
            {"class": "navbar", "id": "main-nav"}
        )
        expected = '<nav class="navbar" id="main-nav"><a>Home</a></nav>'
        self.assertEqual(parent.to_html(), expected)

    def test_deeply_nested(self):
        nested = ParentNode(
            "ul",
            [
                ParentNode("li", [
                    ParentNode("ul", [
                        ParentNode("li", [
                            LeafNode("span", "Deeply nested")
                        ])
                    ])
                ])
            ]
        )
        expected = "<ul><li><ul><li><span>Deeply nested</span></li></ul></li></ul>"
        self.assertEqual(nested.to_html(), expected)
    
    def test_empty_children_list(self):
        parent = ParentNode("div", [])
        expected = "<div></div>"
        self.assertEqual(parent.to_html(), expected)
    
    def test_missing_tag_error(self):
        parent = ParentNode(None, [LeafNode("p", "Text")])
        with self.assertRaises(ValueError) as context:
            parent.to_html()
        
        self.assertEqual(str(context.exception), "ParentNode must have a tag")

    def test_missing_children_error(self):
        # Note: You'd normally not be able to create this state since the constructor requires children
        # This test would only make sense if someone manually sets children to None after creation
        parent = ParentNode("div", [])
        parent.children = None
        with self.assertRaises(ValueError) as context:
            parent.to_html()
    
        self.assertEqual(str(context.exception), "ParentNode must have children")
    
    def test_mixed_leaf_nodes(self):
        parent = ParentNode(
            "p",
            [
                LeafNode("strong", "Important"),
                LeafNode(None, " normal text "),
                LeafNode("em", "emphasized")
            ]
        )
        expected = "<p><strong>Important</strong> normal text <em>emphasized</em></p>"
        self.assertEqual(parent.to_html(), expected)
    
    def test_nested_props(self):
        parent = ParentNode(
            "form",
            [
                LeafNode("input", "", {"type": "text", "name": "username"}),
                LeafNode("input", "", {"type": "password", "name": "password"}),
                LeafNode("button", "Submit", {"type": "submit"})
            ],
            {"action": "/login", "method": "post"}
        )
        expected = '<form action="/login" method="post"><input type="text" name="username"></input><input type="password" name="password"></input><button type="submit">Submit</button></form>'
        self.assertEqual(parent.to_html(), expected)
    
    def test_special_characters(self):
        parent = ParentNode(
            "div",
            [
                LeafNode("p", "This is a paragraph with < and > symbols"),
                LeafNode("p", "This has quotes: \"quoted text\"")
            ]
        )
        expected = "<div><p>This is a paragraph with < and > symbols</p><p>This has quotes: \"quoted text\"</p></div>"
        self.assertEqual(parent.to_html(), expected)

if __name__ == '__main__':
    unittest.main()