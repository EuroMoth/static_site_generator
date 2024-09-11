class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError

	def is_parent(self):
		raise NotImplementedError

	def props_to_html(self):
		prop_string = " "
		for key, value in self.props.items():
			prop_string += f"{key}=\"{value}\" "
		return prop_string

	def __eq__(self, other):
		if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
			return True
		else:
			return False

	def __repr__(self):
		return f"***\ntag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}\n***"

class LeafNode(HTMLNode):
	def __init__(self, tag, value, props):
		super().__init__(tag, value, None, props)

	def is_parent(self):
		return False

	def to_html(self):
		if self.value == None:
			raise ValueError

		if self.tag == None:
			return f"{value}"

		if self.props == None:
			props_string = ""
		else:
			props_string = self.props_to_html()

		return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props):
		super().__init__(tag, None, children, props)

	def is_parent(self):
		return True

	def to_html(self):
		if self.tag == None:
			raise ValueError("Object must have tag")

		if self.children == None:
			raise ValueError("Object must have children")
		else:
			for child in self.children:
				if not child.is_parent():
					if child.props == None:
						print("OptionA")
						return f"<{self.tag}>{child.to_html()}</{self.tag}>"
					else:
						print("OptionB")
						return f"<{self.tag}{child.props_to_html()}>{child.to_html()}</{self.tag}>"
				else:
					child.to_html()
