from Node import Node

class Edge(object):
	def __init__(self, nodeIn, nodeOut, weight=.1):
		self.nodeIn = nodeIn
		self.nodeOut = nodeOut
		self.weight = weight

	def setWeight(self,w):
		self.weight = w

	def getVal(self):
		self.nodeIn()*self.weight