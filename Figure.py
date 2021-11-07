class Figure:

    v = 0.0
    density = 0

    def to_string(self, fout):
        f = open(fout, 'a')
        f.write("\n")

    def __init__(self, density):
        self.density = density
        self.v = 0
