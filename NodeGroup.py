from Node import Node

class NodeGroup(object):
	def __init__(self, size=0, NodeType=Node):
		self.nodes = list()
		self.size = size
		for i in xrange(size):
			self.addNode(NodeType())

		raise NotImplementedError

	def addNode(self, node):
		raise NotImplementedError