from InputNode import InputNode

class InputNodeGroup(NodeGroup):
	def __init__(self,size=0):
		super(InputNodeGroup, self).__init__(size=size, NodeType=InputNode)