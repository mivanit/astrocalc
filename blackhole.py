#Michael Ivanitskiy
#Astronomical calculator
#version 0.4.0
#star object

import graph_util
import gen_calc
import gen_obj
import star
import solar_val

#black hole object
class black_hole(gen_obj):
	def __init__(self):
			#call parent constructor
			super(gen_obj,self).__init__()			
			lifetime = -1
			L_peak = -1
		
	#function to push values onto dictionary
	def push_dict(self):
		self.push_dict()
		vals_init = deepcopy(self.vals)
		
		super(gen_obj,self).push_dict()
		
		self.vals["L_peak"] = self.L_peak
		self.vals["lifetime"] = self.lifetime

		
	#setting mass recalculates all other properties
	def set_mass(self, m):
		self.push_dict()
		vals_init = deepcopy(self.vals)
		
		self.mass = m
	
		self.radius = (2 * G * m)/(c**2)
		self.temp = h*(c**3) / ( 8 * pi * G * k_B * m)
		
		self.lifetime = 5120 * pi * (G**2) * (m**3) / ( h * (c**4) )
		self.grav_surface = (c**4)/(4 * G * m)
		self.L_peak = b_wien/self.temp
		self.power = h * (c**6) / ( 15360 * pi * ((G * m) ** 2) )
		
		self.check_changes("set_mass", vals_init, self.vals)
		
	def set_radius(self, r_S):
		self.push_dict()
		vals_init = deepcopy(self.vals)
		
		self.radius = r_S
		m = r_S * (c**2) * .5 / G
		set_mass(m)
		
		self.check_changes("set_radius", vals_init, self.vals)
		
	def set_temp(self, T):
		self.push_dict()
		vals_init = deepcopy(self.vals)
		
		self.temp = T
		m = h*(c**3) / ( 8 * pi * G * k_B * m)
		set_mass(m)
		
		self.check_changes("set_temp", vals_init, self.vals)

		