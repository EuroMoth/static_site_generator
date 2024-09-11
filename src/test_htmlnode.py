import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
	def test_eq(self):
		node = HTMLNode("p", "hello")
		node2 = HTMLNode("p", "hello")
		self.assertEqual(node, node2)

	def test_not_eq(self):
		node = HTMLNode("p")
		node2 = HTMLNode()
		self.assertNotEqual(node, node2)

	def test_print(self):
		node = HTMLNode("a", "click here", None, {"href": "https://www.google.com", "target": "_blank"})
		if node.__repr__() == f"***\ntag: {node.tag}\nvalue: {node.value}\nchildren: {node.children}\nprops: {node.props}\n***":
			return  True
		else:
			return False

	def test_props_to_html(self):
		node = HTMLNode(None, None, None, {"href": "Google.com"})
		self.assertEqual(node.props_to_html(), " href=\"Google.com\" ")

	def test_leaf_node_eq(self):
		node = LeafNode("a", "click here", {"href": "google.com", "target": "_blank"})
		node2 = LeafNode("a", "click here", {"href": "google.com", "target": "_blank"})
		self.assertEqual(node, node2)

	def test_leaf_node_to_html(self):
		node = LeafNode("a", "click", {"href": "google.com", "target": "_blank"})
		html = node.to_html()
		self.assertEqual(html, "<a href=\"google.com\" target=\"_blank\" >click</a>")

	def test_leaf_node_value(self):
		with self.assertRaises(ValueError):
			node = LeafNode("p", None, {"href": "yahoo.com", "target": "_blank"})
			html = node.to_html()

	def test_parent_recursion(self):
		node = ParentNode("div", [LeafNode("p", "hello!", None)], None)
		html = node.to_html()
		self.assertEqual(html, "<div><p>hello!</p></div>")

	def test_parent_recursion_level_two(self):
		node = ParentNode("div", [LeafNode("p", "hello!", None), ParentNode("a", [LeafNode("b", "bold", None)], None)], None)
		html = node.to_html()
		print(html)
		#self.assertEqual(html, "<div><p>hello!</p></div>")

if __name__ == "__main__":
	unittest.main()
