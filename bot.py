# -*- coding: utf-8 -*-
# Bot to play 7 Wonders
import torch 
import torch.nn as nn
from nn7wonders import Net 

# load model
PATH = "./models/seven_net.pth"
# TODO: get input_size, hidden_size, num_classes from same location wich nn7wonders 
model = Net(21, 42, 21)
model.load_state_dict(torch.load(PATH))
model.eval()
print(model)

# bot logic
