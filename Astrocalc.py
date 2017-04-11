#Michael Ivanitskiy
#Astronomical calculator
#version 0.4.1
#main file

print "Welcome to Astrocalc version 0.4.1"
print "by Michael Ivanitskiy"

from math import*
from copy import*
from copy import deepcopy

from visual import *
from visual.graph import *

import csv

#import graph_util_f
import gen_calc_f
from gen_calc_f import calc
import star_f
import blackhole_f
from vals import *
from vals_obj import sun


type_float = type(1.1)
type_int = type(1)


#write code here


#calculating mass of interstellar medium in a galaxy
#print "mass of galaxy's stars:	" + str(1e11*sun.mass)

#cubic_meters = 1e13*(ly**3)
#print "cubic meters of interstellar space:	" + str(cubic_meters)
#print "mass of interstellar space:	" + str(cubic_meters * proton.mass)

sun.set_mass(sun.mass)

print sun.temp





input("Press enter to exit")














