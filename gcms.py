from bin import Bin
from node import Node
from avl import AVLTree,firstcompare,secondcompare,idcompare
from object import Object, Color
from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.binsTree1 = AVLTree(firstcompare)
        self.binsTree2 = AVLTree(secondcompare)
        self.binIDTree = AVLTree(idcompare)
        self.objectIDTree = AVLTree(idcompare)
        pass

    def add_bin(self, bin_id, capacity):
        binadded = Bin(bin_id,capacity)
        self.binsTree1.root = self.binsTree1.insert([capacity,bin_id],binadded,self.binsTree1.root)
        self.binsTree2.root = self.binsTree2.insert([capacity,bin_id],binadded,self.binsTree2.root)
        self.binIDTree.root = self.binIDTree.insert(bin_id, binadded, self.binIDTree.root)

    def add_object(self, object_id, size, color):
        if color == Color(1):
            y = self.binsTree1.searchmethod1(size,self.binsTree1.root,None)
            if y is not None:
                g = y.key
                h = Node(y.key,y.value)
                self.binsTree1.root = self.binsTree1.delete(g,self.binsTree1.root)
                self.binsTree2.root = self.binsTree2.delete(g,self.binsTree2.root)
                h.value.capacity =h.value.capacity - size
                object = Object(object_id,size,color,h.value)
                self.objectIDTree.root = self.objectIDTree.insert(object_id,object,self.objectIDTree.root)
                h.value.tree.root = h.value.add_object(object_id,object)
                h.key[0] = h.value.capacity
                h.key[1] = h.value.id
                self.binsTree1.root = self.binsTree1.insert(h.key,h.value, self.binsTree1.root)
                self.binsTree2.root = self.binsTree2.insert(h.key,h.value, self.binsTree2.root)
            else:
                raise NoBinFoundException
        if color == Color(2):
            y = self.binsTree1.searchmethod1(size,self.binsTree2.root,None)
            if y is not None:
                g = y.key
                h = Node(y.key,y.value)
                self.binsTree1.root = self.binsTree1.delete(g,self.binsTree1.root)
                self.binsTree2.root = self.binsTree2.delete(g,self.binsTree2.root)
                h.value.capacity =h.value.capacity - size
                object = Object(object_id,size,color,h.value)
                self.objectIDTree.root = self.objectIDTree.insert(object_id,object,self.objectIDTree.root)
                h.value.tree.root = h.value.add_object(object_id,object)
                h.key[0] = h.value.capacity
                h.key[1] = h.value.id
                self.binsTree1.root = self.binsTree1.insert(h.key,h.value, self.binsTree1.root)
                self.binsTree2.root = self.binsTree2.insert(h.key,h.value, self.binsTree2.root)
            else:
                raise NoBinFoundException

        if color == Color(3):
            y = self.binsTree1.searchmethod2(size,self.binsTree2.root)
            if y is not None:
                g = y.key
                h = Node(y.key,y.value)
                self.binsTree1.root = self.binsTree1.delete(g,self.binsTree1.root)
                self.binsTree2.root = self.binsTree2.delete(g,self.binsTree2.root)
                h.value.capacity =h.value.capacity - size
                object = Object(object_id,size,color,h.value)
                self.objectIDTree.root = self.objectIDTree.insert(object_id,object,self.objectIDTree.root)
                h.value.tree.root = h.value.add_object(object_id,object)
                h.key[0] = h.value.capacity
                h.key[1] = h.value.id
                self.binsTree1.root = self.binsTree1.insert(h.key,h.value, self.binsTree1.root)
                self.binsTree2.root = self.binsTree2.insert(h.key,h.value, self.binsTree2.root)
            else:
                raise NoBinFoundException
        if color == Color(4):
            y = self.binsTree1.searchmethod2(size,self.binsTree1.root)
            if y is not None:
                g = y.key
                h = Node(y.key,y.value)
                self.binsTree1.root = self.binsTree1.delete(g,self.binsTree1.root)
                self.binsTree2.root = self.binsTree2.delete(g,self.binsTree2.root)
                h.value.capacity =h.value.capacity - size
                object = Object(object_id,size,color,h.value)
                self.objectIDTree.root = self.objectIDTree.insert(object_id,object,self.objectIDTree.root)
                h.value.tree.root = h.value.add_object(object_id,object)
                h.key[0] = h.value.capacity
                h.key[1] = h.value.id
                self.binsTree1.root = self.binsTree1.insert(h.key,h.value, self.binsTree1.root)
                self.binsTree2.root = self.binsTree2.insert(h.key,h.value, self.binsTree2.root)
            else:
                raise NoBinFoundException




    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        y = self.objectIDTree.normalsearch(object_id,self.objectIDTree.root)
        if y is None: return None
        # y is a Node whose key is object_id and value is an instance of Object
        bincorrespondence = y.value.belongingbin
        size = y.value.size
        bincorrespondence.tree.root = bincorrespondence.remove_object(object_id)
        self.objectIDTree.root = self.objectIDTree.delete(object_id,self.objectIDTree.root)
        h = Node([bincorrespondence.capacity,bincorrespondence.id], bincorrespondence)
        self.binsTree1.root = self.binsTree1.delete([bincorrespondence.capacity,bincorrespondence.id], self.binsTree1.root)
        self.binsTree2.root = self.binsTree2.delete([bincorrespondence.capacity,bincorrespondence.id], self.binsTree2.root)
        h.value.capacity = h.value.capacity+ size
        h.key[0] = h.value.capacity
        h.key[1] = h.value.id
        self.binsTree1.root = self.binsTree1.insert(h.key, h.value, self.binsTree1.root)
        self.binsTree2.root = self.binsTree2.insert(h.key, h.value, self.binsTree2.root)
        pass

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])

        y = self.binIDTree.normalsearch(bin_id,self.binIDTree.root)
        # y is a Node whose key is Bin_id and value is an instance of Bin
        if y is not None:
            ans = []
            y.value.tree.inorder(y.value.tree.root, ans)
            return (y.value.capacity,ans)
        else: return None


    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        y = self.objectIDTree.normalsearch(object_id, self.objectIDTree.root)
        # y is a Node whose key is object_id and value is an instance of Object
        if y is not None:
            bincorrespondence = y.value.belongingbin.id
            return bincorrespondence
        else:return None


