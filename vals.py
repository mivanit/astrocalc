#Michael Ivanitskiy
#Astronomical calculator
#version 0.4.1
#common values

from math import*
from copy import*
from copy import deepcopy

#calculation error margin to print changes
comparison_margin = 0.05

#mathematical consts
e = 2.71828
pi = 3.1415926536

#physical consts
h = 6.62607004e-34              #planck
k_B = 1.38064852e-23            #Boltzmann const
c = 2.997924e8                  #speed of light
G = 6.67408e-11                 #universal gravitational constant
b_wien = h * c / (4.9651 * k_B)                 #wiens displacement
s_b = 2 * (pi**5) * (k_B ** 4) / (15 * (h**3) * (c**2))         #Stefan - Boltzmann const (sigma)

#unit conversions
#distance
parsec = 3.08567758149137e16
AU = 149597870700		#astronomical unit
ly = 9.460530e15		#light year
#time
year = 31556925.9747	#seconds in a year
#surface gravity
gee = 9.80665
#"gee" so as to avoid confusion 
#with gravitational constant

#other
universe_age = 13.82e9 * year
















