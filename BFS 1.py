class Node:
    def __init__(self,vertex,weight):
        self.vertex = vertex;
        self.weight = weight



graph = {}

def add_edge(src, dest, wei):
    if src not in graph:
        graph[src] = []
    if dest not in graph:
        graph[dest] = []

    node = Node(dest, wei)
    graph[src].append(node)


def BFS(start):

    q = [start]
    visited = [start]

    while(q):
        n = q.pop(0)
        print (n)

        for i in graph[n]:
            if i.vertex not in visited:
                visited.append(i.vertex)
                q.append(i.vertex)


def find_path(start, end, path = []):
    path = path + [start]
    if(start == end):
        return path
    
    for node in graph[start]:
        if node.vertex not in path:
            new_path = find_path(node.vertex, end, path)
            if new_path:
                return new_path
    return
    
def shortest_path(start, goal):
    try:
        return next(bfs_paths(start, goal))
    except StopIteration:
        return None

    
if __name__ == "__main__":
    add_edge('A', 'B', 5)
    add_edge('A', 'C', 5)
    add_edge('A', 'D', 5)
    add_edge('B', 'E', 5)
    add_edge('B', 'F', 5)
    add_edge('C', 'G', 5)
    add_edge('C', 'D', 5)
    add_edge('D', 'H', 5)
    add_edge('E', 'I', 5)
    add_edge('F', 'G', 5)

    c = shortest_path('A', 'G')
    print (c)
