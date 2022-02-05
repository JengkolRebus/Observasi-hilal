# _jengkolrebus
# Mei 2021
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
import numpy as np

class var:
    df = pd.DataFrame(list(zip(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')), columns=['Waktu Konjungsi (UTC+07)', 'Waktu Hilal (UTC+07)', 
                                      'Altitude Bulan', 'Azimuth Bulan', 
                                      'Altitude Matahari', 'Azimuth Matahari', 
                                     'Elongasi', 'Usia Bulan', 
                                     'Imkan Rukyat'])

    MOON_DIAMETER = 3474.2 #1737.1 # km
    SUN_DIAMETER = 1392700 #696340 # km

jkt = timezone('Asia/Jakarta')
ts = load.timescale(builtin=True)
e = load('de421.bsp')

class Find():
    def __init__(self, lat, long, t):
        self.lat = lat
        self.long = long
        self.t = t
        # self.elev = elev
        # self.topo = Topos(self.lat, self.long, elevation_m=self.elev)
        self.topo = Topos(self.lat, self.long)
        self.loc = e['earth'] + self.topo
        print(self.loc)

    def nearest_second(self, t):
        return (t + timedelta(seconds=0.5)).replace(microsecond=0)

    def moonSet(self, t):
        t = t.utc
        t0 = ts.utc(t[0], t[1], t[2], t[3], t[4], t[5])
        t1 = ts.utc(t[0], t[1], t[2]+1, t[3], t[4], t[5])
        f = almanac.risings_and_settings(e, e['moon'], self.topo)
        t, y = almanac.find_discrete(t0, t1, f)
        for ti, yi in zip(t, y):
            if(yi == 0):
                return ti
            else:
                pass
        
    def sunset(self, t):
        t = ts.utc(t)
        t = t.utc
        t0 = ts.utc(t[0], t[1], t[2], t[3], t[4], t[5])
        t1 = ts.utc(t[0], t[1], t[2] + 1, t[3], t[4], t[5])
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
        if (obj == 'moon'):
          appDiam = (2*np.arcsin(var.MOON_DIAMETER/(2*d.km)))*(180/np.pi)
        else:
          appDiam = (2*np.arcsin(var.SUN_DIAMETER/(2*d.km)))*(180/np.pi)
        appDia = Angle(degrees=appDiam)
        return alt, az, astrometric, appDia


# Metode untuk membandingkan dengan Imkan Rukyat
def imkanRukyat(alt, elong, age):
    if(alt.degrees >= 2 and elong.degrees >= 3 and (timedelta.total_seconds(age)/3600) > 8):
        return u'\u2714'
    else:
        return u'\u2718'

def result(lat, long, t0):
    f = Find(lat, long, t0)

    sunset = f.sunset(t0)
    # for i in sunset:
    #     print(i.astimezone(jkt))
    
    moonset = f.moonSet(sunset)
    # for i in moonset:
    #     print(i.astimezone(jkt))
    
    alt, az, astro, appDia = f.objPos(sunset, 'moon')
    moon_alt = alt
    moon_az = az
    moon_astrometric = astro
    moon_appDia = appDia.degrees
        
    alt, az, astro, appDia = f.objPos(sunset, 'sun')
    sun_alt = alt
    sun_az = az
    sun_astrometric = astro
    sun_appDia = appDia.degrees
    
    elong = moon_astrometric.separation_from(sun_astrometric)

    def nearest_second(t):
        return (t + timedelta(seconds=0.5)).replace(microsecond=0)

    def nearest_second_timedelta(t):
        return timedelta(seconds=round(t.total_seconds()))

    
    conj = 1
    sunset = sunset.astimezone(jkt).replace(tzinfo=None)
    moonset = moonset.astimezone(jkt).replace(tzinfo=None)
    
    moon_age = 1
    lag = moonset - sunset
    
    imkan_rukyat = 1
    
    sunset = nearest_second(sunset)
    moonset = nearest_second(moonset)

    lag = nearest_second_timedelta(lag)

    moon_age = str(moon_age)
    lag = str(lag)
    
    # conj[:] = [str(i).split('.', 1)[0] for i in conj]
    # sunset[:] = [str(i).split('.', 1)[0] for i in sunset]
    # moon_age[:] = [i.split('.', 1)[0] for i in moon_age]
    # lag[:] = [i.split('.', 1)[0] for i in lag]

    moon_alt_deg = moon_alt.degrees
    moon_az_deg = moon_az.degrees
    sun_alt_deg = sun_alt.degrees
    sun_az_deg = sun_az.degrees

    moon_alt = str(moon_alt).replace('deg', u'\N{DEGREE SIGN}')
    moon_az = str(moon_az).replace('deg', u'\N{DEGREE SIGN}')
    sun_alt = str(sun_alt).replace('deg', u'\N{DEGREE SIGN}')
    sun_az = str(sun_az).replace('deg', u'\N{DEGREE SIGN}')
    elong = str(elong).replace('deg', u'\N{DEGREE SIGN}')
    
    # Menampilkan hasil dalam bentuk tabel dataframe
    tabel = [conj, sunset, 
                    moon_alt, moon_az, 
                    sun_alt, sun_az, 
                    elong, moon_age, 
                    moonset, lag, 
                    imkan_rukyat, moon_alt_deg, 
                    moon_az_deg, sun_alt_deg, 
                    sun_az_deg, moon_appDia, 
                    sun_appDia]
    
    row = ['Waktu Konjungsi (UTC+07)', 'Waktu Sunset (UTC+07)', 
                                      'Altitude Bulan', 'Azimuth Bulan', 
                                      'Altitude Matahari', 'Azimuth Matahari', 
                                     'Elongasi', 'Usia Bulan',
                                     'Moonset', 'Lag Time',
                                     'Imkan Rukyat',
                                     'moon_alt', 'moon_az',
                                     'sun_alt', 'sun_az',
                                     'moonAppDia', 'sunAppDia']


    # tabel = list(zip(conj, sunset,
    #                  moon_alt, moon_az, 
    #                  sun_alt, sun_az, 
    #                  elong, moon_age,
    #                  imkan_rukyat))
    
    df = pd.DataFrame([tabel], columns=row)

    # df = pd.DataFrame(tabel, columns=['Waktu Konjungsi (UTC+07)', 'Waktu Sunset (UTC+07)', 
    #                                   'Altitude Bulan', 'Azimuth Bulan', 
    #                                   'Altitude Matahari', 'Azimuth Matahari', 
    #                                  'Elongasi', 'Usia Bulan',
    #                                  'Imkan Rukyat'])
    # df.index+=1
    display(df.head())
    
    var.df = df
