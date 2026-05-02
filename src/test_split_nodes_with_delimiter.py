import unittest

from htmlnode import *
from textnode import *
from function.split_node_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_split_with_single_delimiter(self):
        """Test splitting text with one delimiter"""
        nodes = [TextNode("hello **bold** world", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD) 
        
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "hello ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " world")
        self.assertEqual(result[2].text_type, TextType.TEXT)
    
    def test_split_with_multiple_delimiters(self):
        """Test splitting text with multiple delimiters"""
        nodes = [TextNode("a **b** c **d** e", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].text, "a ")
        self.assertEqual(result[1].text, "b")
        self.assertEqual(result[2].text, " c ")
        self.assertEqual(result[3].text, "d")
        self.assertEqual(result[4].text, " e")
    
    def test_no_delimiter_found(self):
        """Test when delimiter is not present in text"""
        nodes = [TextNode("hello world", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "hello world")
        self.assertEqual(result[0].text_type, TextType.TEXT)
    
    def test_non_text_nodes_pass_through(self):
        """Test that non-text nodes pass through unchanged"""
        nodes = [TextNode("bold", TextType.BOLD)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "bold")
        self.assertEqual(result[0].text_type, TextType.BOLD)
    
    def test_mixed_text_and_non_text_nodes(self):
        """Test processing with both text and non-text nodes"""
        nodes = [
            TextNode("hello **bold**", TextType.TEXT),
            TextNode("already bold", TextType.BOLD),
            TextNode("more **text**", TextType.TEXT)
        ]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].text, "hello ")
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[2].text_type, TextType.BOLD)
        self.assertNotEqual(result[2].text, "")
        self.assertEqual(result[2].text, "already bold")
        self.assertEqual(result[3].text_type, TextType.TEXT)
        self.assertEqual(result[3].text, "more ")
        self.assertEqual(result[4].text, "text")
        self.assertEqual(result[4].text_type, TextType.BOLD)

        
    def test_empty_string(self):
        """Test with empty text"""
        nodes = [TextNode("", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        
        self.assertEqual(len(result), 0)
    
    def test_consecutive_delimiters(self):
        """Test with consecutive delimiters (empty bold text)"""
        nodes = [TextNode("hello **** world", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        
        # Should create: "hello ", "", " world"
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "hello ")
        self.assertEqual(result[1].text, " world")
    
    def test_different_text_types(self):
        """Test with different text type variations"""
        nodes = [TextNode("hello _italic_ world", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        
        self.assertEqual(result[1].text_type, TextType.ITALIC)
    
    def test_delimiter_at_start(self):
        """Test when text starts with delimiter"""
        nodes = [TextNode("**bold** text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        
        self.assertEqual(len(result), 2)
        self.assertNotEqual(result[0].text, "")
        self.assertEqual(result[0].text, "bold")
        self.assertEqual(result[1].text, " text")


if __name__ == "__main__":
    unittest.main()
