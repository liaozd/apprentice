from PyQt5.QtCore import QObject, pyqtSignal


class TaxRate(QObject):

    rateChanged = pyqtSignal(float)

    def __init__(self):
        super(TaxRate, self).__init__()
        self.__rate = 17.5

    def rate(self):
        return self.__rate

    def setRate(self, rate):
        if rate != self.__rate:
            self.__rate = rate
            self.rateChanged.emit(self.__rate)


def rateChanged(value):
    print("TaxRate changed to %.2f" % value)

if __name__ == '__main__':
    vat = TaxRate()
    vat.rateChanged.connect(rateChanged)
    vat.setRate(10)
