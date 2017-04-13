#Michael Ivanitskiy
#Astronomical calculator
#version 0.4.1
#general object

from math import*
from copy import*
from copy import deepcopy

from vals import *

class gen_obj(object):

	def __init__(self):
		#basic properties
		self.name = "null"		#object name
		self.mass = -1			#mass
		self.radius = -1				#radius
		self.temp = -1				#surface temperature
		self.grav_surface = -1		#surface gravity
		self.power = -1				#emissive power
		self.mag_abs = -1		#absolute magnitude

		self.junk = -1			#junk variable for testing

		#declare dictionary with properties
		self.vals = {}

		#fill dictionary
		self.push_dict()

	#function to push values onto dictionary
	def push_dict(self):
		self.vals["name"] = self.name
		self.vals["mass"] = self.mass
		self.vals["radius"] = self.radius
		self.vals["temp"] = self.temp
		self.vals["grav_surface"] = self.grav_surface
		self.vals["power"] = self.power
		self.vals["mag_abs"] = self.mag_abs

		self.vals["junk"] = self.junk

	def check_changes(self, name, vals_init, vals):
		print "checking " + name + " changes"
		self.push_dict()
		calc.compare_dicts(vals_init, self.vals)
