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

i = 1
draw(G, "G.png")
# perform i-th production on G  (productions indices starts from 0)
G1 = production(productions, rules, G, i)

draw(G1, "G1.png")
get_stats(G1)
