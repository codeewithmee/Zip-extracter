from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from zipfile import ZipFile 
import sys

class Window(QtWidgets.QWidget):
	"""docstring for Window"""
	def __init__(self):
		QMainWindow.__init__(self) 

		self.fileName = ""
		self.path = ""
		self.setWindowTitle("Zip Extracter")
		self.setGeometry(100, 100, 400, 80) 
		self.ui()
		self.show()
		

	def ui(self):

		self.label_1 = QLabel("Select the zip file ")

		self.select_btn = QPushButton('Browse..',self)
		self.type_space = QLineEdit('')
		self.extract_btn = QPushButton('Extract',self)

		
		hbox = QHBoxLayout()
		hbox.addWidget(self.type_space)
		hbox.addWidget(self.select_btn)
		hbox.addWidget(self.extract_btn)
		
		vbox = QVBoxLayout()
		vbox.addStretch(1)
		vbox.addWidget(self.label_1)
		vbox.addLayout(hbox)


		self.setLayout(vbox)

		self.select_btn.clicked.connect(lambda x : self.Browse() )
		self.extract_btn.clicked.connect(lambda x : self.unzip())


	def find_path(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		self.path = QFileDialog.getExistingDirectory(None, "Select Directory",options=options)
		if self.path:
			print(self.path)

	def Browse(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
		self.type_space.setText(self.fileName)
		
	def unzip(self):
		try:
			self.find_path()
			with ZipFile(self.fileName, 'r') as files:
				files.extractall(self.path)
		except :
			pass
		


if __name__ == '__main__':
	App = QApplication(sys.argv)
	window = Window()
	sys.exit(App.exec())