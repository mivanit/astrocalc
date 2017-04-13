#Michael Ivanitskiy
#Astronomical calculator
#version 0.4.1
#object values

from math import*
from copy import*
from copy import deepcopy

import gen_calc_f
from gen_obj_f import*
from vals import*
from star_f import*
from blackhole_f import*

#sun values
sun = star()
sun.mass = 1.989e30
sun.mag_abs = -26.74
sun.lifetime = (10**10) * year
sun.power = 3.846e26
sun.radius = 6.95700e8
sun.grav_surface = 28.02 * gee
sun.push_dict()

#earth values
earth = gen_obj()
earth.mass = 5.972e24
sun.radius = 6.371e6
sun.grav_surface = gee
sun.push_dict()

#proton values
proton = particle()
proton.mass = 1.672621898e-27
proton.charge =	1.6021766208e-19
proton.radius = 0.85e15

#electron values
electron = particle()
electron.mass = 9.10938356e-31
electron.charge =	1.6021766208e-19
