from transfer import parse
from get_prod import get_prod_func
from get_rules import get_rules_func
from production import production
import networkx as nx
from networkx.drawing.nx_agraph import read_dot
import matplotlib.pyplot as plt
import pygraphviz

N=parse("test.txt") #liczba produkcji plus rozdzialanie
G = read_dot("graph.dot") #wczytuje ten graf
productions=get_prod_func(N) #zwraca tablice z lewymi i prawymi stronami
rules = get_rules_func(N) #zwraca słownik z transf osadzenia
i=1 #my bedziemy wpisywac te produkcje i jakas petla co nie?
production(productions, rules, G, N, i)
