from collections import namedtuple
import queue
import pysnooper
from collections import defaultdict
import time
import unittest

Edge = namedtuple('Edge', ['vertex', 'weight'])
class DirectedWeightedGraph:
    def __init__(self, v_cnt, adj_list):
        self._v_cnt = v_cnt
        self._adj_list = [[] for _ in range(v_cnt)]
        for i in range(v_cnt):
            for edge in adj_list[i]:
                self._adj_list[i].append(Edge(edge[0], edge[1]))
        
    def iter_neighbors(self, vi):
        """
        variable 
            vi = vertex at index i 
        function
            iterates through neighbor of the vertex at given index vi
        """
        for nb in self._adj_list[vi]:
            yield nb
        
    def iter_vertices(self):
        """
        function
            iterates through all the vertices by Index
        """
        for vi in range(self._v_cnt):
            yield vi
            
    def kruskals_min_spanning_tree(self):
        edge_q = queue.PriorityQueue()
        to_visit = set(e for e in self.iter_vertices)
        mst = []
        
        for vi in range(self._v_cnt):
            for ei in range(len(self._adj_list[vi])):
                edge_q.put((self._adj_list[vi][ei].weight, vi, ei))
                
        while to_visit:
            edge = edge_q.get()
            if edge[1] in to_visit or edge[2] in to_visit:
                mst.append(edge)
                to_visit.discard[edge[1]]
                to_visit.discard[edge[2]]
                
        return mst
            
    def prims_min_spanning_tree(self):
        min_edge = self._adj_list[0][0]
        to_visit = set(e for e in self.iter_vertices)
        end_vertex = []
        mst = []
        for vi in range(self._v_cnt):
            for edge in self._adj_list[vi]:
                if edge.weight < min_edge.weight:
                    min_edge = edge
                    end_vertex = [vi, min_edge.vertex]
                    
        for v in end_vertex:
            to_visit.remove(v)
        to_replace = -1
        
        while to_visit:
            min_edge = self._adj_list[end_vertex[0]][0]
            for vi in end_vertex:
                for edge in self._adj_list[vi]:
                    if edge.vertex in to_visit and edge.weight < min_edge.weight:
                        min_edge = edge
                        to_replace = vi
            end_vertex = [end_vertex[0], min_edge.vertex] if to_replace == end_vertex[1] else [min_edge.vertex, end_vertex[1]]
            to_visit.remove(min_edge.vertex)
            mst.append((vi, edge.vertex, edge.weight))
            
    def dijkstra_min_heap(self, s, e):
        """
        variable
            s : starting vertex
            e : destination vertex
        function
            calculate dijkstra shortest path for each vertex starting from s
            return tuple(shortest path from s to e including s and e, shortest path length)
        Implication
            for Dijkstra algo to have its optimal running time, it must be implemented with fibonacci heap
        """
        
        NO_PRED = -1
        NO_PATH = float('inf')
        
        best_pred = [NO_PRED for _ in range(self._v_cnt)]
        sp_len = [NO_PATH for _ in range(self._v_cnt)]
        pq = queue.PriorityQueue()
        pq.put([0, s])
        sp_len[0] = 0
        unfinished_vertex = set([i for i in range(self._v_cnt)])
        
        while unfinished_vertex:
            v = pq.get()
            while v[1] not in unfinished_vertex:
                v = pq.get()
            unfinished_vertex.remove(v[1])
            for edge in self.iter_neighbors(v[1]):
                if sp_len[edge.vertex] > sp_len[v[1]] + edge.weight:
                    best_pred[edge.vertex] = v[1]
                    sp_len[edge.vertex] = sp_len[v[1]] + edge.weight
                pq.put([sp_len[edge.vertex], edge.vertex])
        
        shortest_path = []
        curr = e
        
        while curr != s:
            shortest_path.append(curr)
            curr = best_pred[curr]
            
        shortest_path.reverse()
        
        return(shortest_path, sp_len[e])
    
    def bellman_ford(self, s , e):
        """
        function
            can handle negative weight edges. Also can detect negative weight cycles
        runtime
            runs in O(VE) time where V = |v| and E = |e|
        """
        NO_PRED = -1
        NO_PATH = float('inf')
        sp_len = [NO_PATH for _ in range(self._v_cnt)]
        best_pred = [NO_PRED for _ in range(self._v_cnt)]
        sp_len[0] = 0
        
        for _ in range(self._v_cnt):
            for vi in range(self._v_cnt):
                for edge in self._adj_list[vi]:
                    if sp_len[edge.vertex] > sp_len[vi] + edge.weight:
                        sp_len[edge.vertex] = sp_len[vi] + edge.weight
                        best_pred[edge.vertex] = vi
        
        for vi in range(self._v_cnt):
            for edge in self._adj_list[vi]:
                if sp_len[edge.vertex] > sp_len[vi] + edge.weight:
                    raise RuntimeError("Negative Weight Cycle found")
        
        shortest_path = []
        curr = e
        
        while curr != s:
            shortest_path.append(curr)
            curr = best_pred[curr]
        
        shortest_path.reverse()
        return (shortest_path, sp_len[e])
         
    
class Test(unittest.TestCase):
    test_cases = [
        (0, 3, ([2,1,3], 9))
    ]
    
    
    test_adj_list = [
            [(1, 10), (2, 3)],
            [(3, 2) , (2, 1)],
            [(1, 4) , (3, 8), (4, 2)],
            [(4, 7)],
            [(3, 9)]
    ]
    test_graph = DirectedWeightedGraph(5, test_adj_list)
    test_functions = [
        test_graph.dijkstra_min_heap,
        test_graph.bellman_ford
    ]
    def test_shortest_path(self):
        num_runs = 100
        function_runtimes = defaultdict(float)
        
        
        for _ in range(num_runs):
            for s, e, expected in self.test_cases:
                for shortest_path in self.test_functions:
                    start = time.process_time()
                    assert(
                    shortest_path(s, e) == expected
                    ), f"{shortest_path.__name__} failed at {s}, {e}"
                    function_runtimes[shortest_path.__name__] += (
                    time.process_time() - start) * 1000
        print(f"{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<25s}: {runtime:.1f}ms")
                        
if __name__ == "__main__":
    unittest.main()