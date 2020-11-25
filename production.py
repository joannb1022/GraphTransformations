import networkx as nx


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
    return list(G.neighbors(node))


def get_rightside_graph(productions, i):
    return productions[i][1]


def connect_graphs(F, P, rules, nodes_to_connect, i):
    lblsF = dict(nx.get_node_attributes(F, 'label'))
    lblsP = dict(nx.get_node_attributes(P, 'label'))
    indxP = list(lblsP.keys())
    valP = list(lblsP.values())

    for v in nodes_to_connect:
        for p in range(len(valP)):
            if valP[p] == rules[i][lblsF[v]]:
                F.add_edge(v, indxP[p])


def production(productions, rules, G, i):

    G = nx.convert_node_labels_to_integers(G)
    # productions indexed from 0
    i -= 1

    # get left-side node from i-th production
    leftside_node = get_leftside_node(productions, i)

    # find left-side node in initial graph G
    found = find_node_in_graph(G, leftside_node)

    # get all nodes adjacent to left-side in G
    nodes_to_connect = adjacent_to(G, found)

    # remove left-side from G
    G.remove_node(found)

    # get right-side graph
    P = get_rightside_graph(productions, i)

    # union G and P
    F = nx.union(G, P)

    # connect G and P according to rules[i]
    connect_graphs(F, P, rules, nodes_to_connect, i)

    # re-index nodes to keep consistency
    F = nx.convert_node_labels_to_integers(F)

    # return final graph
    return F
