from __future__ import print_function
from ClosedSystem import ClosedSystem
import ConfigParser

class Simulation(object):

    def __init__(self):
        self.system = ClosedSystem()

        config = ConfigParser.ConfigParser()
        config.read('parameters.ini')
        self.system.n = config.getint('System parameters', 'n')
        self.system.m = config.getfloat('System parameters', 'm')
        self.system.eps = config.getfloat('System parameters', 'eps')
        self.system.R = config.getfloat('System parameters', 'R')
        self.system.f = config.getfloat('System parameters', 'f')
        self.system.L = config.getfloat('System parameters', 'L')
        self.system.a = config.getfloat('System parameters', 'a')
        self.system.T0 = config.getfloat('System parameters', 'T0')
        self.system.tau = config.getfloat('System parameters', 'tau')

        self.So = config.getint('File management parameters', 'So')
        self.Sd = config.getint('File management parameters', 'Sd')
        self.Sout = config.getint('File management parameters', 'Sout')
        self.Sxyz = config.getint('File management parameters', 'Sxyz')

        self.system.create_particles()

    def start_calculation(self):
        self.xyzFile = open('simulation_output', 'w')
        self.stateFile = open('state_output', 'w')
        self.system.calculate_state()
        for s in xrange(self.So + self.Sd):
            self.system.evolve()
            if ( s % self.Sout == 0 ):
                #zapis t, H, V, T, P do pliku
                print(s*self.system.tau, self.system.T, self.system.P/16.6, self.system.V, self.system.Ek+self.system.V, file=self.stateFile)
            if ( s % self.Sxyz == 0 ):
                #zapis r[][], E[] do avs.dat (r,p)
                for particle in self.system.particles:
                    print(particle.r[0], particle.r[1], particle.r[2], particle.p[0], particle.p[1], particle.p[2], file = self.xyzFile)    

            if ( s > self.So ):
                #akumulacja wartosci usrednianych T', P', H'
                pass

        self.xyzFile.close()
        self.stateFile.close()


def main():
   experiment = Simulation()
   experiment.start_calculation()

if __name__ == "__main__":
    main()
