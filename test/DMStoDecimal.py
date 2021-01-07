import os
import pandas as pd

file_name = 'test\data_dmstodec.txt'
result = 'data_dmstodec.csv'

# open(result, 'w') as result_file

with open(file_name) as data:
    for line in data:
        val = line.split('\t')
        Sf = val[0]
        PP = val[1]
        Sf = Sf.split(':')
        Sf = int(Sf[0]) + (int(Sf[1])/60) + (float(Sf[2])/3600)
        PP = PP.split(':')
        PP = int(PP[0]) + (int(PP[1])/60) + (float(PP[2])/3600)
        selisih = PP-Sf
        print(round(Sf, 4), round(PP, 4), round(selisih, 4))