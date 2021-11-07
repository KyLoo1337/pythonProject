import math

from Figure import Figure


class Tetrahedron(Figure):
    edge = 0

    def __init__(self, edge, density):
        super().__init__(density)
        self.edge = edge
        self.v = math.sqrt(3) * self.edge

    def to_string(self, fout):
        f = open(fout, 'a')
        f.write("3.\nTetrahedron\nEdge = {}\nDensity = {}\nSurface area = {:.3f}\n".format(self.edge, self.density, self.v))