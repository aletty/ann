from Node import Node
class InputNode(Node):
	def __init__(self):
		super(InputNode,self).__init__()

	def __call__(self):
		return val

	def load(self,val):
		self.val = val

	def addInputEdge(self):
		raise AttributeError('Input nodes only accept data via the load() method, they do not support input edges')