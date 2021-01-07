# jengkolrebus
# 8 Januari 2021
# Yogyakarta
# sumber: Jean Meeus

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
hDay = [30, 29,
        30, 29,
        30, 29,
        30, 29,
        30, 29,
        30, 29]

X = 1991 # tahun
M = 3 # bulan
D = 13 # tanggal

print(X, M, D)
print()
if M < 3:
    X = X -1
    M = M + 12
else:
    pass
print(X, M, D)
print()

alpha = int(X/100)
beta = 2 - alpha + int(alpha/4)
print('alpha=', alpha)
print('beta=', beta)

b = int(365.25*X) + int(30.6001*(M+1)) + D + 1722519 + beta
print('b=', b)
c = int((b-122.1)/365.25)
print('c=', c)
d = int(365.25*c)
print('d=', d)
e = int((b-d)/30.6001)

D = b - d - int(30.6001 * e)
print('D=', D)
if (e>13):
    M = e-13
else:
    M = e-1
print('M=', M)

if (M>3):
    X = c - 4716
else:
    X = c - 4715
print('X=', X)

Xmod = X % 4
print('Xmod=', Xmod)
if(Xmod == 0):
    W = 1
else:
    W = 2
print('W=',W)

N = int((275*M)/9) - (W * int((M+9)/12)) + D - 30
print('N=', N)
A = X - 623
print('A=', A)
B = int(A/4)
print('B=', B)
C = A % 4
print('C=', C)
C1 = 365.2501 * C
print('C1=', C1)
C2 = int(C1)
print('C2=', C2)
if(C1-C2 == 0.5):
    C2 = C2+1
else:
    pass
print('C2=', C2)

Da = (1461 * B) + 170 + C2
print('Da=', Da)

Q = int(Da/10631)
print('Q=', Q)

R = Da % 10631
print('R=', R)

J = int(R/354)
print('J=', J)

K = R % 354
print('K=', K)

O = int(((11*J)+14)/30)
print('O=', O)

H = (30*Q) + J + 1
print('H=', H)

JJ = K - O + N -1
print('JJ=', JJ)

CL = H % 30
print('CL=', CL)

DL = ((11*CL)+3) % 30
print('DL=', DL)

if (DL < 19):
    print('Common Year')
    leap = False
    JJ = JJ - 354
    H = H + 1
elif(DL > 18):
    print('Leap Year')
    leap = True
    JJ = JJ - 355
    H = H + 1
elif(JJ == 0):
    print('Leap Year')
    leap = False
    JJ = 355
    H = H -1
else:
    pass
print('JJ=', JJ)
print('H=', H)

S = int((JJ-1)/29.5)
print('S=', S)

m = 1+S
print('m=', m)

d = int(JJ-(29.5*S))
print('d=', d)

if (JJ == 355):
    m = 12
    d = 30

print()
print(H, m, d)

# if (d < 1):
#     if (m < 0):
#         m = m + 11
#         if (m < 1):
#             H = H -1
#     else:
#         m = m - 13
# if (m < 1):
#     H = H -1
# if (d < 1):
#     mDay = hDay[abs(m)-1]
#     print(mDay)
#     d = mDay + d

# print(H, abs(m), d)

print(H, hijr[m-1], d)
