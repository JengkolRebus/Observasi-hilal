# _jengkolrebus
# 1 Januari 2021
# Yogyakarta

from skyfield.api import load, Topos
from skyfield.units import Angle
from skyfield import almanac
from datetime import datetime, timedelta
from pytz import timezone
from ipywidgets import widgets, interact, interactive
from IPython.display import display, HTML
import pandas as pd
import calendar
import gui

class var:
    df = pd.DataFrame(list(zip(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')), columns=['Waktu Konjungsi (UTC+07)', 'Waktu Hilal (UTC+07)', 
                                      'Altitude Bulan', 'Azimuth Bulan', 
                                      'Altitude Matahari', 'Azimuth Matahari', 
                                     'Elongasi', 'Usia Bulan', 
                                     'Imkan Rukyat'])

jkt = timezone('Asia/Jakarta')
ts = load.timescale()
e = load('de421.bsp')

latitude = '7.83305556 S'
longitude = '110.38305556 E'

dari = jkt.localize(datetime(2019, 1, 1))
sampai = jkt.localize(datetime(2020, 1, 1))

class Find():
    def __init__(self, latitude, longitude, dari, sampai):
        self.latitude = latitude
        self.longitude = longitude
        self.topo = Topos(self.latitude, self.longitude)
        self.loc = e['earth'] + self.topo
        self.t0 = dari
        self.t1 = sampai
        
    def conjunction(self):
        conj = []
        t0 = ts.utc(self.t0)
        t1 = ts.utc(self.t1)
        f = almanac.oppositions_conjunctions(e, e['moon'])
        t, y = almanac.find_discrete(t0, t1, f)
        for ti, yi in zip(t, y):
            if(yi == 1):
                conj.append(ti)
            else:
                pass
        return conj
    
    def moonset(self, t):
        t = t.utc
        t0 = ts.utc(t[0], t[1], t[2], t[3], t[4], t[5])
        t1 = ts.utc(t[0], t[1], t[2] + 1, t[3], t[4], t[5])
        f = almanac.risings_and_settings(e, e['moon'], self.topo)
        t, y = almanac.find_discrete(t0, t1, f)
        for ti, yi in zip(t, y):
            if(yi == 0):
                return ti
            else:
                pass

    def isMoonset(self, t):
        stat = self.moonset(t)
        if (stat == None):
            return False
        else:
            return True
        
    def sunset(self, t, case):
        t = t.utc
        t0 = ts.utc(t[0], t[1], t[2], t[3], t[4], t[5])
        t1 = ts.utc(t[0], t[1], t[2] + case, t[3], t[4], t[5])
        f = almanac.sunrise_sunset(e, self.topo)
        t, y = almanac.find_discrete(t0, t1, f)
        for ti, yi in zip(t, y):
            if(yi == False):
                return ti
            else:
                pass


f = Find(latitude, longitude, dari, sampai)
conj = f.conjunction()
print('Konjungsi:')
for i in conj:
    print(conj.index(i)+1, i.astimezone(jkt))

sunset =[]
for i in conj:
    sunset.append(f.sunset(i, 1))

print()
print('Sunset Hilal:')


for index, i in enumerate(sunset):
    if(f.isMoonset(i) == False):
        i = f.sunset(i, 2)
        sunset[index] = i
    else:
        pass
    print(sunset.index(i)+1, i.astimezone(jkt))
