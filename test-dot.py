import networkx as nx
import pygraphviz
from networkx.drawing.nx_agraph import read_dot
import matplotlib.pyplot as plt

G = read_dot("graph.dot")
#L = read_dot("L0.dot")
#P = read_dot("P0.dot")
'''
nx.draw(G, with_labels=True)
plt.savefig('G.png')
nx.draw(L, with_labels=True)
plt.savefig('L.png')
nx.draw(P, with_labels=True)
plt.savefig('P.png')
'''

lbls = dict(nx.get_node_attributes(G,'label'))
print(lbls)

id = list(lbls.keys())
val= list(lbls.values())

for i in range(len(lbls)):                  # znalezienie id wierzcholka o labelu 'X'
    if val[i] == 'X':
        found = id[i]
        break

nodes_to_connect = list(G.neighbors(found))
print(nodes_to_connect)                      # lista adjacentnych do X
G.remove_node(found)
# tu jakoś łączyc te nody z tymi z prawej strony produkcji według osadzenia


