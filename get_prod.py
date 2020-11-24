import networkx as nx
from networkx.drawing.nx_agraph import read_dot
import matplotlib.pyplot as plt
import pygraphviz

def get_prod_func(N):
    prod=[[0 for i in range(2)] for j in range(N)]
    i=0
    with open("left_sides.txt", "r") as left:
        while i<N:
            for label in left:
                if label not in "\n":
                    prod[i][0] = label.strip('\n')
                    filename= "P%s.dot" % str (i+1)
                    P=read_dot(filename)
                    prod[i][1] = P
                    i+=1

    return (prod)
