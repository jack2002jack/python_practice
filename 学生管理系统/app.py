import sys
import typing
import threading

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import csv
from lib import vars,manipulate
from itertools import islice
from ui.UIMain import Ui_MainWindow
from ui.UIaddPanel import Ui_AddPanel
from ui.UIdleletePanel import Ui_deletePanel
from ui.UIupdatePanel import Ui_updatePanel
from ui.UIquery import Ui_queryPanel
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


    def appendRow(self,data:typing.Iterable):
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
    @pyqtSlot()
    def on_actionAdd_triggered(self):
        self.addPanel=addPanel()
        self.addPanel.show()

    @pyqtSlot()
    def on_actionDelete_triggered(self):
        self.deletePanel = deletePanel()
        self.deletePanel.show()

    @pyqtSlot()
    def on_actionUpdate_triggered(self):
        self.updatePanel = updatePanel()
        self.updatePanel.show()


    @pyqtSlot()
    def on_actionQuery_triggered(self):
        self.queryPanel = queryPanel()
        self.queryPanel.show()

class addPanel(Ui_AddPanel,QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("添加学生")


    @pyqtSlot()
    def on_pushButton_clicked(self):
        values=[]
        for i in range(1,8):
            value=eval(f"self.lineEdit{i}.text()")
            if value:
                values.append(value)
            else:
                showErrorMessage(self,"添加失败,无效的信息")
                return
        vars.card_list.append(dict(zip(vars.headers,values)))
        vars.WidgetsHandles[0]['mainWindow'].flush()

class deletePanel(Ui_deletePanel,QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("删除学生")

    @pyqtSlot()
    def on_pushButton_clicked(self):
        value=self.lineEdit.text()
        if value:
            if (index := manipulate.findBysno(vars.card_list, value))!=None:
                if QMessageBox.information(self, "确认删除",
                                           "确定要删除%s，%s，%s，%s，%s，%s，%s 这条数据吗"%
                                                   tuple(vars.card_list[
                                                       index].values()),buttons=QMessageBox.Yes|QMessageBox.No)==QMessageBox.Yes:
                    manipulate.man_delete(vars.card_list, index)
                    showInformation(self, "删除成功")
                    vars.WidgetsHandles[0]['mainWindow'].flush()
            else:
                showInformation(self, "未找到该名学生")
        else:
            showErrorMessage(self,"不能为空")


class updatePanel(Ui_updatePanel,QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("更新信息")


    @pyqtSlot()
    def on_pushButton_clicked(self):
        if sno:=self.lineEdit.text():
            index=manipulate.findBysno(vars.card_list,sno)
            if index!=None and (value:=self.lineEdit_2.text()) and (head:=self.comboBox.currentText()):
                head_str=vars.headers_str[vars.headers.index(head)]
                old_value=vars.card_list[index][head_str]
                name=vars.card_list[index]["name_str"]
                if QMessageBox.information(self, "确认修改","确定要将 %s的%s %s 修改为 %s吗？ " %(name,head,old_value,value),
                                           buttons=QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                    vars.card_list[index][head_str]=value
                    vars.WidgetsHandles[0]['mainWindow'].flush()



class queryPanel(Ui_queryPanel,QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("查询信息")



    @pyqtSlot()
    def on_pushButton_clicked(self):
        if value:=self.lineEdit.text():
            head_str=self.comboBox.currentText()
            column=vars.headers.index(head_str)
            for index in manipulate.man_find(vars.card_list,head_str,value):
                model=vars.WidgetsHandles[0]["mainWindow"].model
                model.item(index,column).setBackground(QBrush(QColor(Qt.red)))
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        vars.WidgetsHandles[0]["mainWindow"].flush()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = mainWindowX()
    myshow.show()
    sys.exit(app.exec_())
