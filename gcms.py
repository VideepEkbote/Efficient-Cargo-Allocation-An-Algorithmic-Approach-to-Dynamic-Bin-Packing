from bin import Bin
from avl import AVLTree,comp_1
from object import Object, Color
from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.bincapacitytree = AVLTree(comp_1)
        pass 

    def add_bin(self, bin_id, capacity):
        bin_to_be_added = Bin(bin_id,capacity)
        self.bincapacitytree.insert(bin_to_be_added,self.bincapacitytree.root)
        pass

    def add_object(self, object_id, size, color):
        if color == 1:
            # search
            y = self.bincapacitytree.compactleastsearch(size,self.bincapacitytree.root,None)
            if y is not None:
                objectcreate = Object(object_id,size,color)
                y.add_object(objectcreate,y.root)
                self.bincapacitytree.remove_bin(y)
                y.capacity = capacity - size
                self.bincapacitytree.insert(y,self.bincapacitytree.root)
            else: raise NoBinFoundException



        raise NoBinFoundException

    def delete_object(self, object_id):
        if color == 1:
            # search
            y = self.bincapacitytree.compactleastsearch(size, self.bincapacitytree.root, None)
            if y is not None:
                objectcreate = Object(object_id, size, color)
                y.remove_object(objectcreate, y.root)
                self.bincapacitytree.remove_bin(y)
                y.capacity = capacity + size
                self.bincapacitytree.insert(y, self.bincapacitytree.root)
            else:
                raise NoBinFoundException
        pass

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        pass

    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        pass
    
    