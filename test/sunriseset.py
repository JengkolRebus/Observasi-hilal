from skyfield.api import load, Topos
from skyfield import almanac
from datetime import datetime, timedelta
from pytz import timezone

jkt = timezone('Asia/Jakarta')
ts = load.timescale(builtin=True)
e = load('de421.bsp')

lat = 7+(49/60)+(59/3600)
long = 110+(22/60)+(49/3600)

lat = str(lat)+ ' S'
long = str(long)+ ' E'

topos = Topos(lat, long)

t0 = ts.utc(2021, 1, 15, -7)
t1 = ts.utc(2021, 1, 20, -7)
f = almanac.sunrise_sunset(e, topos)
t, y = almanac.find_discrete(t0, t1, f)
for ti, yi in zip(t, y):
    print(ti.astimezone(jkt), yi)