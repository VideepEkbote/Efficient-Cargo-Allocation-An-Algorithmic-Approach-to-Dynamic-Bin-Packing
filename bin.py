from object import Object

class Bin:
    def __init__(self, bin_id, capacity):
        self.capacity= capacity
        self.bin_id = bin_id
        self.left = None
        self.right = None
        self.height = 1
        self.root = None
        pass

    def tall(self,node):
        if node is None:
            return 0
        return node.height

    def getbal(self,node):
        if node is None:
            return 0
        return self.tall(node.left) - self.tall(node.right)

    def right_rotate(self,y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.tall(y.left), self.tall(y.right))
        x.height = 1 + max(self.tall(x.left), self.tall(x.right))

        return x

    def left_rotate(self,x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.tall(x.left), self.tall(x.right))
        y.height = 1 + max(self.tall(y.left), self.tall(y.right))

        return y

    def add_object(self, object,node):
        if node is None:
            object.parentbin = self.bin_id
            return object

        if object.object_id < node.object_id:
            node.left = self.add_object(object,node.left)
        elif object.object_id > node.object_id:
            node.right = self.add_object(object,node.right)

        node.height = 1 + max(self.tall(node.left),self.tall(node.right))
        balancefactor =self.getbal(node)

        if balancefactor > 1 and object.object_id < node.left.object_id:
            return self.left_rotate(node.left)
        if balancefactor < -1 and object.object_id > node.left.object_id:
            return self.right_rotate(node.right)
        if balancefactor > 1 and object.object_id > node.left.object_id:
            node.left = self.left_rotate(node.left)
            return right_rotate(node)
        if balancefactor <  -1 and object.object_id < node.left.object_id:
            node.left = self.left_rotate(node.left)
            return left_rotate(node)



    def inordersucc(self,node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    def remove_object(self, object,node):
        if node is None: return node
        if object.object_id < node.object_id:
            node.left =self.remove_object(object,node.left)
        elif object.object_id > node.object_id:
            node.right = self.remove_object(object,node.right)
        else:
            if node.left is None: return node.right
            if node.right is None: return node.left

            temp = self.inordersucc(node.right)
            temp.object_id , object.object_id = object.object_id,temp.object_id
            node.right= self.remove_object(temp, node.right)
        node.height = 1 + max(self.tall(node.left), self.tall(node.right))
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

