class bNode(object):
    def __init__(self,data=None):
        self.left = None
        self.right = None
        self.data = data
A=bNode('2')
A.left=bNode('7')
A.right=bNode('5')
B=A.left
C=A.right
B.right=bNode('2')
D=B.right
C.left=bNode('6')
C.right=bNode('9')
E=C.left
F=C.right
D.left=bNode('5')
D.right=bNode('11')
E.left=bNode('4')
def DFS(A,data):
    visited = set()
    stack=[data]
    while stack:
        vertex = stack.pop()
        if not(vertex in visited):
            visited.add(vertex)
            stack.extend(A[vertex] - visited)
    return visited
def BFS(A,data):
    visited = set()
    queue = [data]
    while queue:
        vertex = queue.pop(0)
        if not(vertex in visited):
            visited.add(vertex)
            queue.extend(A[vertex] - visited)
    return visited
# DFS(A,'2')
print()
BFS(A,'2')