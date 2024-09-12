import unittest

from textnode import TextNode
from htmlnode import *
from main import text_node_to_html_node

class TestNodeConversion(unittest.TestCase):
	def test_text_type_text(self):
		node = TextNode("Hello World!", "text", None)
		#print(f"***{node.text}***")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node, "Hello World!")

	def test_text_type_bold(self):
		node = TextNode("Hello World!", "bold", None)
		#print(f"***{node.text}***")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node, "<b>Hello World!</b>")

	def test_text_type_italic(self):
		node = TextNode("Hello World!", "italic", None)
		#print(f"***{node.text}***")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node, "<i>Hello World!</i>")

	def test_text_type_code(self):
		node = TextNode("Hello World!", "code", None)
		#print(f"***{node.text}***")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node, "<code>Hello World!</code>")

	def test_text_type_link(self):
		node = TextNode("Hello World!", "link", "Google.com")
		#print(f"***{node.text}***")
		html_node = text_node_to_html_node(node)
		#print(f"***{html_node}***")
		self.assertEqual(html_node, "<a href=\"Google.com\">Hello World!</a>")

	def test_text_type_image(self):
		node = TextNode("Hello World!", "image", "Google.com")
		#print(f"***{node.text}***")
		html_node = text_node_to_html_node(node)
		#print(f"***{html_node}***")
		self.assertEqual(html_node, "<img src=\"Google.com\" alt=\"Hello World!\"></img>")

	def test_text_type_invalid_text(self):
		with self.assertRaises(Exception):
			node = TextNode("Text", "Grog", "Goog.com")
			html_node = text_node_to_html_node(node)
			print(html_node)
