#Michael Ivanitskiy
#Astronomical calculator
#version 0.4.1
#graph utility class

from visual import *
from visual.graph import *

import vals
import gen_calc_f

class graph_util(object):
	graph_disp = gdisplay(foreground=color.black, background= color.white,
                xtitle='Radius (AU)', ytitle='Temp (K)',
                 xmax=70, xmin=20, ymax=30, ymin=0)

	graph_curve = gcurve(color=color.red)

	def acr_tester(self):
		#star constants
		acr_rate = sun.mass * 1e-6 / year

		radius = AU

		while radius <= (AU * 150):
			rate(10)
			
			temp = calc.accretion_disk_temp(star_mass, acr_rate, radius)

			if (19<temp<21):
				print "temp:\t" + str(temp)
				print "radius:\t" + str(radius/AU) + "\n"

			self.graph_curve.plot(pos=(radius/AU, temp))
			
			radius = radius + AU

