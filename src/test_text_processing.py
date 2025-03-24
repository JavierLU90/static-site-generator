import unittest
from textnode import TextNode, TextType
from text_processing import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_with_code_delimiter(self):
        # Test code delimiter with backticks
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual(3, len(new_nodes))
        self.assertEqual("This is text with a ", new_nodes[0].text)
        self.assertEqual(TextType.TEXT, new_nodes[0].text_type)
        self.assertEqual("code block", new_nodes[1].text)
        self.assertEqual(TextType.CODE, new_nodes[1].text_type)
        self.assertEqual(" word", new_nodes[2].text)
        self.assertEqual(TextType.TEXT, new_nodes[2].text_type)
    
    def test_split_with_bold_delimiter(self):
        # Test bold delimiter with double asterisks
        node = TextNode("This is **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        self.assertEqual(3, len(new_nodes))
        self.assertEqual("This is ", new_nodes[0].text)
        self.assertEqual("bold", new_nodes[1].text)
        self.assertEqual(TextType.BOLD, new_nodes[1].text_type)
        self.assertEqual(" text", new_nodes[2].text)
    
    def test_split_with_text_starting_with_delimiter(self):
        # Test text that starts with a delimiter
        node = TextNode("**Bold** at start", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        self.assertEqual(2, len(new_nodes))
        self.assertEqual("Bold", new_nodes[0].text)
        self.assertEqual(TextType.BOLD, new_nodes[0].text_type)
        self.assertEqual(" at start", new_nodes[1].text)
        self.assertEqual(TextType.TEXT, new_nodes[1].text_type)

    def test_split_with_text_ending_with_delimiter(self):
        # Test text that ends with a delimiter
        node = TextNode("End with **Bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        self.assertEqual(2, len(new_nodes))
        self.assertEqual("End with ", new_nodes[0].text)
        self.assertEqual(TextType.TEXT, new_nodes[0].text_type)
        self.assertEqual("Bold", new_nodes[1].text)
        self.assertEqual(TextType.BOLD, new_nodes[1].text_type)

    def test_split_with_multiple_delimiters(self):
        # Test text with multiple occurrences of the delimiter
        node = TextNode("This has **multiple** bold **words**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        self.assertEqual(4, len(new_nodes))
        self.assertEqual("This has ", new_nodes[0].text)
        self.assertEqual("multiple", new_nodes[1].text)
        self.assertEqual(TextType.BOLD, new_nodes[1].text_type)
        self.assertEqual(" bold ", new_nodes[2].text)
        self.assertEqual("words", new_nodes[3].text)
        self.assertEqual(TextType.BOLD, new_nodes[3].text_type)

    def test_split_with_italic_delimiter(self):
        # Test italic delimiter with underscore
        node = TextNode("This is _italic_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        
        self.assertEqual(3, len(new_nodes))
        self.assertEqual("This is ", new_nodes[0].text)
        self.assertEqual("italic", new_nodes[1].text)
        self.assertEqual(TextType.ITALIC, new_nodes[1].text_type)
        self.assertEqual(" text", new_nodes[2].text)
        self.assertEqual(TextType.TEXT, new_nodes[2].text_type)

    def test_with_non_text_node(self):
        # Test that non-TEXT nodes are passed through unchanged
        node = TextNode("already bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        self.assertEqual(1, len(new_nodes))
        self.assertEqual("already bold", new_nodes[0].text)
        self.assertEqual(TextType.BOLD, new_nodes[0].text_type)

    def test_with_multiple_nodes(self):
        # Test with a list containing multiple nodes
        node1 = TextNode("Text with **bold**", TextType.TEXT)
        node2 = TextNode("More text", TextType.TEXT)
        node3 = TextNode("Already italic", TextType.ITALIC)
        
        new_nodes = split_nodes_delimiter([node1, node2, node3], "**", TextType.BOLD)
        
        self.assertEqual(4, len(new_nodes))
        self.assertEqual("Text with ", new_nodes[0].text)
        self.assertEqual("bold", new_nodes[1].text)
        self.assertEqual(TextType.BOLD, new_nodes[1].text_type)
        # Note: We're not expecting an empty string node here anymore
        self.assertEqual("More text", new_nodes[2].text)
        self.assertEqual("Already italic", new_nodes[3].text)
        self.assertEqual(TextType.ITALIC, new_nodes[3].text_type)

    def test_unclosed_delimiter(self):
        # Test with unclosed delimiter which should raise an exception
        node = TextNode("This has an **unclosed delimiter", TextType.TEXT)
        
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

if __name__ == "__main__":
    unittest.main()