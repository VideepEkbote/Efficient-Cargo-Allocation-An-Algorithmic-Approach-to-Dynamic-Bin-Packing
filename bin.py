from avl import AVLTree,idcompare
class Bin:
    def __init__(self, bin_id, capacity):
        self.id= bin_id
        self.capacity = capacity
        self.tree = AVLTree(idcompare)

    def add_object(self, id,object):
        # Implement logic to add an object to this bin
        return self.tree.insert(id,object,self.tree.root)
        pass

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        return self.tree.delete(object_id,self.tree.root)
        pass
