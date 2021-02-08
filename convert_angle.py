from skyfield.api import load, Topos
from skyfield.api import Angle

# a = Angle()
# print(type(a.dms()))

b = '282° 41\' 01\"'
c = b.split(' ')
c[:] = [int(str(i).replace('°', '').replace('\'', '').replace('\"', '')) for i in c]

print(c)