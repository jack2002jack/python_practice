import sys
from designed import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
import csv
from itertools import islice
class mainWindowX(Ui_MainWindow,QMainWindow):
    headers=["学号","姓名","班级","性别","年龄","电话","QQ","地址"]
    def __init__(self):

        super(QMainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("学生管理系统")
        self.model=QStandardItemModel(0,len(self.headers))
        self.model.setHorizontalHeaderLabels(self.headers)
        self.tableView.resizeColumnsToContents()
        self.tableView.setModel(self.model)
        self.tableView.setSortingEnabled(True)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(7,QHeaderView.Stretch)

    def appendColumn(self,data:tuple):
        pass
    @pyqtSlot()
    def on_actionImport_triggered(self):
        fname,_=QFileDialog.getOpenFileName(self, 'Load file', '.',
                                    "database (*.csv);;All files (*.*)")
        if fname:
            self.model.removeRows(0,self.model.rowCount())
            with open(fname,'r',encoding="utf-8") as fp:
                for data in islice(csv.reader(fp),1,None):
                    self.model.appendRow([QStandardItem(i)for i in data])


    @pyqtSlot()
    def on_actionExport_triggered(self):
        QFileDialog.getOpenFileName(self, 'Export file', '.',
                                    "database (*.csv);;All files (*.*)")

    @pyqtSlot()
    def on_actionSave_triggered(self):
        QFileDialog.getOpenFileName(self, 'Save file', '.',
                                    "project file (*.stu);;All files (*.*)")

    @pyqtSlot()
    def on_actionLoad_triggered(self):
        QFileDialog.getOpenFileName(self, 'Save file', '.',
                                    "project file (*.stu);;All files (*.*)")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = mainWindowX()
    myshow.show()
    sys.exit(app.exec_())
