#Create the Network
#Feed-Forward

#create a 3 layer feedforward network with 6 neurons in each layer
#create the node structure
network = FeedForward([6]*3)
#create the edge structure
network.fullConnect()