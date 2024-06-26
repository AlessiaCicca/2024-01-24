import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.metodi=DAO.getMetodi()
        self.grafo = nx.DiGraph()
        self._idMapMetodi = {}
        self._idMapProdotti={}
        self.dict = {}
        self._solBest = []
        self._costBest = 0
        for v in self.metodi:
            self._idMapMetodi[v.Order_method_type] = v.Order_method_code

    def creaGrafo(self, metodoTipo, anno, maggiorazione):
        metodo=self._idMapMetodi[metodoTipo]
        self.nodi = DAO.getNodi(metodo, anno)
        for v in self.nodi:
            self._idMapProdotti[v.Product_number] = v
        self.grafo.add_nodes_from(self.nodi)
        self.dict = DAO.getPrezzoTot(metodo,anno)
        self.addEdges(maggiorazione)
        return self.grafo

    def addEdges(self, maggiorazione):
         self.grafo.clear_edges()
         for nodo1 in self.grafo.nodes:
             for nodo2 in self.grafo.nodes:
                if self.dict[nodo2.Product_number]>=(1+maggiorazione)*float(self.dict[nodo1.Product_number]):
                    if self.grafo.has_edge(nodo1, nodo2) == False:
                      self.grafo.add_edge(nodo1, nodo2)

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def redditizi(self):
        dizio={}
        count=0
        for nodo in self.grafo.nodes:
            if self.grafo.out_degree(nodo)==0:
                dizio[nodo]=self.grafo.in_degree(nodo)
        dizioOrder=dict(sorted(dizio.items(), key=lambda item: item[1], reverse=True))
        redditizi=[]
        for nodo in dizioOrder.keys():
            if count<5:
                count+=1
                redditizi.append((nodo,dizio[nodo],self.dict[nodo.Product_number]))
        return redditizi





