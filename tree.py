class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insertLeft (self,newNode):
        if self.left == None:
            self.left = Node(newNode)

        else :
            t = Node(newNode)
            t.left = self.left
            self.left = t

    def insertRight (self,newNode):
        if self.right == None:
            self.right = Node (newNode)
        
        else :
            t = Node (newNode)
            t.right = self.right
            self.right = t
    
    def setRoot (self,rootNode) :
        self.data = rootNode

    def getRoot (self) :
        return self.data

    def getLeft (self) :
        return self.left
    
    def getRight (self) :
        return self.right

class BinaryTree :
    def __init__(self):
        self.inorder 
        self.postorder 
        self.preorder
        
    def inorder(self,root):
        if root != None :
            self.inorder(root.getLeft())
            print(str(root.getRoot()) + "->", end='')
            self.inorder(root.getRight())


    def postorder(self,root):
        if root != None :
            self.postorder(root.getLeft())
            self.postorder(root.getRight())
            print(str(root.getRoot()) + "->", end='')


    def preorder(self,root):
        if root != None :
            print(str(root.getRoot()) + "->", end='')
            self.preorder(root.getLeft())
            self.preorder(root.getRight())

p = BinaryTree()
tree = Node('A')
tree.insertLeft('B')
tree.getLeft().insertLeft('D')
tree.getLeft().insertRight('E')
tree.insertRight('C')
tree.getRight().insertLeft('F')
tree.getRight().getLeft().insertLeft('I')
tree.getRight().getLeft().getLeft().insertLeft('K')
tree.getRight().getLeft().insertRight('J')

print('\t == Soal No.1 ==')
print(" - Inorder traversal ")
p.inorder(tree)

print("\n - Preorder traversal ")
p.preorder(tree)

print("\n - Postorder traversal ")
p.postorder(tree)

tree2 = Node('G')
tree2.insertLeft('K')
tree2.getLeft().insertRight('P')
tree2.getLeft().insertRight('B')
tree2.getLeft().getRight().insertRight('D')
tree2.getLeft().getRight().getRight().insertRight('S')
tree2.getLeft().getRight().getRight().insertLeft("C")
tree2.insertRight('M')
tree2.getRight().insertRight('A')
tree2.getRight().getRight().insertLeft('L')
tree2.getRight().getRight().insertRight('G')
tree2.getRight().getLeft().insertLeft('G')


print('\n\n\n\t == Soal No.2 ==')
print(" - Inorder traversal ")
p.inorder(tree2)

print("\n - Preorder traversal ")
p.preorder(tree2)

print("\n - Postorder traversal ")
p.postorder(tree2)



tree3 = Node (18)
tree3.insertLeft(16)
tree3.getLeft().insertRight(7)
tree3.getLeft().getRight().insertLeft(9)
tree3.getLeft().getRight().insertRight(12)
tree3.insertRight(5)
tree3.getRight().insertLeft(10)
tree3.getRight().insertRight(14)
tree3.getRight().getRight().insertLeft(23)

print('\n\n\n\t == Soal No.3 ==')
print(" - Inorder traversal ")
p.inorder(tree3)

print("\n - Preorder traversal ")
p.preorder(tree3)

print("\n - Postorder traversal ")
p.postorder(tree3)



