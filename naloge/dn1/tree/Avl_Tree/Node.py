
__author__ = "Luka Avbreht"

class Node():

    # TODO Probably havinf left and right node in init is kinda stupid, idk

    def __init__(self, value, left=None, right=None, parent=None):
        """
        Class that creates the structure for Avl to work on (only called once)
        """
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        if parent != None:
            self.depth = parent.depth+1
        else:
            self.depth = 0

    def __str__(self):
        if self.left is not None:
            if self.right is not None:
                return str(self.value) + "[" + str(self.depth) + "]" + " left:(" + str(self.left) + ")" + " right:(" + str(self.right) + ")"
            else:
                return str(self.value) + "[" + str(self.depth) + "]" + " left:(" + str(self.left) + ")" + " right:(" + " " + ")"
        else:
            if self.right is not None:
                return str(self.value) + "[" + str(self.depth) + "]" + " left:(" + " " + ")" + " right:(" + str(self.right) + ")"
            else:
                return str(self.value) + "[" + str(self.depth) + "]"









