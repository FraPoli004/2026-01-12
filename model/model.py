import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodi = None
        self._grafo = nx.Graph()
        self._idMap = {}

    def getAnni(self):
        return DAO.getAllYears()

    def get_numnodi(self):
        return len(self._grafo.nodes())
    def get_numarchi(self):
        return len(self._grafo.edges())

    def buildGraph(self, ai, af):
        self._grafo.clear()
        self._idMap = {}
        self._nodi = DAO.getAllNodes(ai, af)
        for n in self._nodi:
            self._grafo.add_node(n)
            self._idMap[n.constructorId] = n
