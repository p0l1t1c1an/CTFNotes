#! env python3

import subprocess

mess = '1011000101011001100101001000101100101100111000101011011111001110111100001'

# Change upon reload of nc
magic = 73

for m in mess:
    if m == '0':
        print('00' * magic, end='')
    else:
        print('ff' * magic, end='')

