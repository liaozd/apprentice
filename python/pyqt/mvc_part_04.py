from PyQt5 import QtCore


class Node(object):

    def __init__(self, name, parent=None):
        self._name = name
        self._children =[]
        self._parent = parent

        if parent is not None:
            parent.addChild(self)

    def addChild(self, child):
        self._children.append(child)

    def name(self):
        return self._name

    def child(self, row):
        return self._children[row]

    def childCount(self):
        return len(self._children)

    def parent(self):
        return self._parent

    def row(self):
        if self._parent is not None:
            return self._parent._children.index(self)

    def log(self, tabLevel=-1):

        output = ""
        tabLevel += 1

        for i in range(tabLevel):
            output += " " * 5

        output += "|----" + self._name + "\n"

        for child in self._children:
            output += child.log(tabLevel)

        tabLevel -= 1

        return output

    def __repr__(self):
        return self.log()


class SceneGraphModel(QtCore.QAbstractItemModel):

    """INPUTS: Node, QObject"""
    def __init__(self, root, parent=None):
        super(SceneGraphModel, self).__init__(parent)
        self.rootNode = root

    def rowCount(self, parent=None, *args, **kwargs):
        pass

    def columnCount(self, parent=None, *args, **kwargs):
        pass

    def data(self, QModelIndex, role=None):
        pass

    def headerData(self, p_int, Qt_Orientation, role=None):
        pass

    def flags(self, QModelIndex):
        pass

    def parent(self, index):
        node = index.internalPointer()
        parentNode = node.parent()

        if parentNode == self.rootNode:
            return QtCore.QModelIndex()


    def index(self, p_int, p_int_1, parent=None, *args, **kwargs):
        pass

if __name__ == "__main__":

    rootNode = Node("Hips")
    childNode0 = Node("LeftPirateLeg", rootNode)
    childNode1 = Node("RightLeg", rootNode)
    childNode2 = Node("RightFoot", childNode1)

    print(rootNode)
