# _jengkolrebus
# November 2020
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
# import gui



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
    def __init__(self, lat, long, t0, t1):
        self.lat = lat
        self.long = long
        self.t0 = t0
        self.t1 = t1
        # self.elev = elev
        # self.topo = Topos(self.lat, self.long, elevation_m=self.elev)
        self.topo = Topos(self.lat, self.long)
        self.loc = e['earth'] + self.topo
        print(self.loc)

    def nearest_second(self, t):
        return (t + timedelta(seconds=0.5)).replace(microsecond=0)
    
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

    def newMoon(self):
        result = []
        t0 = ts.utc(self.t0)
        t1 = ts.utc(self.t1)
        f = almanac.moon_phases(e)
        t, y = almanac.find_discrete(t0, t1, f)
        for ti, yi in zip(t, y):
            if(yi == 0):
                result.append(ti)
            else:
                pass

        return result


    def moonSet(self, t):
        t = t.utc
        t0 = ts.utc(t[0], t[1], t[2], t[3], t[4], t[5])
        t1 = ts.utc(t[0], t[1], t[2]+1, t[3], t[4], t[5])
        f = almanac.risings_and_settings(e, e['moon'], self.topo, horizon_degrees=-0.833333)
        t, y = almanac.find_discrete(t0, t1, f)
        for ti, yi in zip(t, y):
            if(yi == 0):
                return ti
            else:
                pass

    def isMoonset(self, t):
        stat = self.moonSet(t)
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
    
    def objPos(self, t, obj):
        astrometric = self.loc.at(t).observe(e[obj])
        alt, az, d = astrometric.apparent().altaz()
        if (obj == 'moon'):
          appDiam = (2*np.arcsin(var.MOON_DIAMETER/(2*d.km)))*(180/np.pi)
        else:
          appDiam = (2*np.arcsin(var.SUN_DIAMETER/(2*d.km)))*(180/np.pi)
        appDia = Angle(degrees=appDiam)
        return alt, az, astrometric, appDia

    def hijri(self, t):
        t = t.utc
        year = t[0]
        month = t[1]
        day = t[2]

        print('Input:', year, month, day)

        # IF 1
        if (month < 3):
            year = year - 1 
            month = month + 12
        else:
            pass

        alpha = int(year/100)
        betha = 2 - alpha + int(alpha/4)
        b = int(365.25 * year) + int(30.6001 * (month + 1)) + day + 1722519 + betha
        c = int((b - 122.1)/365.25)
        d = int(365.25*c)
        e = int((b - d) / 30.6001)

        day = b - d - int(30.6001 * e)

        # IF 2
        if (e < 14):
            month = e - 1
        elif (e > 13):
            month = e - 13
        else:
            pass

        # IF 3
        if (month > 2):
            year = c - 4716
        elif (month < 3):
            year = c - 4715
        else:
            pass
        print('Julian Date:', year, month, day)


        # IF 4
        if ((year % 4) == 0):
            W = 1
        else:
            W = 2

        N = int((275*month)/9) - (W * int((month + 9)/12)) + day - 30
        A = year - 623
        B = int(A/4)
        C = A % 4
        C1 = 365.2501 * C
        C2 = int(C1)

        # IF 5
        if ((C1 - C2) > 0.5):
            C2 = C2 + 1
        else:
            pass

        D = (1461*B) + 170 + C2
        Q = int(D/10631)
        R = D % 10631
        J = int(R/354)
        K = R % 354
        O = int(((11*J) + 14)/30)
        H = (30 * Q) + J + 1
        JJ = K - O + N - 1

        CL = H % 30
        DL = ((11 * CL) + 3) % 30

        # IF 6
        if (DL < 19):
            JJ = JJ - 354
            H = H + 1
        elif (DL > 18):
            JJ = JJ - 355
            H = H + 1
        elif (JJ == 0):
            JJ = 355
            H = H - 1
        else:
            pass

        S = int((JJ - 1)/29.5)
        m = 1 + S
        d = int(JJ - (29.5 * S))

        if (d < 0):
            d = 30 + d
            m = 11 + m
            H = H - 1
            # print(tahun, bulan, hari)
        else:
            pass
        return '{}-{}-{}'.format(H, m, d)


# Metode untuk membandingkan dengan Imkan Rukyat
def imkanRukyat(alt, elong, age):
    if(alt.degrees >= 3 and elong.degrees >= 6.4):
        return u'\u2714'
    else:
        return u'\u2718'

# Metode untuk membandingkan dengan Wujudul Hilal
def wujudulHilal(alt):
    if(alt.degrees >= 0):
        return u'\u2714'
    else:
        return u'\u2718'

def result(lat, long, t0, t1):
    f = Find(lat, long, t0, t1)
    conj = f.newMoon()
    # conj = f.conjunction()
    # hijr = [f.hijri(i) for i in conj]

    sunset = [f.sunset(t, 1) for t in conj]
    for index, i in enumerate(sunset):
        if(f.isMoonset(i) == False):
            i = f.sunset(i, 2)
            sunset[index] = i
        else:
            pass
    # for i in sunset:
    #     print(i.astimezone(jkt))
    
    moonset = [f.moonSet(t) for t in sunset]
    # for i in moonset:
    #     print(i.astimezone(jkt))
    
    moon_alt = []
    moon_az = []
    moon_astrometric = []
    moon_appDia = []
    sun_alt = []
    sun_az = []
    sun_astrometric = []
    sun_appDia = []
    for t in sunset:
        alt, az, astro, appDia = f.objPos(t, 'moon')
        moon_alt.append(alt)
        moon_az.append(az)
        moon_astrometric.append(astro)
        moon_appDia.append(appDia.degrees)
        
        alt, az, astro, appDia = f.objPos(t, 'sun')
        sun_alt.append(alt)
        sun_az.append(az)
        sun_astrometric.append(astro)
        sun_appDia.append(appDia.degrees)
    
    elong = [moon.separation_from(sun) for moon, sun in zip(moon_astrometric, sun_astrometric)]

    def nearest_second(t):
        return (t + timedelta(seconds=0.5)).replace(microsecond=0)

    def nearest_second_timedelta(t):
        return timedelta(seconds=round(t.total_seconds()))

    
    conj[:] = [t.astimezone(jkt).replace(tzinfo=None) for t in conj]
    sunset[:] = [t.astimezone(jkt).replace(tzinfo=None) for t in sunset]
    moonset[:] = [t.astimezone(jkt).replace(tzinfo=None) for t in moonset]
    
    moon_age = [t1-t0 for (t0, t1) in zip(conj, sunset)]
    lag = [j-i for (i, j) in zip(sunset, moonset)]
    
    wujudul_hilal = [wujudulHilal(al) for al in moon_alt]
    imkan_rukyat = [imkanRukyat(al, el, age) for al, el, age in zip(moon_alt, elong, moon_age)]
    

    # lag[:] = [str(i) for i in lag]
    
    conj[:] = [nearest_second(t) for t in conj]
    sunset[:] = [nearest_second(t) for t in sunset]
    moonset[:] = [nearest_second(t) for t in moonset]

    
    moon_age[:] = [nearest_second_timedelta(t) for t in moon_age]
    lag[:] = [nearest_second_timedelta(t) for t in lag]

    moon_age[:] = [str(i) for i in moon_age]
    lag[:] = [str(i) for i in lag]
    
    # conj[:] = [str(i).split('.', 1)[0] for i in conj]
    # sunset[:] = [str(i).split('.', 1)[0] for i in sunset]
    # moon_age[:] = [i.split('.', 1)[0] for i in moon_age]
    # lag[:] = [i.split('.', 1)[0] for i in lag]

    moon_alt_deg = [i.degrees for i in moon_alt]
    moon_az_deg = [i.degrees for i in moon_az]
    sun_alt_deg = [i.degrees for i in sun_alt]
    sun_az_deg = [i.degrees for i in sun_az]

    moon_alt[:] = [str(i).replace('deg', u'\N{DEGREE SIGN}') for i in moon_alt]
    moon_az[:] = [str(i).replace('deg', u'\N{DEGREE SIGN}') for i in moon_az]
    sun_alt[:] = [str(i).replace('deg', u'\N{DEGREE SIGN}') for i in sun_alt]
    sun_az[:] = [str(i).replace('deg', u'\N{DEGREE SIGN}') for i in sun_az]
    elong[:] = [str(i).replace('deg', u'\N{DEGREE SIGN}') for i in elong]
    
    # Menampilkan hasil dalam bentuk tabel dataframe
    tabel = list(zip(conj, sunset,
                     moon_alt, moon_az, 
                     sun_alt, sun_az, 
                     elong, moon_age,
                     moonset, lag,
                     wujudul_hilal, imkan_rukyat,
                     moon_alt_deg, moon_az_deg,
                     sun_alt_deg, sun_az_deg,
                     moon_appDia, sun_appDia))


    # tabel = list(zip(conj, sunset,
    #                  moon_alt, moon_az, 
    #                  sun_alt, sun_az, 
    #                  elong, moon_age,
    #                  imkan_rukyat))
    
    df = pd.DataFrame(tabel, columns=['Waktu Konjungsi (UTC+07)', 'Waktu Sunset (UTC+07)', 
                                      'Altitude Bulan', 'Azimuth Bulan', 
                                      'Altitude Matahari', 'Azimuth Matahari', 
                                     'Elongasi', 'Usia Bulan',
                                     'Moonset', 'Lag Time',
                                     'Wujudul Hilal', 'Imkan Rukyat',
                                     'moon_alt', 'moon_az',
                                     'sun_alt', 'sun_az',
                                     'moonAppDia', 'sunAppDia'])

    # df = pd.DataFrame(tabel, columns=['Waktu Konjungsi (UTC+07)', 'Waktu Sunset (UTC+07)', 
    #                                   'Altitude Bulan', 'Azimuth Bulan', 
    #                                   'Altitude Matahari', 'Azimuth Matahari', 
    #                                  'Elongasi', 'Usia Bulan',
    #                                  'Imkan Rukyat'])
    # df.index+=1
    display(df.head())
    
    var.df = df
