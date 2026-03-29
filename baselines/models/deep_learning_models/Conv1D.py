import torch
import torch.nn as nn
import torch.nn.functional as F

class _ConvBlock(nn.Module):
    def __init__(self, in_ch, out_ch, k=3, s=1, d=1, dropout=0.0, use_bn=True):
        super().__init__()
        pad = (k - 1) // 2 * d  
        self.conv = nn.Conv1d(in_ch, out_ch, kernel_size=k, stride=s, dilation=d, padding=pad)
        self.bn   = nn.BatchNorm1d(out_ch) if use_bn else nn.Identity()
        self.act  = nn.GELU()
        self.drop = nn.Dropout(dropout)

    def forward(self, x):  
        x = self.conv(x)
        x = self.bn(x)
        x = self.act(x)
        x = self.drop(x)
        return x


class Model(nn.Module):
    def __init__(self, configs):
        super().__init__()
        self.seq_len         = configs.seq_len
        self.enc_in          = configs.enc_in
        self.d_model         = configs.d_model
        self.num_blocks      = configs.e_layers
        self.hidden_channels = configs.cnn_channels
        self.kernel_size     = configs.kernel_size
        self.stride          = configs.stride
        self.dilation_base   = configs.dilation_base
        self.dropout_prob    = configs.dropout
        self.use_bn          = configs.use_bn

        blocks = []
        in_ch = self.enc_in
        dilation = 1
        for _ in range(self.num_blocks):
            blocks.append(
                _ConvBlock(
                    in_ch=in_ch,
                    out_ch=self.hidden_channels,
                    k=self.kernel_size,
                    s=self.stride,
                    d=dilation,
                    dropout=self.dropout_prob,
                    use_bn=self.use_bn,
                )
            )
            in_ch = self.hidden_channels
            dilation *= self.dilation_base

        self.blocks = nn.Sequential(*blocks)
        self.pool = nn.AdaptiveAvgPool1d(output_size=1)

        self.head = nn.Sequential(
            nn.LayerNorm(self.hidden_channels),
            nn.GELU(),
            nn.Dropout(self.dropout_prob),
            nn.Linear(self.hidden_channels, self.d_model),
        )

    def forward(self, x_enc):  
        x = x_enc.transpose(1, 2)   
        x = self.blocks(x)          
        x = self.pool(x).squeeze(-1) 
        x = self.head(x)           
        return x
