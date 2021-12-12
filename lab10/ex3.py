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

def NLR(A):
    if A:
        print(A.data + "->", end = '')
        NLR(A.left)
        NLR(A.right)
def LNR(A):
    NLR(A.left)
    print(A.data+ "->", end = '')
    NLR(A.right)
def LRN(A):
    NLR(A.left)
    NLR(A.right)
    print(A.data+ "->", end = '')
print("Node-Left-Right")
NLR(A)
print()
print("Left-Node-Right")
LNR(A)
print()
print("Left-Right-Node")
LRN(A)