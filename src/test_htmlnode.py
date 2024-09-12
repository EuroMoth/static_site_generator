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
		self.assertEqual(node.props_to_html(), " href=\"Google.com\"")

	def test_leaf_node_eq(self):
		node = LeafNode("a", "click here", {"href": "google.com", "target": "_blank"})
		node2 = LeafNode("a", "click here", {"href": "google.com", "target": "_blank"})
		self.assertEqual(node, node2)

	def test_leaf_node_to_html(self):
		node = LeafNode("a", "click", {"href": "google.com", "target": "_blank"})
		html = node.to_html()
		self.assertEqual(html, "<a href=\"google.com\" target=\"_blank\">click</a>")

	def test_leaf_node_value(self):
		with self.assertRaises(ValueError):
			node = LeafNode("p", None, {"href": "yahoo.com", "target": "_blank"})
			html = node.to_html()

	def test_parent_recursion(self):
		node = ParentNode("div", [LeafNode("p", "hello!", None)], None)
		html = node.to_html()
		#print(f"\nlevel_one:{html}")
		self.assertEqual(html, "<div><p>hello!</p></div>")

	def test_parent_recursion_level_two(self):
		node = ParentNode("div", [LeafNode("p", "hello!", None), ParentNode("a", [LeafNode("b", "bold", None)], None)], None)
		html = node.to_html()
		#print(f"\nlevel_two:{html}")
		self.assertEqual(html, "<div><p>hello!</p><a><b>bold</b></a></div>")

	def test_parent_recursion_level_three(self):
		node = ParentNode("body",[ParentNode("article", [ParentNode("section", [LeafNode("p", "This is a paragraph", None), LeafNode("b", "BOLD", None)], {"test": "another test"}), LeafNode("span", "Spannin!", {"prop": "a prop"})], {"test_prop": "this-is-a-test"})], None)
		html = node.to_html()
		#print(f"\nlevel_three:{html}")
		self.assertEqual(html, "<body><article test_prop=\"this-is-a-test\"><section test=\"another test\"><p>This is a paragraph</p><b>BOLD</b></section><span prop=\"a prop\">Spannin!</span></article></body>")

	def test_parent_no_children(self):
		with self.assertRaises(ValueError):
			node = ParentNode("body", None, None)
			html = node.to_html()


if __name__ == "__main__":
	unittest.main()
