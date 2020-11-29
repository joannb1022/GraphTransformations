from parsing import *
from production import production
from statistics import *

    # parse input
    # N - number of productions
N = parse("test.txt")
    # G - initial graph
G = read_dot("data/graph.dot")

    # read productions to list of tuples [(Left-side, Right-side)]
productions = get_prod_func(N)

    # read rules to dict
rules = get_rules_func(N)


def production_gui(i):
    G1=production(productions, rules, G, i)
    if G1 is not None:
        draw(G1, "G1.png")
        nodes=nodes_gui(G1)

        return G1
production_gui(3)
