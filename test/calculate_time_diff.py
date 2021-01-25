import glob
import os
import pandas as pd
import matplotlib.pyplot as plt

from datetime import timedelta

hasil = 'test\data\hasil_moon_phase2019.xlsx'
# print(os.listdir('test\data'))

sheet = [0, 1, 2, 3]
sheetName = ['NewMoon', 'FirstQuarter', 'FullMoon', 'LastQuarter']

def calculate(sheetname):

    data = pd.read_excel('test\data\moon_phase.xlsx', sheet_name=sheetname)
    df = pd.DataFrame(data)
    nasa = df.columns[0]
    at = df.columns[1]
    ahc = df.columns[2]
    skyfield = df.columns[3]

    delta_at = (df[nasa] - df[at]).astype('timedelta64[s]')
    delta_ahc = (df[nasa] - df[ahc]).astype('timedelta64[s]')
    delta_skyfield = (df[nasa] - df[skyfield]).astype('timedelta64[s]')

    # delta_at[:] = [pd.Timedelta(i).total_seconds() for i in delta_at]
    # delta_ahc[:] = [pd.Timedelta(i).total_seconds() for i in delta_ahc]
    # delta_skyfield[:] = [pd.Timedelta(i).total_seconds() for i in delta_skyfield]

    df['delta_at'] = delta_at
    df['delta_ahc'] = delta_ahc
    df['delta_skyfield'] = delta_skyfield
    print(df)
    return df

newMoon = calculate(0)
firstQuarter = calculate(1)
fullMoon = calculate(2)
lastQuarter = calculate(3)

with pd.ExcelWriter(hasil) as writer:
    newMoon.to_excel(writer, sheet_name=sheetName[0])
    firstQuarter.to_excel(writer, sheet_name=sheetName[1])
    fullMoon.to_excel(writer, sheet_name=sheetName[2])
    lastQuarter.to_excel(writer, sheet_name=sheetName[3])