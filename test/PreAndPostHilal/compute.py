  
# _jengkolrebus
# November 2020
# Yogyakarta

from skyfield.api import load, Topos
from skyfield.units import Angle
from skyfield import almanac
from datetime import datetime, timedelta
from pytz import timezone
import calendar
import numpy as np

jkt = timezone('Asia/Jakarta')
ts = load.timescale()
e = load('de421.bsp')


Lat = '7.83305556 S'
Long =  '110.38305556 E'
topo = Topos(Lat, Long)
loc = e['earth'] + topo

t0 = datetime(2021, 4, 1, 0, 0, 0)
t1 = datetime(2021, 4, 30, 0, 0, 0)

t0 = ts.from_datetime(jkt.localize(t0))
t1 = ts.from_datetime(jkt.localize(t1))

print('t0: ', t0.astimezone(jkt))
print('t1: ', t1.astimezone(jkt))

# NewMoon
# conj = []
f = almanac.moon_phases(e)
t, y = almanac.find_discrete(t0, t1, f)
for ti, yi in zip(t, y):
    if(yi == 0):
        conj = ti
    else:
        pass

print('Konjungsi: ', conj.astimezone(jkt))

# Sunset
t = t.utc
t0 = ts.utc(t[0], t[1], t[2], t[3], t[4], t[5])
t1 = ts.utc(t[0], t[1], t[2] + 1, t[3], t[4], t[5])
f = almanac.sunrise_sunset(e, topo)
t, y = almanac.find_discrete(t0, t1, f)
for ti, yi in zip(t, y):
    if(yi == False):
        sunset = ti
    else:
        pass

print('Sunset: ', sunset)