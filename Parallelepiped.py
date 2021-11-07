from Figure import Figure


class Parallelepiped(Figure):
    edge_len = [0, 0, 0]

    def __init__(self, edge_len, density):
        super().__init__(density)
        self.edge_len = edge_len
        self.v = 2 * (self.edge_len[0] * self.edge_len[1] + self.edge_len[1] * self.edge_len[2] + self.edge_len[2] *
                      self.edge_len[0])

    def to_string(self, fout):
        f = open(fout, 'a')
        f.write("2.\nParallelepiped\nEdges: {}\nDensity = {}\nSurface area = {:.3f}".format(self.edge_len, self.density,self.v))
