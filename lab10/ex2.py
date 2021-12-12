
# ex2
class bNode(object):
    def __init__(self,data = None):
        self.left = None
        self.right = None
        self.data = data
#cau a
A = bNode('2')
A.left = bNode('7')
A.right = bNode('5')
B = A.left
C = A.right
B.left = bNode('2')
B.right = bNode('6')
D = B.right
C.right = bNode('9')
E = C.right
D.left = bNode('5')
D.right = bNode('11')
E.left = bNode('4')
F = D.left
G = D.right
H = E.left

#cau b
A = bNode('50')
A.left = bNode('17')
A.right = bNode('76')
B = A.left
C = A.right
B.left = bNode('9')
B.right = bNode('23')
D = B.left
D.right = bNode('14')
G = D.right
E = B.right
E.left = bNode('19')
C.left = bNode('54')
F = C.left
F.right = bNode('72')
I = F.right
I.left = bNode('67')
K = I.left
G.left = bNode('12')
J = G.left
M = E.left
