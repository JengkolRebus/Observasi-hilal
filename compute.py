from skyfield.api import load, Topos
from skyfield.units import Angle
from skyfield import almanac
from datetime import datetime, timedelta
from pytz import timezone
from ipywidgets import widgets, interact, interactive
from IPython.display import display, HTML
import pandas as pd
import calendar

class var:
    df = []

jkt = timezone('Asia/Jakarta')
ts = load.timescale()
e = load('de421.bsp')

class Find():
    def __init__(self, lat, long, t0, t1):
        self.lat = lat
        self.long = long
        self.t0 = t0
        self.t1 = t1
        self.topo = Topos(self.lat, self.long)
        self.loc = e['earth'] + self.topo
    
    def conjunction(self):
        result = []
        t0 = ts.utc(self.t0)
        t1 = ts.utc(self.t1)
        f = almanac.oppositions_conjunctions(e, e['moon'])
        t, y = almanac.find_discrete(t0, t1, f)
        for ti, yi in zip(t, y):
            if(yi == 1):
                result.append(ti)
            else:
                pass

        return result
        
    def sunset(self, t):
        t = t.utc
        t0 = ts.utc(t[0], t[1], t[2], t[3], t[4], t[5])
        t1 = ts.utc(t[0], t[1], t[2]+1, t[3], t[4], t[5])
        f = almanac.sunrise_sunset(e, self.topo)
        t, y = almanac.find_discrete(t0, t1, f)
        for ti, yi in zip(t, y):
            if(yi == False):
                return ti
            else:
                pass
    
    def objPos(self, t, obj):
        astrometric = self.loc.at(t).observe(e[obj])
        alt, az, d = astrometric.apparent().altaz()
        return alt, az, astrometric

# Metode untuk membandingkan dengan Imkan Rukyat
def imkanRukyat(alt, elong, age):
    if(alt.degrees >= 2 and elong.degrees >= 3 and (timedelta.total_seconds(age)/3600) > 8):
        return u'\u2714'
    else:
        return u'\u2718'

def result(lat, long, t0, t1):
    f = Find(lat, long, t0, t1)
    conj = f.conjunction()
    sunset = [f.sunset(t) for t in conj]
    
    moon_alt = []
    moon_az = []
    moon_astrometric = []
    sun_alt = []
    sun_az = []
    sun_astrometric = []
    for t in sunset:
        alt, az, astro = f.objPos(t, 'moon')
        moon_alt.append(alt)
        moon_az.append(az)
        moon_astrometric.append(astro)
        
        alt, az, astro = f.objPos(t, 'sun')
        sun_alt.append(alt)
        sun_az.append(az)
        sun_astrometric.append(astro)
    
    elong = [moon.separation_from(sun) for moon, sun in zip(moon_astrometric, sun_astrometric)]
        
    conj[:] = [t.astimezone(jkt).replace(tzinfo=None) for t in conj]
    sunset[:] = [t.astimezone(jkt).replace(tzinfo=None) for t in sunset]
    
    moon_age = [t1-t0 for (t0, t1) in zip(conj, sunset)]
    imkan_rukyat = [imkanRukyat(al, el, age) for al, el, age in zip(moon_alt, elong, moon_age)]
    
    # Menampilkan hasil dalam bentuk tabel dataframe
    tabel = list(zip(conj, sunset,
                     moon_alt, moon_az, 
                     sun_alt, sun_az, 
                     elong, moon_age,
                    imkan_rukyat))
    
    df = pd.DataFrame(tabel, columns=['Waktu Konjungsi (UTC+07)', 'Waktu Hilal (UTC+07)', 
                                      'Altitude Bulan', 'Azimuth Bulan', 
                                      'Altitude Matahari', 'Azimuth Matahari', 
                                     'Elongasi', 'Usia Bulan', 
                                     'Imkan Rukyat'])
    df.index+=1
    display(df.head())
    
    var.df = df
