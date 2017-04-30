from PyQt5 import QtCore, QtWidgets
import sys

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("cleanlooks")

    data = QtWidgets.QListWidgetItem()
    data = ['one', 'two', 'three']

    listWidget = QtWidgets.QListView()
    listWidget.show()

    model = QtCore.QStringListModel(data)
    listWidget.setModel(model)

    comboBox = QtWidgets.QComboBox()
    comboBox.show()
    comboBox.setModel(model)
    sys.exit(app.exec_())
