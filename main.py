import control.matlab as c
import matplotlib.pyplot as plt
import sys
import numpy as np
from sympy import *
import math

#ПИД-регулятор+САУ
def PID(Kp,Ki,Kd):
    wP = c.tf([Kp], [1])
    wI = c.tf([Ki], [1, 0])
    wD = c.tf([Kd, 0], [1])
    wPID = c.parallel(wP + wI + wD);
    return wPID;
def CAYPID(w1,w2,w3,wPID):
    w5 = c.series(w1, w2, w3, wPID)
    w = c.feedback(w5, 1,-1)
    return w;

#П-регулятор+САУ
def P(Kp):
    wP = c.tf([Kp], [1])
    return wP;
def CAYP(w1,w2,w3,wP):
    w5 = c.series(w1, w2, w3, wP)
    w = c.feedback(w5, 1,-1)
    return w;

#Переходная
def perehodnayONE(W):
    f = True
    TimeLine = []
    for i in range(0, 600, 1):
        TimeLine.append(i / 10)
    plt.figure(figsize=(6, 6))
    y, x = c.step(W, TimeLine)
    plt.plot(x, y)
    plt.vlines(15, 0, 1.121,
               color='b',
               linewidth=0.75,
               linestyle='-')
    plt.hlines(1.025, 0, 40,
               color='g',
               linewidth=0.5,
               linestyle='--'
               )
    plt.hlines(0.975, 0, 40,
               color='g',
               linewidth=0.5,
               linestyle='--'
               )
    plt.legend(['W'], fontsize=10, shadow=True)
    plt.title('Переходная характеристика ')
    plt.ylabel('Амплитуда', fontsize=10, color='black')
    plt.xlabel('Время(сек)', fontsize=8, color='black')
    plt.grid()
    plt.show()
#АЧХ и ФЧХ
def ACH(W):
    omega = []
    for i in range(1, 1000,1):
        omega.append(i/10)
    mag,phase,omega = c.bode(W, omega, dB=False, Hz=False)
    plt.legend(['W'], fontsize=10, shadow=True)
    plt.plot()
    plt.show()
#Комплексная плоскость
def KORNI(W):
   c.pzmap (W)
   plt.axis([-5, 0.5, -2, 2])
   plt.show()
#ЛАЧХ и ЛФЧХ
def LACH(W):
    mag,phase,omega = c.bode(W,dB=True)
    plt.legend(['W'], fontsize=10, shadow=True)
    plt.plot()
    plt.show()
def pokorn(W):
    f=True
    s = c.pole(W)
    for i in s:
        print(i, ' ')
        if (i.real >= 0):
            f = false
    if f == true:
        print("Система устойчива")
    else:
        print("Система неустойчива")

ky=22
Tg=10.0
Ty=4.0
Tgm=1.0
w1=c.tf([1],[Tg,1])
w2=c.tf([Tgm*0.01,1],[Tg*0.05,1])
w3=c.tf([ky],[Ty,1])

##################
W3 = CAYP(w1, w2, w3,wP=P(1))
print(W3)
############
# perehodnayONE(W3)
# pokorn(W3)
# KORNI(W3)
# ACH(W3)
# LACH(W3)
def perehodnay(W1,W2,W3):
    f = True
    TimeLine = []
    for i in range(0, 600, 1):
        TimeLine.append(i / 10)
    plt.figure(figsize=(6, 6))
    y, x = c.step(W1, TimeLine)
    plt.plot(x, y)
    y, x = c.step(W2, TimeLine)
    plt.plot(x, y)
    y, x = c.step(W3, TimeLine)
    plt.plot(x, y)
    plt.vlines(15, 0, 1.121,
               color='b',
               linewidth=0.75,
               linestyle='-')
    plt.hlines(1, 0, 60,
               color='r',
               linewidth=0.5,
               linestyle='-'
               )
    plt.hlines(1.05, 0, 60,
               color='g',
               linewidth=0.5,
               linestyle='--'
               )
    plt.hlines(0.95, 0, 40,
               color='g',
               linewidth=0.5,
               linestyle='--'
               )
    plt.legend(['W1','W2','W3'], fontsize=10, shadow=True)
    plt.title('Переходная характеристика ')
    plt.ylabel('Амплитуда', fontsize=10, color='black')
    plt.xlabel('Время(сек)', fontsize=8, color='black')
    plt.grid()
    plt.show()
def ACH(W1,W2,W3):
    omega = []
    for i in range(1, 1000,1):
        omega.append(i/10)
    mag,phase,omega = c.bode(W1, omega, dB=False)
    mag,phase, omega = c.bode(W2, omega, dB=False)
    mag,phase, omega = c.bode(W3, omega, dB=False)
    plt.legend(['W1','W2','W3'], fontsize=10, shadow=True)
    plt.plot()
    plt.show()
W1 = CAYP(w1, w2, w3,wP=P(1.4))
W2 = CAYP(w1, w2, w3,wP=P(1))
W3 = CAYP(w1, w2, w3,wP=P(0.7))
perehodnay(W1,W2,W3 )
