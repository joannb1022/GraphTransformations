import networkx as nx
import matplotlib.pyplot as plt


def draw(G, filename):
    plt.clf()
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, node_size=500, labels=labels)
    plt.draw()
    plt.savefig(filename, format="PNG", dpi=80)


# average degree of all nodes
def avg_degree_all(G):
    degs = nx.degree(G)
    deg = list(map((lambda tup: tup[1]), degs))
    return round(sum(deg) / len(deg), 2)


# average degree of non terminal nodes
def avg_degree_terminal(G):
    degs = nx.degree(G)
    lbls = dict(nx.get_node_attributes(G, 'label'))
    deg = []
    for d in degs:
        if lbls[d[0]] != 'Y' and lbls[d[0]] != 'X':
            deg.append(d[1])
    return round(sum(deg) / len(deg), 2)


def get_stats(G):
    nodes = nx.number_of_nodes(G)
    edges = nx.number_of_edges(G)
    con_comp = nx.number_connected_components(G)
    avg_deg_all = avg_degree_all(G)
    avg_deg_T = avg_degree_terminal(G)
    print("Liczba wierzchołków: ", nodes)
    print("Liczba krawędzi: ", edges)
    print("Liczba spójnych składowych: ", con_comp)
    print("Średni stopień wierzchołków: ", avg_deg_all)
    print("Średni stopień wierzchołków terminalnych: ", avg_deg_T)
    print("Średnia liczba wierzchołków w spójnych składowych: ", avg_deg_all/con_comp)

def nodes_gui(G):
    nodes = nx.number_of_nodes(G)
    return nodes
