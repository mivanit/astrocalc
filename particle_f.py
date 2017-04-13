#Michael Ivanitskiy
#Astronomical calculator
#version 0.4.1
#particle object

#used mostly for elementary particles

from math import*
from copy import*
from copy import deepcopy

import gen_calc_f
from gen_obj_f import gen_obj
from vals import*
from vals_obj import*

class particle(gen_obj):
	def __init__(self):
		self.charge = 0

		#call parent constructor
		#called after variables because push_dict inheritance is weird
		super(star, self).__init__()

		#fill dictionary
		self.push_dict()

	#function to push values onto dictionary
	def push_dict(self):
		#parent push dictionary function for universal vars
		super(star,self).push_dict()

		self.vals["charge"] = self.charge
