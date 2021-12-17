# jengkolrebus
# 12 Januari 2021
# Yogyakarta


class month():
    hijr = [
    'Muharram',
    'Shafar',
    'Rabi’ul Awwal',
    'Rabi’ul Akhir',
    'Jumadil',
    'Jumadil Akhir',
    'Rajab',
    'Sya’ban',
    'Ramadan',
    'Syawal',
    'Dzulqa’dah',
    'Dzulhijjah',
]

class toHijri():
    def __init__(self, tahun, bulan, hari):
        self.tahun = tahun
        self.bulan = bulan
        self.hari = hari
        self.hitung()

    def hitung(self):
        A = self.tahun
        B = self.bulan
        C = self.hari
        D = int(A/100)
        E = int(D/4)
        F = 2 - D + E
        A1 =A%400
        A2 = A%4
        A3 = A%100
        print(A1, A2, A3)
        
        if (A%400) == 0 or ((A%4)==0 and (A%100)>0):
            F = 2 - D + E
        else:
            F = 0
        print(F)

        G = int(365.25 * A)
        H = int((B+1) * 30.6001)
        I = C + F + G + H - 428
        print(I)
        J = I - 227016
        K = int(J/354.3671)
        L = int(K*354.3671)
        L = J - L
        K = K + int(L/354)
        L = L % 354
        if (L > 0):
            K = K + 1
        else:
            pass

        M = I % 7
        N = I % 5

        print('{}-{}-{}'.format(K, L, M))
        
        hari = L
        bulan = month.hijr

        if (hari <= 30):
            print(hari, bulan[0], K)
        elif (hari <= 59):
            print(hari - 30, bulan[1], K)
        elif (hari <= 89):
            print(hari - 59, bulan[2], K)
        elif (hari <= 118):
            print(hari - 89, bulan[3], K)
        elif (hari <= 148):
            print(hari - 118, bulan[4], K)
        elif (hari <= 177):
            print(hari - 148, bulan[5], K)
        elif (hari <= 207):
            print(hari - 177, bulan[6], K)
        elif (hari <= 236):
            print(hari - 207, bulan[7], K)
        elif (hari <= 266):
            print(hari - 236, bulan[8], K)
        elif (hari <= 295):
            print(hari - 266, bulan[9], K)
        elif (hari <= 325):
            print(hari - 295, bulan[10], K)
        else:
            print(hari - 325, bulan[11], K)

toHijri(2018, 8, 8)