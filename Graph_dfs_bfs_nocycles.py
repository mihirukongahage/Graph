''' Directed Graph '''
''' No Weights '''
''' Oper : BFS, DFS, No of cycles '''

graph = {}

def add_node(src, dest):
    if(src not in graph):
        graph[src] = []
    if(dest not in graph):
        graph[dest] = []
     
    graph[src].append(dest)


def bfs(start):
    visited = []
    q = [start]
    while(q):
        p = q.pop(0)
        if(p not in visited):
            visited.append(p)
            for v in graph[p]:
                q.append(v)
    
    return visited

def dfs(start):
    visited = []
    s = [start]
    while(s):
        p = s.pop(-1)
        if(p not in visited):
            visited.append(p)
            for v in graph[p]:
                s.append(v)
    
    return visited

def no_of_cyc(start):
    count  = 0
    visited = []
    s = [start]
    while(s):
        p = s.pop(-1)
        if(p not in visited):
            visited.append(p)
            for v in graph[p]:
                s.append(v)
        else:
            count = count + 1
    return count

if __name__ == "__main__":
    '''add_node(0,1)
    add_node(1,2)
    add_node(0,2)
    add_node(2,0)
    add_node(2,3)
    add_node(3,3)'''

    add_node(2,2)

    
    print(no_of_cyc(2))
