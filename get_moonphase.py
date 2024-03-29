from skyfield.api import load, Topos
from skyfield import almanac
from datetime import datetime, timedelta
from pytz import timezone

jkt = timezone('Asia/Jakarta')
ts = load.timescale(builtin=True)
e = load('de421.bsp')

t0 = ts.utc(2019, 1, 1)
t1 = ts.utc(2020, 1, 1)
f = almanac.moon_phases(e)
t, y = almanac.find_discrete(t0, t1, f)
for ti, yi in zip(t, y):
    if (yi == 0):
        print(ti.astimezone(jkt).replace(tzinfo=None))