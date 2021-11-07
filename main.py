import sys

from Ball import Ball
from Parallelepiped import Parallelepiped
from Tetrahedron import Tetrahedron


def error_msg1():
    print("incorrect qualifier value!\n" + "  Waited:\n" + "main.py infile outfile01 outfile02\n" + "  Or:\n" +
          "main.py number outfile01 outfile02\n")


def shaker_sort(alist):
    def swap(i, j):
        alist[i], alist[j] = alist[j], alist[i]

    upper = len(alist) - 1
    lower = 0

    no_swap = False
    while not no_swap and upper - lower > 1:
        no_swap = True
        for j in range(lower, upper):
            if alist[j + 1].v > alist[j].v:
                swap(j + 1, j)
                no_swap = False
        upper = upper - 1

        for j in range(upper, lower, -1):
            if alist[j - 1].v < alist[j].v:
                swap(j - 1, j)
                no_swap = False
        lower = lower + 1


if __name__ == "__main__":
    if len(sys.argv) != 3:
        error_msg1()
        exit()
    print("Start")
    f = open(sys.argv[1], 'r')
    data = f.readlines()
    f.close()
    figs = []
    for i in range(len(data)):
        if len(data[i].split()) < 2:
            data[i] = data[i].split()
            data[i] = data[i][0]
    for i in range(0, len(data), 3):
        if data[i] == '1':
            r = int(data[i+1])
            dest = int(data[i+2])
            figs.append(Ball(r, dest))
        elif data[i] == '2':
            edge_len = list(map(int, data[i+1].split()))
            dest = int(data[i+2])
            figs.append(Parallelepiped(edge_len, dest))
        elif data[i] == '3':
            edge = int(data[i + 1])
            dest = int(data[i + 2])
            figs.append(Tetrahedron(edge, dest))
    shaker_sort(figs)
    _f = open(sys.argv[2], "w")
    _f.close()
    for fig in figs:
        fig.to_string(sys.argv[2])
