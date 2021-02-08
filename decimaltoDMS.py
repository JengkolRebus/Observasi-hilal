import os
import pandas as pd

file_name = 'test\dataconvert.txt'
result = 'dataconvert.csv'

# open(result, 'w') as result_file

with open(file_name) as data:
    for line in data:
        val = float(line)
        d = int(val)
        m = int((val - d) * 60)
        s = (val - (m/60))* 3600
        print(d, m, "{:.2f}".format(round(s, 2)))