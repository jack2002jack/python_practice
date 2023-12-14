import sys
from designed import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
import csv
from lib import vars
from itertools import islice

def showErrorMessage(object,message:str):
    QMessageBox.critical(object,"错误",message)

def showInformation(object,message:str):
    QMessageBox.information(object, "注意", message)
class mainWindowX(Ui_MainWindow,QMainWindow):
    def __init__(self):

        super(QMainWindow,self).__init__()
        self.headers_str=vars.headers_str
        self.headers=vars.headers
        self.card_list=vars.card_list
        self.setupUi(self)
        self.setWindowTitle("学生管理系统")
        self.model=QStandardItemModel(0,len(self.headers))
        self.model.setHorizontalHeaderLabels(self.headers)
        self.tableView.resizeColumnsToContents()
        self.tableView.setModel(self.model)
        self.tableView.setSortingEnabled(True)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(7,QHeaderView.Stretch)
        vars.WidgetsHandles.append({"mainWindow":self})

    def clearAll(self):
        self.model.removeRows(0, self.model.rowCount())


    def appendRow(self,data:tuple):
        self.model.appendRow([QStandardItem(i)for i in data])

    def flush(self):
        self.clearAll()
        for card in self.card_list:
            self.appendRow(card.values())
    def reflect(self):
        self.card_list.clear()
        for row in range(self.model.rowCount()):
            card={}
            for column in range(len(self.headers_str)):
                if self.model.item(row, column):
                    card[self.headers_str[column]]=self.model.item(row, column).text()
            self.card_list.append(card)


    @pyqtSlot()
    def on_actionImport_triggered(self):
        fname,_=QFileDialog.getOpenFileName(self, 'Load file', '.',
                     "database (*.csv);;All files (*.*)")
        if fname:
            self.card_list.clear()
            with open(fname,'r',encoding="utf-8") as fp:
                for data in islice(csv.reader(fp),1,None):
                  self.card_list.append(dict(zip(self.headers_str,data)))
        self.flush()
        self.reflect()


    @pyqtSlot()
    def on_actionExport_triggered(self):
        fname, _=QFileDialog.getSaveFileName(self, 'Export file', '.',
                        "database (*.csv);;All files (*.*)")
        if fname:
            self.reflect()
            with open(fname,'w',encoding="utf-8",newline="") as fp:
                cw=csv.writer(fp)
                cw.writerow(self.headers)
                for card in self.card_list:
                    cw.writerow(card.values())


    @pyqtSlot()
    def on_actionSave_triggered(self):
        fname, _ = QFileDialog.getSaveFileName(self, 'Load file', '.',
                                              "database (*.csv);;All files (*.*)")
        if fname:
            self.reflect()
            with open(fname,"w") as fp:
                fp.write()
    @pyqtSlot()
    def on_actionLoad_triggered(self):
        QFileDialog.getOpenFileName(self, 'Save file', '.',
                                    "project file (*.stu);;All files (*.*)")
    @pyqtSlot()
    def on_actionAppend_triggered(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Load file', '.',
                                               "database (*.csv);;All files (*.*)")
        if fname:
            with open(fname, 'r', encoding="utf-8") as fp:
                for data in islice(csv.reader(fp), 1, None):
                    self.card_list.append(dict(zip(self.headers_str,data)))
                self.flush()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = mainWindowX()
    myshow.show()
    sys.exit(app.exec_())
