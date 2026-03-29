import torch
import torch.nn as nn

class Model(nn.Module):
    def __init__(self, configs):
        super().__init__()
        self.seq_len = configs.seq_len   
        self.enc_in  = configs.enc_in    
        self.d_model = configs.d_model   
        self.flatten = nn.Flatten(start_dim=1) 
        self.proj    = nn.Linear(self.seq_len * self.enc_in, self.d_model)

    def forward(self, x_enc):            
        x = self.flatten(x_enc)         
        out = self.proj(x)              
        return out
