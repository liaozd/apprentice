from PyQt5 import QtGui, QtCore, QtWidgets
import sys


class PaletteTableModel(QtCore.QAbstractTableModel):
    def __init__(self, colors=[[]], headers=[], parent=None):
        super(PaletteTableModel, self).__init__()
        self.__colors = colors
        self.__headers = headers

    def headerData(self, section, orientation, role=None):
        if role == QtCore.Qt.DisplayRole:

            if orientation == QtCore.Qt.Horizontal:
                return self.__headers[section]
            else:
                return "Color %s" % section

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.__colors)

    def columnCount(self, parent=None, *args, **kwargs):
        return len(self.__colors[0])

    def flags(self, QModelIndex):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def data(self, index, role=None):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            return self.__colors[row][column].name()

        if role == QtCore.Qt.ToolTipRole:
            row = index.row()
            column = index.column()
            return "Hex code: " + self.__colors[row][column].name()

        if role == QtCore.Qt.DecorationRole:
            row = index.row()
            column = index.column()
            value = self.__colors[row][column]

            pixmap = QtGui.QPixmap(26, 26)
            pixmap.fill(value)
            icon = QtGui.QIcon(pixmap)
            return icon

        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            column = index.column()
            value = self.__colors[row][column]
            return value.name()


if __name__ == "__main__":
    tableData0 = [[QtGui.QColor("#FFFF00") for i in range(4)] for j in range(5)]
    headers = ["Pallete", "Colors", "Brushes", "MO"]

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("plastique")

    tableView = QtWidgets.QTableView()
    tableView.show()

    model = PaletteTableModel(tableData0, headers)
    tableView.setModel(model)

    sys.exit(app.exec_())
