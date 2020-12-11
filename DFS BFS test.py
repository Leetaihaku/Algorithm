from anytree import Node, RenderTree
from collections import deque

one = Node('1')
two = Node('2', parent=one)
three = Node('3', parent=one)
four = Node('4', parent=two)
five = Node('5', parent=two)
six = Node('6', parent=three)
seven = Node('7', parent=three)

for pre, fill, node in RenderTree(one):
    print("%s%s" % (pre, node.name))

graph = {
    1: set([2, 3]),
    2: set([1, 4, 5]),
    3: set([1, 6, 7]),
    4: set([2]),
    5: set([2]),
    6: set([3]),
    7: set([3])
}
root = 1

def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

def DFS(graph, root):
    visited = []
    stack = deque([root])

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

if __name__ == '__main__':
    print('BFS')
    print(BFS(graph, root), '\n')
    print('DFS')
    print(DFS(graph, root))