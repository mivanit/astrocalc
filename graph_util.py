#Michael Ivanitskiy
#Astronomical calculator
#version 0.4.0
#graph utility class

class graph_util(object):
	graph_disp = gdisplay(foreground=color.black, background= color.white,
                xtitle='Radius (AU)', ytitle='Temp (K)',
                 xmax=70, xmin=20, ymax=30, ymin=0)

	graph_curve = gcurve(color=color.red)

	def acr_tester(self):
		#star constants
		acr_rate = val_repo.mass_sun * 1e-6 / val_repo.year

		radius = val_repo.AU

		while radius <= (val_repo.AU * 150):
			rate(10)
			
			temp = calc.accretion_disk_temp(star_mass, acr_rate, radius)

			if (19<temp<21):
				print "temp:\t" + str(temp)
				print "radius:\t" + str(radius/val_repo.AU) + "\n"

			self.graph_curve.plot(pos=(radius/val_repo.AU, temp))
			
			radius = radius + val_repo.AU

