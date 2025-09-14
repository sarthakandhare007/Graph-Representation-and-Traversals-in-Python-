from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    # Add edge (undirected)
    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)  # Comment this for directed graph

    # BFS traversal
    def bfs(self, start):
        visited = set()
        queue = deque()
        visited.add(start)
        queue.append(start)

        print("BFS Traversal:", end=" ")
        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()

    # DFS traversal
    def dfs(self, start):
        visited = set()
        print("DFS Traversal:", end=" ")
        self._dfs_util(start, visited)
        print()

    def _dfs_util(self, node, visited):
        visited.add(node)
        print(node, end=" ")
        
        for neighbor in self.adj_list[node]:
            if neighbor not in visited:
                self._dfs_util(neighbor, visited)

# Test the graph
if __name__ == "__main__":
    graph = Graph()
    
    # Adding edges
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    
    graph.bfs(0)
    graph.dfs(0)
