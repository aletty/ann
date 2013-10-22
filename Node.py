class Node(object):
	def __init__(self):
		self.inputEdges = []
		raise NotImplementedError

	def addInputEdge(self, node):
		raise NotImplementedError

	def addOutputEdge(self, node):
		raise NotImplementedError

	def __call__(self):
		val = 0
		for edge in self.inputEdges
			val += edge.getVal()

		val = self.activationFunction(val)

	def activationFunction(val):
		raise NotImplementedError
