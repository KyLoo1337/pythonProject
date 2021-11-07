import math

from Figure import Figure


class Ball(Figure):

    r = 0

    def __init__(self, r, density):
        super().__init__(density)
        self.r = r
        self.v = 4.0*math.pi*r*r

    def to_string(self, fout):
        f = open(fout, 'a')
        f.write("1.\nBall\nR = {}\ndensity = {}\nsurface area = {:.3f}\n".format(self.r, self.density, self.v))
