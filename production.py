import globals
from statistics import *


def get_leftside_node(productions, i):
    return productions[i][0]


def find_node_in_graph(G, leftside_node):
    lbls = dict(nx.get_node_attributes(G, 'label'))
    indx = list(lbls.keys())
    val = list(lbls.values())
    found = None

    for i in range(len(lbls)):

        if val[i] == leftside_node:
            found = indx[i]
            break

    return found


def adjacent_to(G, node):
    print(list(G.neighbors(node)))
    return list(G.neighbors(node))


def get_rightside_graph(productions, i):
    return productions[i][1]


def connect_graphs(F, P, rules, nodes_to_connect, i):
    lblsF = dict(nx.get_node_attributes(F, 'label'))
    lblsP = dict(nx.get_node_attributes(P, 'label'))
    indxP = list(lblsP.keys())
    valP = list(lblsP.values())
    new_edges = []
    for v in nodes_to_connect:
        for p in range(len(valP)):
            if valP[p] == rules[i][lblsF[v]]:
                F.add_edge(v, indxP[p])
                new_edges.append((v, indxP[p]))
    return new_edges


def production(i):
    productions, rules, G, = globals.productions, globals.rules, globals.G

    G = nx.convert_node_labels_to_integers(G)
    # Productions indexed from 0
    i -= 1

    # Get left-side node from i-th production
    leftside_node = get_leftside_node(productions, i)

    # Find left-side node in initial graph G
    found = find_node_in_graph(G, leftside_node)
    if found is None:
        return None

<<<<<<< HEAD
    # Get all nodes adjacent to left-side in G
=======
    if found is None: return None
    # get all nodes adjacent to left-side in G
>>>>>>> 48c682fb5a63624d05e4f0b5eef4fc147050175f
    nodes_to_connect = adjacent_to(G, found)

    # Remove left-side from G
    G.remove_node(found)

    # Get right-side graph
    P = get_rightside_graph(productions, i)
    rightside_edges = list(P.edges)
    rightside_nodes = list(P.nodes)

    # Union G and P
    F = nx.union(G, P)

    # Connect G and P according to rules[i]
    new_edges = connect_graphs(F, P, rules, nodes_to_connect, i)

    # Rraw new graph
    draw(F, new_edges, rightside_edges, rightside_nodes, nodes_to_connect, "G1.png")

    # Re-index nodes to keep consistency
    F = nx.convert_node_labels_to_integers(F)

    # Return final graph
    return F


# For ComboBox options
def get_productions_list():
    p_list = []
    for i in range(globals.N):
        p_list.append("Produkcja {}".format(str(i + 1)))
    return p_list
