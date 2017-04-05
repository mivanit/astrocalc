#Michael Ivanitskiy
#Astronomical calculator
#version 0.4.0
#general calculation class

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