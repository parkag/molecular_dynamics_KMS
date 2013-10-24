from Simulation import Simulation
from visual import *
import csv
from Particle import Particle

class Visualizer(object):

	def __init__(self, p_count=125):
		self.simulation = Simulation()
		self.particle_count = self.simulation.system.particle_count
		self.framerate = 20
		self.L = self.simulation.system.L
		self.ball = [None] * self.particle_count
		self.arr = [None] * self.particle_count
		self.container = sphere(pos =(0,0,0), radius = self.L+0.05, opacity = 0.1, color=color.yellow)
		scene.range = 2*self.L
		self.particles = [None] * self.particle_count

		for i in xrange(self.particle_count):
			self.ball[i] = sphere(color=color.blue, radius = 0.05)
			self.arr[i] = arrow(color=color.red, axis=[0,0,0])

	def show_from_file(self, filename='simulation_output'):
		i=0

		with open(name=filename,mode='rb') as positions_file:
			data_reader = csv.reader(positions_file, delimiter=' ')

			for row in data_reader:
				rate(self.particle_count * self.framerate)

				self.particles[i] = Particle()
				self.particles[i].r = [float(row[0]), float(row[1]), float(row[2])]
				self.particles[i].p = [float(row[3]), float(row[4]), float(row[5])]
				self.ball[i].pos = self.particles[i].r
				self.arr[i].pos = self.ball[i].pos
				self.arr[i].axis = [p/150.0 for p in self.particles[i].p]
				i = (i + 1) % self.particle_count

	def show_real_time(self):
		self.particles = self.simulation.system.particles
		particle_count = self.simulation.system.particle_count

		self.simulation.system.calculate_state()

		for s in xrange(self.simulation.So + self.simulation.Sd):
			self.simulation.system.evolve()
			if(s % self.simulation.Sxyz):
				for i in xrange(particle_count):
					self.ball[i].pos = self.particles[i].r
					self.arr[i].pos = self.ball[i].pos
					self.arr[i].axis = [p/150.0 for p in self.particles[i].p]



if __name__ == '__main__':
	vis = Visualizer()
#	vis.show_from_file()
	vis.show_real_time()
