from skyfield.api import load, Topos
from skyfield.units import Angle
from datetime import datetime
from pytz import timezone

jkt = timezone('Asia/Jakarta')
ts = load.timescale()
e = load('de421.bsp')

lat = '7.83305556 S'
long = '110.38305556 E'
t = jkt.localize(datetime(2020, 1, 1))

topo = Topos(lat, long)
loc = e['earth'] + topo

print(topo)


for d in range(12):
    t0 = ts.utc(2020, 1 + d, 1)
    astrometric = loc.at(t0).observe(e['sun'])
    alt, az, d = astrometric.apparent().altaz()
    print(t0.astimezone(jkt).replace(tzinfo=None), alt, az)
