class Graph:
    class Vertex:
        __slots__ = '_element'
        def __init__(self, e):
            self._element = e
        
        def element(self):
            return self._element
        
        def __hash__(self):
            return hash(id(self))
        
    class Edge:
        __slots__ = '_origin', '_destination', '_element'
        def __init__(self, o, d, e):
            self._origin = o
            self._destination = d
            self._element = e
        
        def element(self):
            return self._element
    
        def opposite(self, v):
            return self._destination if v is self._origin else self._origin
        
        def __hash__(self):
            return hash((self._origin, self._destination))
        
        def end_points(self):
            return (self._origin, self._destination)
        
    def __init__(self, directed = False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing
        
    def is_directed(self):
        return self._incoming is not self._outgoing
    
    def vertex_count(self):
        return len(self._outgoing)
    
    def vertices(self):
        for vertex in self._outgoing.keys():
            yield vertex
            
    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2
    
    def edges(self):
        for secondary_map in self._outgoing.values():
            for edge in secondary_map.values():
                yield edge
                
    def get_edge(self, v, u):
        return self._outgoing[v].get(u)
    
    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])
    
    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge
    
    def insert_vertex(self, e):
        v = self.Vertex(e)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v
    
    def insert_edge(self, v, u, e):
        edge = self.Edge(v, u, e)
        self._outgoing[v][u] = edge
        self._incoming[u][v] = edge
        
    def remove_edge(self, edge):
        u, v = edge.end_points()
        del self._outgoing[u][v]
        del self._incoming[v][u]

def topological_sort(g):
    incount = {}
    topo = []
    ready = []
    for v in g.vertices():
        incount[v] = g.degree(v, False)
        if incount[v] == 0:
            ready.append(v)
    while ready:
        u = ready.pop()
        topo.append(u)
        for edge in g.incident_edges(u):
            v = edge.opposite(u)
            incount[v] -= 1
            if incount[v] == 0:
                ready.append(v)
    return topo

def fill_order(g, u, stack, visited):
    visited.add(u)
    for edge in g.incident_edges(u):
        v = edge.opposite(u)
        if v not in visited:
            fill_order(g, v, stack, visited)
    stack.append(u)

def dfs_back(g, u, order, visited):
    order.append(u.element())
    visited.add(u)
    for edge in g.incident_edges(u, False):
        v = edge.opposite(u)
        if v not in visited:
            dfs_back(g, v, order, visited)

def kosaraju(g, u):
    stack = []
    scc = []
    visited = set()
    fill_order(g, u, stack, set())
    while stack:
        connected = []
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            dfs_back(g, u, connected, visited)
            scc.append(connected)
    return scc

import queue

class Parition:
    class Position:
        __slots__ = '_container', '_size', '_element', '_parent'
        def __init__(self, container, element):
            self._container = container
            self._size = 1
            self._element = element
            self._parent = self
        def element(self):
            return self._element
    
    def make_position(self, v):
        return self.Position(self, v)
    
    def find(self, v):
        if v != v._parent:
            self.find(v._parent)
        return v

    def union(p, q):
        a = self.find(p)
        b = self.find(q)
        if a is not b:
            if a._size > b._size:
                b._parent = a
                a._size += b._size
            else:
                a._parent = b
                b._size += a._size

def kruskal(g):
    tree = []
    forest = Partition()
    position = {}
    pq = queue.PriorityQueue()
    for v in g.vertices():
        position[v] = forest.make_position(v)
    for edge in g.edges():
        pq.put(edge.element(), edge)
    size = g.vertex_count()
    while len(tree) != size - 1 and pq:
        weight, edge = pq.get()
        u, v = edge.end_points()
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a is not b:
            tree.append(edge)
            forest.union(a, b)
    return tree

def prim_mst(g):
    tree = []
    d = {}
    pq = AdaptablePriorityQueue()
    pqlocator = {}
    for v in g.vertices():
        if not d:
            d[v] = 0
        else:
            d[v] = float('inf')
        pq.put(d[v],(v, None))
    while pq:
        key, val = pq.get()
        u, edge = val
        del pqlocator[v]
        if edge is not None:
            tree.append(edge)
        for link in g.incident_edges(u):
            v = link.opposite(u)
            if v in pqlocator:
                if d[v] < v.element():
                    d[v] = v.element()
                    pq.update(pqlocator[v], d[v], (v, link))
    return tree

def dijkstra(g, s):
    d = {}
    pq = AdaptablePriorityQueue()
    pqlocator = {}
    anc = {}
    for v in g.vertices():
        if v is s:
            d[v] = 0
        else:
            d[v] = float('inf')
        pqlocator = pq.put(d[v], v)
        anc[v] = None
    while pq:
        u = pq.get()
        del pqlocator[u]
        for edge in g.incident_edges(u):
            v = edge.opposite(u)
            if d[v] > d[u] + edge.element():
                d[v] = d[u] + edge.element()
                anc[v] = u
                pq.update(pqlocator[v], d[v], v)
    return anc, d

def bellman_ford(g, s):
    d  = {}
    anc = {}
    for v in g.vertices():
        if v is s:
            d[v] = 0
        else:
            d[v] = float('inf')
        anc[v] = None
    for _ in range(g.vertex_count()):
        for u in g.vertices():
            for edge in g.incident_edges(u):
                v = edge.opposite(u)
                if d[v] > d[u] + edge.element():
                    d[v] = d[u] + edge.element()
                    anc[v] = u
    for u in g.vertices():
        for edge in g.incident_edges(u):
            v = edge.opposite(u)
            if d[v] > d[u] + edge.element():
                raise RuntimeError("Negative cycle detected")
    return anc, d

def contains_cycle(g):
    STATUS_STARTED = 1
    STATUS_FINISHED = 2
    for vertex in g.vertices():
        statuses = {}
        to_visit = [vertex]
        while to_visit:
            u = to_visit.pop()
            if u in statuses:
                if statuses[u] == STATUS_STARTED:
                    statuses[u] = STATUS_FINISHED
            else:
                statuses[u] = STATUS_STARTED
                to_visit.append(u)
            for edge in g.incident_edges(u):
                v = edge.opposite(u)
                if v in statuses:
                    if statuses[v] == STATUS_STARTED:
                        return True
                else:
                    to_visit.append(v)
    return False

def floyd_marshall(g):
    closure = copy.deepcopy(g)
    verts = list(g.vertices())
    n = len(verts)
    for k in range(n):
        for i in range(n):
            if i != k and closure.get_edge(verts[i], verts[k]) is not None:
                for j in range(n):
                    if i != k != j and closure.get_edge(verts[k], verts[j]) is not None:
                        if closure.get_edge(verts[i], verts[j]):
                            closure.insert_edge(verts[i], verts[j])
    return closure
    
if __name__ == "__main__":
    g = Graph(True)
    v1 = g.insert_vertex(1)
    v2 = g.insert_vertex(2)
    v3 = g.insert_vertex(3)
    v4 = g.insert_vertex(4)
    v5 = g.insert_vertex(5)
    v6 = g.insert_vertex(6)
    
    g.insert_edge(v1, v2, 1)
    g.insert_edge(v2, v3, 1)
    g.insert_edge(v3, v1, 1)
    g.insert_edge(v2, v4, 1)
    g.insert_edge(v4, v5, 1)
    g.insert_edge(v5, v6, 1)
    g.insert_edge(v6, v4, 1)
    
    # print([v.element() for v in topological_sort(g)])
    print(kosaraju(g, v1))