from math import sqrt

class Particle(object):

    def __init__(self):
        self.r = [0.0, 0.0, 0.0]
        self.p = [0.0, 0.0, 0.0]
        self.F = [0.0, 0.0, 0.0]

    def abs_r(self):
        return sqrt(self.r[0]**2 + self.r[1]**2 + self.r[2]**2)

    def abs_p(self):
        return sqrt(self.p[0]**2 + self.p[1]**2 + self.p[2]**2)

    def abs_F(self):
        return sqrt(self.F[0]**2 + self.F[1]**2 + self.F[2]**2)

    def distance(self, par):
        return sqrt( (self.r[0] - par.r[0]) ** 2 + (self.r[1] - par.r[1]) ** 2 + (self.r[2] - par.r[2]) ** 2 )

