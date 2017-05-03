from PyQt5 import QtGui, QtCore, QtWidgets
import sys


class PalleteListModel(QtCore.QAbstractListModel):
    def __init__(self, colors=[], parent=None):
        super(PalleteListModel, self).__init__(parent)
        self.__color = colors

    def headerData(self, section, orientation, role=None):
        if role == QtCore.Qt.DisplayRole:

            if orientation == QtCore.Qt.Horizontal:
                return "Pallette"
            else:
                return "Color %s" % section

    def rowCount(self, parent):
        return len(self.__color)

    def data(self, index, role):

        if role == QtCore.Qt.EditRole:
            return self.__color[index.row()].name()

        if role == QtCore.Qt.ToolTipRole:
            return "Hex code: " + self.__color[index.row()].name()

        if role == QtCore.Qt.DecorationRole:
            row = index.row()
            value = self.__color[row]

            pixmap = QtGui.QPixmap(26, 26)
            pixmap.fill(value)
            icon = QtGui.QIcon(pixmap)
            return icon

        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            value = self.__color[row]
            return value.name()

    def flags(self, QModelIndex):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            color = QtGui.QColor(value)
            if color.isValid():
                self.__color[row] = color
                self.dataChanged.emit(index, index)
                return True
        return False

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('plastique')

    listView = QtWidgets.QListView()

    treeView = QtWidgets.QTreeView()

    comboBox = QtWidgets.QComboBox()

    tableView = QtWidgets.QTableView()

    red = QtGui.QColor(255, 0, 0)
    green = QtGui.QColor(0, 255, 0)
    blue = QtGui.QColor(0, 0, 255)

    model = PalleteListModel(colors=[red, green, blue])

    listView.setModel(model)
    treeView.setModel(model)
    comboBox.setModel(model)
    tableView.setModel(model)

    listView.show()
    treeView.show()
    comboBox.show()
    tableView.show()

    sys.exit(app.exec_())
