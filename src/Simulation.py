from ClosedSystem import ClosedSystem

class Simulation(object):

    system = [None]

    So = 100
    Sd = 2000
    Sout = 10
    Sxyz = 10

    def __init__(self):
        self.system = ClosedSystem()
        self.system.create_particles()

    def start(self):
        self.system.calculate_state()
        for s in xrange(self.So + self.Sd):
            self.system.evolve()
            if ( s % self.Sout == 0 ):
                #zapis t, H, V, T, P do pliku
                pass
            if ( s % self.Sxyz == 0 ):
                #zapis r[][], E[] do avs.dat (x,y,z,E)
                for particle in self.system.particles:
                    print particle.r[0], particle.r[1], particle.r[2], particle.abs_p() ** 2 / (2*self.system.m)
                pass
            if ( s > self.So ):
                #akumulacja wartosci usrednianych T', P', H'
                pass

def main():
   experiment = Simulation()
   experiment.start()

if __name__ == "__main__":
    main()
