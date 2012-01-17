# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Sat Dec 10 20:39:18 2011
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!


import xmlmsg
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
from imagepro import *

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_MainWindow(QtGui.QMainWindow):	
	def setupUi(self,path):
		self.setWindowTitle(QtGui.QApplication.translate("Gnome-BAXC", "Gnome-BAXC", None, QtGui.QApplication.UnicodeUTF8))
		self.resize(560, 512)
		self.centralwidget = QtGui.QWidget(self)
		self.gridLayout_9 = QtGui.QGridLayout(self.centralwidget)
		self.gridLayout_8 = QtGui.QGridLayout()
		self.label_6 = QtGui.QLabel(self.centralwidget)
		self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Select Images :", None, QtGui.QApplication.UnicodeUTF8))
		self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 1)
		self.splitter_3 = QtGui.QSplitter(self.centralwidget)
		self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
		self.label_7 = QtGui.QLabel(self.splitter_3)
		self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Duration (in min) :", None, QtGui.QApplication.UnicodeUTF8))

		self.doubleSpinBox = QtGui.QDoubleSpinBox(self.splitter_3)
		self.doubleSpinBox.setMinimum(1.00)
		self.doubleSpinBox.setValue(30.00)
		self.doubleSpinBox.setSingleStep (5.00)

		self.gridLayout_8.addWidget(self.splitter_3, 2, 0, 1, 1)


		self.splitter_2 = QtGui.QSplitter(self.centralwidget)
		self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
		self.pushButton_1 = QtGui.QPushButton(self.splitter_2)
		self.pushButton_1.setText(QtGui.QApplication.translate("MainWindow", "Mark All", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton_2 = QtGui.QPushButton(self.splitter_2)
		self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Unmark All", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton_13 = QtGui.QPushButton(self.splitter_2)
		self.pushButton_13.setText(QtGui.QApplication.translate("MainWindow", "Load images", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton_15 = QtGui.QPushButton(self.splitter_2)
		self.pushButton_15.setText(QtGui.QApplication.translate("MainWindow", "Create XML", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton_14 = QtGui.QPushButton(self.splitter_2)
		self.pushButton_14.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
		self.gridLayout_8.addWidget(self.splitter_2, 2, 1, 1, 1)
			

		self.scrollArea_6 = QtGui.QScrollArea(self.centralwidget)
		self.scrollArea_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)		
		self.scrollArea_6.setWidgetResizable(True)
		self.scrollAreaWidgetContents_7 = QtGui.QWidget()
		self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 521, 396))
		self.gridLayout_10 = QtGui.QGridLayout(self.scrollAreaWidgetContents_7)

		self.setcheckbox(path)

		self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_7)
		self.gridLayout_8.addWidget(self.scrollArea_6, 1, 0, 1, 2)
		self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)
		self.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(self)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 21))
		self.menuFile = QtGui.QMenu(self.menubar)
		self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
		self.menuHelp = QtGui.QMenu(self.menubar)
		self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
		self.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(self)
		self.setStatusBar(self.statusbar)
		self.actionQuit = QtGui.QAction(self)
		self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
		self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
		self.actionQuit.setMenuRole(QtGui.QAction.QuitRole)
		self.actionQuit.setSoftKeyRole(QtGui.QAction.NoSoftKey)
		self.actionQuit.setPriority(QtGui.QAction.LowPriority)
		self.actionAbout = QtGui.QAction(self)
		self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
		self.menuFile.addAction(self.actionQuit)
		self.menuHelp.addAction(self.actionAbout)
		self.menubar.addAction(self.menuFile.menuAction())
		self.menubar.addAction(self.menuHelp.menuAction())
		QtCore.QObject.connect(self.pushButton_14, QtCore.SIGNAL(_fromUtf8("clicked()")), self.close)
#remove self.pushButton_**  by action
		QtCore.QObject.connect(self.pushButton_15, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getselected)
		QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.close)
		QtCore.QObject.connect(self.actionAbout,QtCore.SIGNAL("activated()"),self.About)
		QtCore.QObject.connect(self.pushButton_13, QtCore.SIGNAL(_fromUtf8("clicked()")), self.dirsel)
		QtCore.QObject.connect(self.pushButton_1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.markall)
		QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.unmarkall)
		
		QtCore.QMetaObject.connectSlotsByName(self)


	def __init__(self,path):
		super(Ui_MainWindow, self).__init__()
		self.setupUi(path)
		self.show()	


	def setcheckbox(self,path):
		self.image=list()
		c=0
		self.path=path+'/'
		dirs = os.listdir(self.path)
		dirs.sort()
		for i in dirs:
			if isimage(i):
				self.image.append(QtGui.QCheckBox(self.scrollAreaWidgetContents_7))
				self.image[c].setText(_fromUtf8(i))
				icon = QtGui.QIcon()
				icon.addPixmap(QtGui.QPixmap(_fromUtf8(self.path+i)), QtGui.QIcon.Normal, QtGui.QIcon.On)
				self.image[c].setIcon(icon)
				self.image[c].setIconSize(QtCore.QSize(150, 150))
				self.gridLayout_10.addWidget(self.image[c], c+1, 0, 1, 1)
				c=c+1


	def getselected(self):
		self.time=self.doubleSpinBox.value()
		outfile=self.path+"background.xml"
		x = xmlmsg.xml(self.path,(self.time)*60.0-5)
		image.start=""
		try:
			f=open(outfile,'w')
			f.write(x.start)
			for j in self.image:
				if j.checkState():
					i=j.text()
					if image.count==0:
						image.count=image.count+1
						f.write(x.s1+i+x.s2+i+x.s3)
						image.start=i
					else:
						s0='\n<to>'+self.path+i+'</to> \n</transition>'
						f.write(s0+x.s1+i+x.s2+i+x.s3)
						image.count=image.count+1
			f.write("\n<to>"+self.path+image.start+x.end)
			f.close()
			close(outfile)
		except IOError as e:
			QtGui.QMessageBox.critical(self,"IOError",e.__str__())
		if image.count!=0:
			QtGui.QMessageBox.about(self,"XML File Created",xmlmsg.finalmsg(outfile,image.count))
			self.close()
				
	def markall(self):
		for i in self.image:
			i.setCheckState(True)

	def unmarkall(self):
		for i in self.image:
			i.setCheckState(False)

	def About(self):
		QtGui.QMessageBox.about(self,"About",xmlmsg.aboutmsg)

	def dirsel(self):
		dirs = QFileDialog.getExistingDirectory(self, "Open Directory","/home",QFileDialog.ShowDirsOnly|QFileDialog.DontResolveSymlinks)
		if dirs !="":
			dirs = dirs+"/"
			print (dirs)
			for i in range(self.gridLayout_10.count()):
				self.gridLayout_10.itemAt(i).widget().close()
			self.image[:] = []
			self.setcheckbox(dirs)


def main():
	import sys
	import os
	path = os.getenv('HOME')+"/Pictures"
	app = QtGui.QApplication(sys.argv)
	ui = Ui_MainWindow(path)
	sys.exit(app.exec_())

