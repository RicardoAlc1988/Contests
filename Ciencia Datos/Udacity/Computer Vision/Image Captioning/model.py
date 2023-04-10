import torch
import torch.nn as nn
import torchvision.models as models


class EncoderCNN(nn.Module):
    def __init__(self, embed_size):
        super(EncoderCNN, self).__init__()
        resnet = models.resnet50(pretrained=True)
        for param in resnet.parameters():
            param.requires_grad_(False)
        
        modules = list(resnet.children())[:-1]
        self.resnet = nn.Sequential(*modules)
        self.embed = nn.Linear(resnet.fc.in_features, embed_size)

    def forward(self, images):
        features = self.resnet(images)
        features = features.view(features.size(0), -1)
        features = self.embed(features)
        return features
    

class DecoderRNN(nn.Module):
    def __init__(self, embed_size, hidden_size, vocab_size, num_layers=1):
        super(DecoderRNN, self).__init__()
        self.num_layers = num_layers
        self.hidden_size = hidden_size
        self.embed_size = embed_size
        self.vocab_size = vocab_size
        
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.lstm = nn.LSTM(input_size =embed_size, hidden_size=hidden_size, num_layers=num_layers, batch_first = True)
        self.fc = nn.Linear(hidden_size, vocab_size)
    
    def forward(self, features, captions):
        
        ### Input dimensions ###
        # caption dimensions (batch_size, caption_length)
        # features dimension (batch_size, embed_size)
        
        device = torch.device('cuda:0' if torch.cuda.is_available() else "cpu")
        
        # Get batch size
        batch_size = captions.size(0)
        
        captions = captions[:, :-1]  # Correction, instead the output will be (batch_size, caption_length + 1, vocab_size)
        features = features.unsqueeze(1) # output dimension (batch_size, 1, embed_size)
        
        self.hidden_state = torch.zeros((self.num_layers, batch_size, self.hidden_size)).to(device)
        self.cell_state = torch.zeros((self.num_layers, batch_size, self.hidden_size)).to(device)
        
        embeddings = self.embedding(captions)  # output dimension (batch_size, caption_length -1, embed_size)
        lstm_input = torch.cat((features, embeddings), dim=1) # output dimension (batch_size, caption_length, embed_size)
        lstm_output, (self.hidden_state, self.cell_state) = self.lstm(lstm_input, (self.hidden_state, self.cell_state)) # output dimension (batch_size, caption_length, embed_size)
        out = self.fc(lstm_output) # output dimension (batch_size, caption_length, vocab_size)

        return out

    def sample(self, inputs, states=None, max_len=20):
        " accepts pre-processed image tensor (inputs) and returns predicted sentence (list of tensor ids of length max_len) "
        
        ### Input dimensions ###
        # feature dimensions (1, 1, embed_size)
        
        pred_words_indices = []
        predicted_word_idx = -1
        actual_length = 0
        
        while (predicted_word_idx != 1) or (actual_length < max_len+1): 
            
            # get the prediction for the current inputs
            
            lstm_out, states = self.lstm(inputs, states) # Output dimension (1, 1, embed_size)
            
            # Get the scores for the given input
            scores = self.fc(lstm_out) # Output dimension (1, 1, vocab_size)
            
            # Get rid of the 'captiong_length' dummy dimension
            scores = scores.squeeze(1) # output dimension (1, vocab_size)
            
            # Get the index of the most probable word
            _, predicted_word_idx = torch.max(input=scores, dim=1)
            
            # Append the predicted word to the list, by using the data dictionary
            pred_words_indices.append(predicted_word_idx.cpu().numpy()[0].item())
            
            ### Preparation for the next prediction ###
            
            # Get the word embedding representation
            inputs = self.embedding(predicted_word_idx) # Dimension output (1, embed_size)
            inputs = inputs.unsqueeze(1) # Dimension output (1, 1, embed_size)
            
            actual_length = actual_length + 1
            
        return pred_words_indices