## TODO: define the convolutional neural network architecture

import torch
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
        ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        
        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel
        
        # Layer 1
        # Input image size (1, 224, 224)
       
        self.conv1 = nn.Conv2d(1, 32, 4)      # Ouput layer (32, 221, 221)
        self.pool1 = nn.MaxPool2d(2, 2)       # Ouput layer (32, 110, 110)
        self.dropout1 = nn.Dropout(p=0.1)     # Ouput layer (32, 110, 110)
        
        # Layer 2
        self.conv2 = nn.Conv2d(32, 64, 3)     # Ouput layer (64, 108, 108)
        self.pool2 = nn.MaxPool2d(2, 2)       # Ouput layer (64, 54, 54)
        self.dropout2 = nn.Dropout(p=0.2)     # Ouput layer (64, 54, 54)
        
        # Layer 3
        self.conv3 = nn.Conv2d(64, 128, 3)    # Ouput layer (128, 52, 52)  
        self.pool3 = nn.MaxPool2d(2, 2)       # Ouput layer (128, 26, 26) 
        self.dropout3 = nn.Dropout(p=0.3)     # Ouput layer (128, 26, 26) 
        
        # Layer 4
        self.conv4 = nn.Conv2d(128, 256, 1)   # Ouput layer (256, 26, 26)
        self.pool4 = nn.MaxPool2d(2, 2)       # Ouput layer (256, 13, 13) 
        self.dropout4 = nn.Dropout(p=0.4)     # Ouput layer (256, 13, 13) 
        
        # Layer 5
        #self.conv5 = nn.Conv2d(256, 512, 2)   # Ouput layer (512, 11, 11)
        #self.pool5 = nn.MaxPool2d(2, 2)       # Ouput layer (512, 5, 5) 
        #self.dropout5 = nn.Dropout(p=0.5)     # Ouput layer (512, 5, 5)
        
        
        # Dense layer 1
        self.dl1 = nn.Linear(256*13*13, 1000)
        self.dropout5 = nn.Dropout(p=0.5)
        
        # Dense layer 2
        self.dl2 = nn.Linear(1000,  1000)
        self.dropout6 = nn.Dropout(p=0.6)
        
        # Output layer
        self.dl3 = nn.Linear(1000,  68*2)
        
        ## Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) to avoid overfitting
        

        
    def forward(self, x):
        ## TODO: Define the feedforward behavior of this model
        ## x is the input image and, as an example, here you may choose to include a pool/conv step:
        ## x = self.pool(F.relu(self.conv1(x)))
        
        # Layer 1
        x = self.pool1(F.relu(self.conv1(x)))
        x = self.dropout1(x)
        # Layer 2
        
        x = self.pool2(F.relu(self.conv2(x)))
        x = self.dropout2(x)

        # Layer 3
        x = self.pool3(F.relu(self.conv3(x)))
        x = self.dropout3(x)

        # Layer 4
        x = self.pool4(F.relu(self.conv4(x)))
        x = self.dropout4(x)
        
        # Layer 5
        #x = self.pool5(F.relu(self.conv5(x)))
        #x = self.dropout5(x)
        
        #x = flatten(x)
        
        x = x.view(x.size(0), -1)
        # Dense layer 1
        x = self.dl1(x)
        x = self.dropout5(x)
        
        
        # Dense layer 2
        x = self.dl2(x)
        x = self.dropout6(x)
        
        x = self.dl3(x)
        
        
        # a modified x, having gone through all the layers of your model, should be returned
        return x
