import networkx as nx
from networkx.drawing.nx_agraph import read_dot
import matplotlib.pyplot as plt
import pygraphviz

def production(productions, rules, G, N, i):
    G = nx.convert_node_labels_to_integers(G)
    # Znalezienie labelu wierzchołka lewej strony produkcji
    # mozemy tak zrobić bo wiemy ze lewa strona to tylko 1 wierzchołek
    i=i-1  #no bo numeruje od 1 juz te pliki
    leftside_node = productions[i][0]

    # Znalezienie id wierzcholka o labelu 'X' w grafie G

    lbls = dict(nx.get_node_attributes(G, 'label'))


    id = list(lbls.keys())
    val = list(lbls.values())

    for i in range(len(lbls)):

        if val[i] == leftside_node.strip('"'):
            found = id[i]
            break

    # Tu zapisuje liste wierzchołków adjacentnych do tego z lewej strony produkcji i go usuwam

    nodes_to_connect = list(G.neighbors(found))
    print(nodes_to_connect)
    G.remove_node(found)

    # Tu tworze nowy graf gdzie mam niepołączone grafy poczatkowy G i prawej strony P
    P=productions[i][1]
    F = nx.union(G, P)
    lbls = dict(nx.get_node_attributes(F, 'label'))

    # Według instrukcji osadzenia łączę wierzchołki z listy nodes_to_connect


    lblsP = dict(nx.get_node_attributes(P, 'label'))  # rozdzielam prawą stronę produkcji na id i val bo nie umiem
    idP = list(lblsP.keys())  # operacji na tych grafach xD
    valP = list(lblsP.values())

    for v in nodes_to_connect:  # dla każdego 'wiszącego' węzła szukam w P wezła do ktorego ma
        for p in range(len(valP)):  # byc podpiety według osadzenia, jesli znajde to tworze krawedz
            if valP[p] == rules[i][lbls[v]]:
                print(valP[p], p, v, lbls[v], rules[i][lbls[v]])
                F.add_edge(v, idP[p])

    # Nadaje grafowi nowe nazwy wierzchołków żeby potem uniknąć powtórzeń

    F = nx.convert_node_labels_to_integers(F)
    lbls = dict(nx.get_node_attributes(F, 'label'))
    print(lbls)
    print(list(F.edges()))
    #i chyba ma zwracać F
