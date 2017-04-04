#Michael Ivanitskiy
#Astronomical calculator
#v 0.3.4

from math import*
from copy import*
from copy import deepcopy

from visual import *
from visual.graph import *

import csv


type_float = type(1.1)
type_int = type(1)

#mathematical consts
e = 2.71828
pi = 3.1415926536

#calculation constants
comparison_margin = .05

#physical consts
h = 6.62607004e-34              #planck
k_B = 1.38064852e-23            #boltzman
c = 2.997924e8                  #speed of light
G = 6.67408e-11                 #universal grav
b_wien = h * c / (4.9651 * k_B)                 #wiens displacement
s_b = 2 * (pi**5) * (k_B ** 4) / (15 * (h**3) * (c**2))         #Stefan - Boltzman const (sigma)

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

#dictionary of stellar types
#stellar_type
				
#common values
#TODO - deprecate by declaring objects (sun, earth, etc) with the needed values
class val_repo(object):
	mass_sun = 1.989e30
	mass_earth = 5.972e24
	
	mag_apparent_sun = -26.74
	
	AU = 149597870700
	parsec = 3.08567758149137e16
	ly = 9.460530e15
	
	#year in seconds
	year = 31556925.9747

	power_sun = 3.846e26

	universe_age = 13.82e9 * year

	lifetime_sun = (10**10) * year
	
	radius_sun = 6.95700e8



#class graph_util(object):
#	graph_disp = gdisplay(foreground=color.black, background= color.white,
#                xtitle='Radius (AU)', ytitle='Temp (K)',
#                 xmax=70, xmin=20, ymax=30, ymin=0)
#
#	graph_curve = gcurve(color=color.red)
#
#	def acr_tester(self):
#		#star constants
#		acr_rate = val_repo.mass_sun * 1e-6 / val_repo.year
#
#		radius = val_repo.AU
#
#		while radius <= (val_repo.AU * 150):
#			rate(10)
#			
#			temp = calc.accretion_disk_temp(star_mass, acr_rate, radius)
#
#			if (19<temp<21):
#				print "temp:\t" + str(temp)
#				print "radius:\t" + str(radius/val_repo.AU) + "\n"
#
#			self.graph_curve.plot(pos=(radius/val_repo.AU, temp))
#			
#			radius = radius + val_repo.AU
#
#
#graph = graph_util()




#general, not always obj based calculations
class gen_calc(object):
	#calculate apparent magnitude from luminosity and distance
	def mag_app(self, lum, dist):
		lum_sols = lum/val_repo.power_sun
		mag_apparent = val_repo.mag_apparent_sun - (10**0.4) * log( (lum_sols * ((val_repo.AU/dist)**2) ), 10)
		return mag_apparent

	def mom_angular_sphere(self, radius, mass):
		return 2 * masss * (radius**2) / 5
		
	#calculate absolute magnitude by calling apparent magnitude function for 10 parsecs
	def mag_abs(self, lum):
		return self.mag_app(lum, 10 * val_repo.parsec)
	
	#calculate distance from apparent and absolute magnitude
	def dist_from_magnitudes(self, mag_app, mag_abs):
		dist = ((10**((mag_app - mag_abs) * 0.2 ))) * (10 * val_repo.parsec)
		return dist

	def compare_dicts(self, A, B):
		if len(A) != len(B):
			print "ERROR: mismatched dictionary size"
			print len(A)
			print len(B)
			print "\n"
		for key in A:
			if (type(A[key]) == type_int) or (type(A[key]) == type_float):
				self.compare_val_num(A[key], B[key], key, True)


	#compare numerical values, printing to console
	def compare_val_num(self, A, B, name="variable", margin=comparison_margin, verbose=True):
		diff = abs(A - B)
		if abs(diff/A) > margin:
			if A == -1:
				print name.ljust(14), "\t\thas been set to \t", B
			elif A != -1:
				print name.ljust(14), "\t\thas been modified by ", diff*100, " %"
				if verbose == True:
					print "\t from its original value of ", A, " to ", B


	def accretion_disk_temp(self, mass, acr_rate, radius):
		frac_t = G * mass * acr_rate
		frac_b = 4 * pi * s_b * (radius ** 3)
		return ((frac_t/frac_b)** 0.25)
	
calc = gen_calc()
	
#star object
class star(object):

	def __init__(self):
		#properties
		self.name = "null"
		self.on_MS = True
		self.spectral_type = "null"
		
		self.mass = -1
		self.mass_sols = -1
		self.radius = -1
		self.temp = -1
		self.grav_surface = -1
		self.L_peak = -1
		self.power = -1
		self.power_sols = -1
		self.mag_abs = -1
		self.E_grav = -1
		self.lifetime = -1
		self.junk = -1
	
		#dictionary with properties
		self.vals = {}
		#fill dictionary
		self.push_dict()
	
	#function to push values onto dictionary
	def push_dict(self):
		self.vals["name"] = self.name
		self.vals["on_MS"] = self.on_MS
		self.vals["spectral_type"] = self.spectral_type
		
		self.vals["mass"] = self.mass
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
		self.vals["junk"] = self.junk
	
	#SETTER FUNCTIONS
	
	#set mass
	def set_mass(self, mass, approx=True):
		self.push_dict()
		vals_init = deepcopy(self.vals)
		
		self.mass_sols = mass / val_repo.mass_sun
		self.mass = mass
		if (approx==True): 
			if (self.on_MS==True):
				#calculate APPROXIMATE lifetime (if on main sequence)
				self.lifetime = val_repo.lifetime_sun * (self.mass_sols**(-2.5))
				self.calc_from_mass()

		print "checking set_mass changes"
		self.push_dict()
		calc.compare_dicts(vals_init, self.vals)
		
		
	#set peak wavelength
	def set_Lpeak(self, L):
		self.push_dict()
		vals_init = deepcopy(self.vals)
		
		self.L_peak = L
		self.temp = b_wien / L

		print "checking set_Lpeak changes"
		self.push_dict()
		calc.compare_dicts(vals_init, self.vals)
	
	
	#set temperature
	def set_temp(self, T):
		self.push_dict()
		vals_init = deepcopy(self.vals)
		
		self.temp = T
		self.L_peak = b_wien / T

		print "checking set_temp changes"
		self.push_dict()
		calc.compare_dicts(vals_init, self.vals)
		

	#set luminosity/power
	def set_lum(self, lum, approx=True):
		self.push_dict()
		vals_init = deepcopy(self.vals)
		
		self.power = lum
		self.power_sols = lum/val_repo.power_sun
		self.calc_mag_abs()
		if (approx==True) and (self.on_MS==True):
			#assuming on main sequence, approximate mass from luminosity
			self.mass_sols = (self.power_sols)**(1/3.5)
			self.set_mass(self.mass_sols * val_repo.mass_sun, True)

		print "checking set_lum changes"
		self.push_dict()
		calc.compare_dicts(vals_init, self.vals)
		
		
	#set spectral type
	def set_spectype(self, spectype, approx=True):
		self.push_dict()
		vals_init = deepcopy(self.vals)
		
		self.spectral_type = spectype
		self.set_temp(spectral_type_temp[spectype])
		if (self.on_MS==True) and (approx==True):
			self.set_lum(spectral_type_lum_MS[spectype] * val_repo.power_sun, True)                
		
		print "checking set_spectype changes"
		self.push_dict()
		calc.compare_dicts(vals_init, self.vals)

	
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
		self.power = self.power_sols * val_repo.power_sun
		
		self.push_dict()
		calc.compare_dicts(vals_init, self.vals)
	
	
	#OTHER CALCULATIONS
	
	#calculate gravitational potential energy
	def calc_energy_grav(self, radius_final):
		self.push_dict()
		vals_init = deepcopy(self.vals)
		
		self.E_grav = G * self.mass * (1/self.radius - 1/radius_final)
		
		self.push_dict()
		calc.compare_dicts(vals_init, self.vals)

	
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
		
		self.push_dict()
		calc.compare_dicts(vals_init, self.vals)
		
		
	def calc_mag_app(self, dist):
		mag_app = calc.mag_app(self, self.power, dist)
		return mag_app
		
	
#black hole object
class black_hole(object):

	#properties
	mass = -1
	radius = -1
	temp = -1
	time_evaporation = -1
	grav_surface = -1
	L_peak = -1
	power = -1
	
	#setting mass recalculates all other properties
	def set_mass(self, m):
		self.mass = m
	
		self.radius = (2 * G * m)/(c**2)
		self.temp = h*(c**3) / ( 8 * pi * G * k_B * m)
		
		self.time_evaporation = 5120 * pi * (G**2) * (m**3) / ( h * (c**4) )
		self.grav_surface = (c**4)/(4 * G * m)
		self.L_peak = b_wien/self.temp
		self.power = h * (c**6) / ( 15360 * pi * ((G * m) ** 2) )
		
	def set_radius(self, r_S):
		self.radius = r_S
		m = r_S * (c**2) * .5 / G
		set_mass(m)
		
	def set_temp(self, T):
		self.temp = T
		m = h*(c**3) / ( 8 * pi * G * k_B * m)
		set_mass(m)



teststar = star()

#teststar.set_mass(1.4 * val_repo.mass_sun, True)

#print teststar.lifetime/val_repo.year

#print (2 * G * val_repo.mass_sun * (10**4) / (5 * val_repo.parsec))**.5

#print calc.dist_from_magnitudes(28.0, -6.91) / val_repo.parsec
#print calc.dist_from_magnitudes(7.0, 2.0) / val_repo.parsec
#print calc.dist_from_magnitudes(12.0, 7.0) / val_repo.parsec

#print ( 50.3 * val_repo.parsec ) / (220000)

#teststar.on_MS = True
#teststar.set_spectype("O5")
#print teststar.lifetime / val_repo.year

#graph.acr_tester()

#n_test = 300 * 10 * ((val_repo.parsec)**(-2)) * pi * (val_repo.radius_sun)**2

#n_test_2 = 10 * pi * ((2.255e-8)**2) * 300

#n_test_3 = val_repo.mass_sun * (10**11) * 1000

#n_test_4 = ((3000*val_repo.parsec)**3) * pi * 4/3

#print n_test_3
#print n_test_4
#print (n_test_3/n_test_4)
#print (n_test_3/(n_test_4 * 1.6737e-27))






print calc.dist_from_magnitudes(7.9, -23.3)
print calc.dist_from_magnitudes(7.9, -23.3)/val_repo.parsec







input("Press enter to exit")














