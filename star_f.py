#Michael Ivanitskiy
#Astronomical calculator
#version 0.4.1
#star object

from math import*
from copy import*
from copy import deepcopy

import gen_calc_f
from gen_obj_f import gen_obj
from vals import*
from vals_obj import*

#dictionary of spectral types to temperature
spectral_type_temp = {}
#dictionary of spectral type to luminosity (in sols) on main sequence
spectral_type_lum_MS = {}

with open("specType_MS.txt","r") as f_spec:
	data =[x.strip().split('\t') for x in f_spec]
	rows = len(data)
	for i in range(0, rows):
		v_spec = data[i][0]
		spectral_type_temp[v_spec] = float(data[i][1])
		spectral_type_lum_MS[v_spec] = float(data[i][3])

#TODO - dictionary of stellar types

#star object
class star(gen_obj):

	def __init__(self):
		#declare class specific vars
		self.on_MS = True		#bool for whether star is on main sequence
		#change this to distance from MS?
		self.spectral_type = "null"

		self.mass_sols = -1		#mass, in solar units
		self.L_peak = -1		#peak emission wavelength
		self.power_sols = -1	#power, in solar units
		self.E_grav = -1		#gravitational collapse potential energy
		self.lifetime = -1		#lifestpan

		#call parent constructor
		#called after variables because push_dict inheritance is weird
		super(star, self).__init__()

		#fill dictionary
		self.push_dict()


	#function to push values onto dictionary
	def push_dict(self):
		#parent push dictionary function for universal vars
		super(star,self).push_dict()

		self.vals["on_MS"] = self.on_MS
		self.vals["spectral_type"] = self.spectral_type
		self.vals["mass_sols"] = self.mass_sols
		self.vals["radius"] = self.radius
		self.vals["temp"] = self.temp
		self.vals["grav_surface"] = self.grav_surface
		self.vals["L_peak"] = self.L_peak
		self.vals["power"] = self.power
		self.vals["power_sols"] = self.power_sols
		self.vals["mag_abs"] = self.mag_abs
		self.vals["E_grav"] = self.E_grav
		self.vals["lifetime"] = self.lifetime

	#SETTER FUNCTIONS

	#set mass
	def set_mass(self, mass, approx=True):
		self.push_dict()
		vals_init = deepcopy(self.vals)

		self.mass_sols = mass / sun.mass
		self.mass = mass
		if (approx==True):
			if (self.on_MS==True):
				#calculate APPROXIMATE lifetime (if on main sequence)
				self.lifetime = sun.lifetime * (self.mass_sols**(-2.5))
				self.calc_from_mass()

		self.check_changes("set_mass", vals_init, self.vals)


	#set peak wavelength
	def set_Lpeak(self, L):
		self.push_dict()
		vals_init = deepcopy(self.vals)

		self.L_peak = L
		self.temp = b_wien / L

		self.check_changes("set_Lpeak", vals_init, self.vals)


	#set temperature
	def set_temp(self, T):
		self.push_dict()
		vals_init = deepcopy(self.vals)

		self.temp = T
		self.L_peak = b_wien / T
		if radius > 0:
			temp_power = (T**4)*s_b*4*pi*(self.radius**2)
			self.set_lum(temp_power)

		self.check_changes("set_temp", vals_init, self.vals)


	#set luminosity/power
	def set_lum(self, lum, approx=True):
		self.push_dict()
		vals_init = deepcopy(self.vals)

		self.power = lum
		self.power_sols = lum/sun.power
		self.calc_mag_abs()
		if (approx==True) and (self.on_MS==True):
			#assuming on main sequence, approximate mass from luminosity
			self.mass_sols = (self.power_sols)**(1/3.5)
			self.set_mass(self.mass_sols * sun.mass, True)

		self.check_changes("set_lum", vals_init, self.vals)


	#set spectral type
	def set_spectype(self, spectype, approx=True):
		self.push_dict()
		vals_init = deepcopy(self.vals)

		self.spectral_type = spectype
		self.set_temp(spectral_type_temp[spectype])
		if (self.on_MS==True) and (approx==True):
			self.set_lum(spectral_type_lum_MS[spectype] * sun.power, True)

		self.check_changes("set_spectype", vals_init, self.vals)


	#APPROXIMATE CALCULATIONS

	#perform approximate luminosity calculation from mass
	def calc_from_mass(self):
		self.push_dict()
		vals_init = deepcopy(self.vals)

		a = 3.5
		coeff = 1

		if (self.mass_sols < 20):
			if (self.mass_sols < 0.43):
				a = 2.3
				coeff = .23
			elif (self.mass_sols < 2):
				a = 4
				coeff = 1
			elif (self.mass_sols < 20):
				a = 3.5
				coeff = 1.5
		else:
			a = 1
			coeff = 3200

		self.power_sols = coeff * (self.mass_sols ** a)
		self.power = self.power_sols * sun.power

		self.check_changes("calc_from_mass", vals_init, self.vals)


	#OTHER CALCULATIONS

	#calculate gravitational potential energy
	def calc_energy_grav(self, radius_final):
		self.push_dict()
		vals_init = deepcopy(self.vals)

		self.E_grav = G * self.mass * (1/self.radius - 1/radius_final)

		self.check_changes("calc_energy_grav", vals_init, self.vals)


	#calculate intensity of a star at temp T for a wavelength L
	def calc_power_at_L(self, L):
		intensity = 2*h*(c**2) / ( (L**5) * (e**( h * c /( L*k*self.temp )) - 1 ) )
		return intensity

	#trivial
	#call absolute and apparent magnitude functions
	def calc_mag_abs(self):
		self.push_dict()
		vals_init = deepcopy(self.vals)

		self.mag_abs = calc.mag_abs(self.power)
		return self.mag_abs

		self.check_changes("calc_mag_abs", vals_init, self.vals)


	def calc_mag_app(self, dist):
		mag_app = calc.mag_app(self, self.power, dist)
		return mag_app
