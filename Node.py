from Edge import Edge
from math import tanh as tanh

class Node(object):
	def __init__(self):
		self.inputEdges = []
		self.outputEdges = []

	def addInputEdge(self, edge):
		self.inputEdges.append(edge)

	def addOutputEdge(self, edge):
		self.outputEdges.append(edge)

	def __call__(self):
		val = 0
		for edge in self.inputEdges
			val += edge.getVal()

		val = self.activationFunction(val)

	def activationFunction(val):
		return (tanh(val)+1)/2
