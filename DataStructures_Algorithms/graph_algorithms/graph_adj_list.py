import queue
import time
from collections import defaultdict
import random
import unittest
import pysnooper

class DirectedGraph:
    def __init__(self, adj = None):
        self._adjacency_list = adj
    
    def add_node(self, src, des):
        if src not in self._adjacency_list:
            self._adjacency_list[src] = set()
        self._adjacency_list[src].add(des)
    
    def __iter__(self):
        for s in self._adjacency_list:
            yield s   
    
    def bfs(self, src):
        parents = {src: None}
        frontier = [src]
        i = 1
        level = {src : 0}
        
        while frontier: 
            next_step = []
            for u in frontier:
                for v in self._adjacency_list[u]:
                    if v not in level:
                        level[v] = i
                        parents[v] = u
                        next_step.append(v)
            frontier = next_step
            i +=1 
        return level, parents


    def dfs(self):
        parents = {}
        initial = set()
        to_visit_stack = []
        
        for vertex in self:
            if vertex not in parents:
                initial.add(vertex)
            else:
                continue
                
            to_visit_stack.append(vertex)
            
            while to_visit_stack:
                v = to_visit_stack.pop()
                
                for neighbor in self._adjacency_list[v]:
                    if neighbor not in parents:
                        parents[neighbor] = v
                        to_visit_stack.append(neighbor)
        
        return initial, parents
        
    
    def rec_dfs(self):
        parents = {}
        for s in self._adjacency_list:
            if s not in parents:
                parents[s] = None
                self.dfs_visit(s, parents)
        return parents
        
    def dfs_visit(self, s, parents):
        for vertex in self._adjacency_list[s]:
            if vertex not in parents:
                parents[vertex] = s 
                self.dfs_visit(vertex, parents)
    
    @pysnooper.snoop()
    def contains_cycle(self):
        STATUS_STARTED = 1
        STATUS_FINISHED = 2
        for vertex in self._adjacency_list.keys():
            statuses = {}
            to_visit = [vertex]
            while to_visit:
                v = to_visit.pop()
                if v in statuses:
                    if statuses[v] == STATUS_STARTED:
                        statuses[v] = STATUS_FINISHED
                else:
                    statuses[v] = STATUS_STARTED
                    to_visit.append(v)
                
                for nb in self._adjacency_list[v]:
                    if nb in statuses:
                        if statuses[nb] == STATUS_STARTED:
                            return True
                    else:
                        to_visit.append(nb)
        return False
    
    def topological_sort(self):
        order = []
        visited = set()
        for vertex in self._adjacency_list.keys():
            if vertex in visited:
                continue
            to_visit = [vertex]
            while to_visit:
                pop = to_visit.pop()
                order.append(pop)
                visited.add(pop)
                if pop in visited:
                    continue
                for nb in self._adjacency_list[pop]:
                    to_visit.append(pop)
        order.reverse()
        return order
    
    def reverse_adj_list(self):
        reversed_list = defaultdict(set)
        for vertex, neighbors in self._adjacency_list.items():
            for nb in neighbors:
                reversed_list[nb].add(vertex)
        return reversed_list
    
    def korasaju_scc(self):
        order = self.topological_sort()
        reversed_graph = self.reverse_adj_list()
        visited = set()
        scc = []
        
        while order:
            connected = []
            vertex = order.pop()
            visited.add(vertex)
            dfs_stack = []
            dfs_stack.append(vertex)
            while dfs_stack:
                poped = dfs_stack.pop()
                if poped in visited:        
                    continue
                else:
                    visited.add(poped)
                connected.append(poped)
                for nb in reversed_graph[poped]:
                    if nb not in visited:
                        dfs_stack.append(nb)
            scc.append(connected)

        return scc

if __name__ == "__main__":
    dg = DirectedGraph({1: {2,3}, 2: {4, 5}, 3: {6}, 4: {7}, 5: {7}, 6: {5, 7}, 7:{}})
    # print(dg.bfs(1))
    # print(dg.dfs())
    # print(dg.rec_dfs())
    # print(dg.contains_cycle())
    # print(dg.topological_sort())
    print(dg.korasaju_scc())