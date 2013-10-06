from math import sqrt

class Particle(object):
    r = [None] * 3
    p = [None] * 3
    F = [None] * 3

    def __init__(self):
        pass

    def abs_r(self):
        return sqrt(self.r[0]**2 + self.r[1]**2 + self.r[2]**2)

    def abs_p(self):
        return sqrt(self.p[0]**2 + self.p[1]**2 + self.p[2]**2)

    def abs_F(self):
        return sqrt(self.F[0]**2 + self.F[1]**2 + self.F[2]**2)
