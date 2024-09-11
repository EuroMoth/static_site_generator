import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_two(self):
        node = TextNode("abc", "italic")
        node2 = TextNode("abc", "italic")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Hello World!", "bold",  "google.com")
        node2 = TextNode("Hi World!", "bold", "google.com")
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("Google", "italic", "google.com")
        node2 = TextNode("Google", "italic", None)
        self.assertNotEqual(node.url, node2.url)

if __name__ == "__main__":
    unittest.main()
