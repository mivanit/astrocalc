#Michael Ivanitskiy
#Astronomical calculator
#version 0.4.1
#main file

print ("Welcome to Astrocalc version 0.4.1")
print ("by Michael Ivanitskiy")

from math import*
from copy import*
from copy import deepcopy

#from visual import *
#from visual.graph import *

import csv

#import graph_util_f
from gen_calc_f import*
from star_f import*
from blackhole_f import*
from vals import *
from vals_obj import *


type_float = type(1.1)
type_int = type(1)


calc_t = gen_calc()

#write code here


#calculating mass of interstellar medium in a galaxy
#print "mass of galaxy's stars:	" + str(1e11*sun.mass)

#cubic_meters = 1e13*(ly**3)
#print "cubic meters of interstellar space:	" + str(cubic_meters)
#print "mass of interstellar space:	" + str(cubic_meters * proton.mass)

#sun.set_mass(sun.mass)

#print sun.temp

E_e = (electron.mass * 2 * (c**2))
E_p = (proton.mass * 2 * (c**2))

#test BlackBody
bb = gen_obj()

t_wavelength = calc_t.photon_energy_to_L(E_e)
bb.set_Lpeak(t_wavelength)
print (bb.temp)

t_wavelength = calc_t.photon_energy_to_L(E_p)
bb.set_Lpeak(t_wavelength)
print (bb.temp)



input("Press enter to exit")
