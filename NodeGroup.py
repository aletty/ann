class NodeGroup(object):
	def __init__(self, size=0):
		self.nodes = list()
		self.size = size
		for i in xrange(size):
			self.addNode(Node())

		raise NotImplementedError

	def addNode(self, node):
		raise NotImplementedError