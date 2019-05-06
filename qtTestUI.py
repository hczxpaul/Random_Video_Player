__author__ = 'Chaozhang Huang'
from PySide2.QtCore import QObject, QRectF, Qt
from PySide2 import QtWidgets
from UI import mainwindow

class RVP(mainwindow.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(RVP, self).__init__()
        self.setupUi(self)
        self.selectRootButton.clicked.connect(self.get_root)

    def tr(self, text):
        return QObject.tr(self, text)

    def get_root(self):
        root_path= QtWidgets.QFileDialog.getExistingDirectory(self, self.tr("Load Directory"))
        self.rootPathLabel.setText(root_path)

    def populate_tree_widget(self):
        self.contentTree.clear()

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = RVP()
    qt_app.show()
    app.exec_()