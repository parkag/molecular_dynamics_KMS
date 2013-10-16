from __future__ import print_function
from ClosedSystem import ClosedSystem

class Simulation(object):

    system = [None]

    So = 100
    Sd = 20000
    Sout = 100
    Sxyz = 100

    xyzFile = open('simulation_output', 'w')
    stateFile = open('state_output', 'w')

    def __init__(self):
        self.system = ClosedSystem()
        self.system.create_particles()

    def start(self):
        self.system.calculate_state()
        for s in xrange(self.So + self.Sd):
            self.system.evolve()
            if ( s % self.Sout == 0 ):
                #zapis t, H, V, T, P do pliku
                print( self.system.T, self.system.P, self.system.V, self.system.Ek+self.system.V, file=self.stateFile)
            if ( s % self.Sxyz == 0 ):
                #zapis r[][], E[] do avs.dat (x,y,z,E)
                for particle in self.system.particles:
                    print(particle.r[0], particle.r[1], particle.r[2], file = self.xyzFile)
                    #print(particle.r[0], particle.r[1], particle.r[2], particle.abs_p() ** 2 / (2*self.system.m), file=self.xyzFile)
                    #print(particle.p[0], particle.p[1], particle.p[2], file = self.xyzFile)
            if ( s > self.So ):
                #akumulacja wartosci usrednianych T', P', H'
                pass

        self.xyzFile.close()
        self.stateFile.close()

def main():
   experiment = Simulation()
   experiment.start()

if __name__ == "__main__":
    main()
