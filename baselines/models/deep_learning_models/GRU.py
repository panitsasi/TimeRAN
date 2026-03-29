import torch
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
    """
    GRU encoder → (B, d_model)
    Expects x_enc shape (B, T, C). Returns (B, d_model).
    """
    def __init__(self, configs):
        super().__init__()
        self.seq_len = configs.seq_len
        self.enc_in  = configs.enc_in
        self.d_model = configs.d_model
        self.num_layers   = configs.e_layers
        self.dropout_prob = configs.dropout
        self.bidirectional = configs.bidirectional
        
        self.input_proj = nn.Linear(self.enc_in, self.d_model)

        self.gru = nn.GRU(
            input_size=self.d_model,
            hidden_size=self.d_model,
            num_layers=self.num_layers,
            batch_first=True,
            dropout=self.dropout_prob if self.num_layers > 1 else 0.0,
            bidirectional=self.bidirectional,
        )

        out_dim = self.d_model * (2 if self.bidirectional else 1)
        self.norm = nn.LayerNorm(out_dim)
        self.act  = nn.GELU()
        self.drop = nn.Dropout(self.dropout_prob)
        self.proj = nn.Linear(out_dim, self.d_model)

    def forward(self, x_enc):     # x_enc: (B, T, C)
        x = self.input_proj(x_enc)          # (B, T, d_model)
        out, _ = self.gru(x)                # (B, T, d_model*dir)
        feat = out[:, -1, :]                # last timestep
        feat = self.norm(feat)
        feat = self.act(feat)
        feat = self.drop(feat)
        return self.proj(feat)              # (B, d_model)
