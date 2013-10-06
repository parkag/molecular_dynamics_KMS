from math import sqrt, log
import random
from Particle import Particle


class ClosedSystem(object):
    """
    Contains whole world of the simulation
    """
    n = 5       # number of atoms along one side of the crystal
    m = 40.0    # mass of each atom [u]
    eps = 1.0	# minimal potential energy of each atom
    f = 1e4     # flexibility of the gas container [kJ/mol * nm^-2]
    L = 2.2     # radius of the spherical container [nm]
    a = 0.38    # lattice constant [nm]
    R = 0.38    # distance between atoms that minimizes V [nm]
    T0 = 1000   # initial temperature [K]
    tau = 3e-3  # time step [ps]

    k = 8.31e-3  # Boltzmann constant [kJ/mol * K^-1]

    V = 0       # Potential Energy [kJ/mol]
    P = 0       # current pressure on the container walls [16.6 atm]
    Ek = 0      # Kinetic energy [kJ/mol]
    T = 0       # Current temperature [K]

    particle_count = n ** 3
    particles = [None] * particle_count

    def __init__(self):
        pass

    def create_particles(self):
        # basis vectors for creating the initial crystal structure
        b1 = [self.a, 0.0, 0.0]
        b2 = [self.a / 2.0, self.a * sqrt(3.0) / 2.0, 0.0]
        b3 = [self.a / 2.0, self.a * sqrt(3.0) / 6.0, self.a * sqrt(2.0 / 3.0)]

        curr_ind = 0
        for i in xrange(self.n):
            i_part = (i - (self.n - 1) / 2.0)
            for j in xrange(self.n):
                j_part = (j - (self.n - 1) / 2.0)
                for k in xrange(self.n):
                    k_part = (k - (self.n - 1) / 2.0)

                    self.particles[curr_ind] = Particle()
                    self.particles[curr_ind].r = [0, 0, 0]  # wtf? :P
                    for d in xrange(3):
                        self.particles[curr_ind].r[d] = (i_part * b1[d] + j_part * b2[d] + k_part * b3[d])
                        self.particles[curr_ind].p[d] = random.choice([-1, 1]) * sqrt(2 * self.m * (-0.5 * self.k * self.T0 * log(random.uniform(0, 1))))

                    curr_ind += 1

    def calculate_state(self):
        self.V = 0.0
        Vs = 0.0
        self.P = 0.0
        ri = 0
        for i in xrange(self.particle_count):
            #(10) potencjaly od scianek do V
            ri = self.particles[i].abs_r()
            if ri >= self.L:
                Vs = 0.5 * self.f * (ri - self.L) ** 2
            else:
                Vs = 0.0

            #(14) sily odpychania od scianek do Fi
            if ri >= self.L:
                for d in xrange(3):
                    self.particles[i].F[d] = self.f * (self.L - ri) * self.particles[i].r[d] / ri
            else:
                self.particles[i].F = [0.0, 0.0, 0.0]

            #(15) akumulacja cisnienia chwilowego
            self.P += 1 / (4 * 3.14 * self.L ** 2) * self.particles[i].abs_F()

            for j in xrange(i - 1):
                if (i != j):
                    rij = sqrt((self.particles[j].r[0] - self.particles[i].r[0]) ** 2 + (self.particles[j].r[1] - self.particles[i].r[1]) ** 2 + (self.particles[j].r[2] - self.particles[i].r[2]) ** 2)

                    #potencjaly par atomowych (9) i akumulacja do V (11)
                    self.V += self.eps * ( (self.R / rij) ** 12 - 2 * (self.R / rij) ** 6)

                    #sily miedzyatomowe(13) do Fi, Fj, pamietajac ze (Fpji = - Fpij)
                    for d in xrange(3):
                        self.particles[i].F[d] += 12 * self.eps * ((self.R/rij) ** 12 - (self.R / rij) ** 6) * (self.particles[i].r[d] - self.particles[j].r[d]) / rij**2

            self.V += Vs

    def evolve(self):
        self.Ek = 0.0
        #modyfikacja pedow (18a)
        for i in xrange(self.particle_count):
            for d in xrange(3):
                self.particles[i].p[d] += 0.5 * self.particles[i].F[d] * self.tau
                #modyfikacja polozen (18b)
                self.particles[i].r[d] += self.tau/self.m * self.particles[i].p[d]

        #obliczenie nowego potencjalu, sil, chwilowego cisnienia (alg2)
        self.calculate_state()
        for i in xrange(self.particle_count):
            for d in xrange(3):
                #modyfikacja pedow (18c)
                self.particles[i].p[d] += 0.5 * self.particles[i].F[d] * self.tau
                #obliczenie T (19), E (16)
            self.Ek += self.particles[i].abs_p() ** 2 / (2 * self.m)

        self.T = 2.0 / (3.0 * self.particle_count * self.k) * self.Ek


def main():
    system = ClosedSystem()
    system.create_particles()

    for particle in system.particles:
        print particle.r[0], particle.r[1], particle.r[2]

    system.calculate_state()
    for i in xrange(200):
        system.evolve()
        for particle in system.particles:
            print particle.r[0], particle.r[1], particle.r[2]

if __name__ == "__main__":
    main()
