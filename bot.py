# -*- coding: utf-8 -*-
# Bot to play 7 Wonders
import torch 
import torch.nn as nn


# load model
PATH = "./models/seven_net.pth"
model = torch.load(PATH)
print(model)


# bot logic
