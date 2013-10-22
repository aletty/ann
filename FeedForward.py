import warnings
from NodeGroup import *

class FeedForward(object):
	def __init__(self, size):
		self.layers = [InputNodeGroup(size[0])]

		for width[1:] in size:
			self.layers.append(NodeGroup(width=width))


	def fullConnect():
		#connect each node to ever node in the next layer
		for index, layer in enumerate(self.layers[:-1])
			for node in layer:
				for nextNode in layer[index+1]:
					node.addEdge(nextNode)

	def __call__(self,input):
		raise NotImplementedError