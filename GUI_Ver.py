# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scarper.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import tkinter as tk
from tkinter import filedialog
import urllib.request
from bs4 import BeautifulSoup
import os
import shutil
import time

class Ui_Form(object):
    def getfilename(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        file_path = file_path.replace("/","\\")
        self.label_3.setText(file_path)
        
    def close(self):
        sys.exit()    
    
    #get correct url from list
    def find_http(self,lists):
        for data in lists:
            if(data[0:4] == "http"):
                return data
            
    #create a directory to store images        
    def directories(self,location,foldername):
        file_path=location.split("\\")
        filename=location.replace(file_path[len(file_path)-1],foldername)   
        #print(filename)
        
        if os.path.exists(filename):
            shutil.rmtree(filename, ignore_errors=True)
            
        for retry in range(100):
            try:
                os.mkdir(filename)        
                break
            except:
                exit()
        return filename
    
    #downloading images and adding to folder 
    def add_images(self,foldername,urls):
        index=1
        for url in urls:
            cal=0
            formats=".png"
            new_file_name=foldername+"\\filename-"+str(index)+"."+formats
            try:
                urllib.request.urlretrieve(url,new_file_name)
                cal=index/(len(urls))
                cal=cal*100
                self.progressBar.setProperty("value", int(cal))
                print(str(index)+"/"+str(len(urls))+" have been downloaded.")
            except:
                print(str(index)+"/"+str(len(urls))+" failed to be downloaded.")
            index=index+1    
            
        tk.messagebox.showinfo('Completed', 'The images have been successfully saved in the folder')
    
    def my_main(self):
        imagesurls=[]
        split_url=[]
        if(self.lineEdit.text() == ""):
            folder_name="Data"
        else:
            folder_name=self.lineEdit.text()
        if(self.label_3.text() == ""):
            return
        directory=self.label_3.text()
        new_dir=directory.replace("\\","\\\\")
        file=open(new_dir,'r')

        #parsing for data
        soup = BeautifulSoup(file, 'html.parser')
        all_images=soup.find_all("div", class_="rg_bx rg_di rg_el ivg-i")
        for images in all_images:
            temp=images.find_all("div", class_="rg_meta notranslate")
            for img in temp:
                imagesurls.append(img)
                
        #getting the urls        
        for url in imagesurls:
            split_temp=str(url)
            split_temp=split_temp.split("\"")
            split_url.append(self.find_http(split_temp))
        
        folder_name=self.directories(directory,folder_name)   
        self.add_images(folder_name,split_url) 
    

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(525, 380)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(150, 300, 281, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(200, 120, 141, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.getfilename)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 260, 141, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.my_main)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 47, 21))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 30, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(210, 190, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 160, 401, 21))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 340, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.close)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(162, 220, 221, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Select File from Directory"))
        self.pushButton_2.setText(_translate("Form", "Start Scarping"))
        self.label_2.setText(_translate("Form", "Directory:"))
        self.label.setText(_translate("Form", "Google Image Scarper"))
        self.label_4.setText(_translate("Form", "Output Folder Name"))
        self.pushButton_3.setText(_translate("Form", "Exit Program"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

