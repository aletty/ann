import warnings
from NodeGroup import *

class FeedForward(object):
	def __init__(self, size):
		self.layers = []

		for width in size:
			self.layers.append(NodeGroup(width))


	def fullConnect():
		for index, layer in enumerate(self.layers[:-1])
			for node in layer:
				for nextNode in layer[index+1]:
					node.addEdge(nextNode)

	def __call__(self,input):
		raise NotImplementedError