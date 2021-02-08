from skyfield.api import load, Topos
from skyfield.units import Angle
from datetime import datetime
from pytz import timezone

jkt = timezone('Asia/Jakarta')
ts = load.timescale(builtin=True)
e = load('de421.bsp')

lat = 7+(49/60)+(59/3600)
long = 110+(22/60)+(59/3600)
print(lat)
lat = str(lat)+' S'
print(lat)

lat = '5.89383333333333 N'
long = '95.324 E'
# t = jkt.localize(datetime(2020, 1, 1, 0, 0, 0))

topo = Topos(lat, long)
loc = e['earth'] + topo

print(topo)

for d in range(1):
    t0 = ts.utc(2020, 8 + d, 19, 18-7, 50, 55)
    astrometric = loc.at(t0).observe(e['moon'])
    alt, az, d = astrometric.apparent().altaz()
    alt=str(alt).replace('deg ', ':').replace('\' ', ':').replace('"', '')
    az=str(az).replace('deg ', ':').replace('\' ', ':').replace('"', '')
    print(alt, az)