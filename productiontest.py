import networkx as nx
from networkx.drawing.nx_agraph import read_dot
import matplotlib.pyplot as plt
import pygraphviz

N = 1  # liczba produkcji to musi być zwracane przez poprzednie funkcje
#G = read_dot("graph.dot")
L = read_dot("L1.dot")
P = read_dot("P1.dot")
G = nx.convert_node_labels_to_integers(G)

# czyta z pliku rules produkcje i wrzuce je do słownika
rules = [{} for _ in range(N)]
i = 0
with open("rules.txt") as f:
    for i in range(N):
        line = f.readline()
        while line != "\n" and line != '':
            (key, val) = line.split()
            print(key, val, i)
            rules[i][key] = val
            line = f.readline()

print(rules)

# Znalezienie labelu wierzchołka lewej strony produkcji
# mozemy tak zrobić bo wiemy ze lewa strona to tylko 1 wierzchołek

leftside_node = list(dict(nx.get_node_attributes(L, 'label')).values())[0]
print(leftside_node)

# Znalezienie id wierzcholka o labelu 'X' w grafie G

lbls = dict(nx.get_node_attributes(G, 'label'))
print(lbls)

id = list(lbls.keys())
val = list(lbls.values())

for i in range(len(lbls)):
    if val[i] == leftside_node:
        found = id[i]
        break

# Tu zapisuje liste wierzchołków adjacentnych do tego z lewej strony produkcji i go usuwam

nodes_to_connect = list(G.neighbors(found))
print(nodes_to_connect)
G.remove_node(found)

# Tu tworze nowy graf gdzie mam niepołączone grafy poczatkowy G i prawej strony P

F = nx.union(G, P)
lbls = dict(nx.get_node_attributes(F, 'label'))

# Według instrukcji osadzenia łączę wierzchołki z listy nodes_to_connect
i = 0  # numer produkcji

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
