import os
import pandas as pd

file_name = 'test\data_dmstodec.txt'
result = 'data_dmstodec.csv'

# open(result, 'w') as result_file

with open(file_name) as data:
    for line in data:
        val = line.split('\t')
        alt = val[0]
        az = val[1]
        alt = alt.split(':')
        alt = int(alt[0]) + (int(alt[1])/60) + (int(alt[2])/3600)
        az = az.split(':')
        az = int(az[0]) + (int(az[1])/60) + (int(az[2])/3600)
        print(round(alt, 4), round(az, 4))