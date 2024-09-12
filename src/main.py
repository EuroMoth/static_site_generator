from textnode import TextNode
from htmlnode import *


def text_node_to_html_node(text_node):
	acceptable_text_types = ("text", "bold", "italic", "code", "link", "image")

	if text_node.text_type not in acceptable_text_types:
		raise Exception("Text type not supported")

	if text_node.text_type == "text":
		html_node = LeafNode(None, text_node.text, None)

	if text_node.text_type == "bold":
		html_node = LeafNode("b", text_node.text, None)

	if text_node.text_type == "italic":
		html_node = LeafNode("i", text_node.text, None)

	if text_node.text_type == "code":
		html_node = LeafNode("code", text_node.text, None)

	if text_node.text_type == "link":
		html_node = LeafNode("a", text_node.text, {"href": text_node.url})

	if text_node.text_type == "image":
		html_node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

	#print(html_node.to_html())
	return html_node.to_html()


def main():
	text_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
	html_node = text_node_to_html_node(text_node)
	#print(text_node.__repr__())

main()
