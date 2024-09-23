from node import Node
from object import Object
def firstcompare(key,node):

    if key[0] < node.key[0] or (key[0]== node.key[0] and key[1] < node.key[1]):
        return 0
    elif key[0]> node.key[0] or (key[0] == node.key[0] and key[1] > node.key[1]):
        return 1
    else: return 2
def secondcompare(key,node):
    if key[0] < node.key[0] or (key[0]== node.key[0] and key[1] > node.key[1]):
        return 0
    elif key[0]> node.key[0] or (key[0] == node.key[0] and key[1] < node.key[1]):
        return 1
    else: return 2
def idcompare(key,node):
    if key < node.key : return 0
    elif key > node.key: return 1
    else: return 2

class AVLTree:
    def __init__(self,comp):
        self.root = None
        self.comparator = comp


    def height(self, node):
        if node is None:
            return 0
        return node.height

    def getbal(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T2 = y.right

        y.right = z
        z.left = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self,key,value,node):
        if node is None:
            return Node(key,value)

        if self.comparator(key,node) == 0 : node.left = self.insert(key,value,node.left)
        elif self.comparator(key,node) == 1: node.right= self.insert(key,value,node.right)

        node.height = 1 + max(self.height(node.left),self.height(node.right))
        balancefactor = self.getbal(node)

        if balancefactor > 1 and self.comparator(key,node.left) == 0 :
            return self.right_rotate(node)

        if balancefactor< -1 and self.comparator(key,node.right) == 1:
            return self.left_rotate(node)

        if balancefactor > 1 and self.comparator(key,node.left) == 1:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balancefactor < -1 and self.comparator(key,node.right) == 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def inordersucc(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, key,node):
        if node is None:
            return None

        if self.comparator(key,node) == 0 :
            node.left= self.delete(key,node.left)
        elif  self.comparator(key,node) == 1 :
            node.right=self.delete(key, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self.inordersucc(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right= self.delete(temp.key,node.right)

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.getbal(node)

        if balance > 1 and self.getbal(node.left) >= 0:
            return self.right_rotate(node)
        if balance < -1 and self.getbal(node.right) <= 0:
            return self.left_rotate(node)
        if balance > 1 and self.getbal(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and self.getbal(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def normalsearch(self,key,node):
        if node is None: return None
        if key < node.key:
            return self.normalsearch(key,node.left)
        elif key > node.key:
            return self.normalsearch(key,node.right)
        else: return node

    def searchmethod1(self,key,node,ans):

        if node is None: return ans
        if key <= node.key[0]:
            ans = node
            return self.searchmethod1(key,node.left,ans)
        return self.searchmethod1(key,node.right,ans)


    def searchmethod2(self,key,node):
        if node is None:return None
        while node.right is not None:
            return self.searchmethod2(key,node.right)
        else:
            if node.key[0] >= key:
                return node
            else: return None


    def inorder(self,node,ans):
        if node:
            self.inorder(node.left,ans)
            ans.append(node.key)
            self.inorder(node.right,ans)

