from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QCloseEvent, QFont
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget 

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('Main_window.ui', self)
        self.show()

        self.setWindowTitle("IDOS-Default texte editor")
        
        #Pour changer la taille des caracteres selon l'option choisi
        self.action12.triggered.connect(lambda: self.change_size(12))
        self.action18.triggered.connect(lambda: self.change_size(18))
        self.action24.triggered.connect(lambda: self.change_size(24))

        #Pour initialiser la taille et la police  
        self.police = "Calibri"
        self.taille_caracter = 10
        self.apply_font()
        
        # Pour changer la police suivant les options choisi
        self.actionArial.triggered.connect(lambda: self.change_font("Arial"))
        self.actionTimes_New_Roman.triggered.connect(lambda: self.change_font("Times New Roman"))
        self.actionArial_Rounded_MT_Bold.triggered.connect(lambda: self.change_font("Arial Rounded MT Bold"))

        #Pour ouvrir et sauvegarder les fichiers
        self.actionopen.triggered.connect(self.open_file)
        self.actionsave.triggered.connect(self.save_file)
        self.actionClose.triggered.connect(self.closeEvent)

    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;Python Files (*.py)",options=options)
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())

    def save_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)",options=options)
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())

    def closeEvent(self,event):
        dialog = QMessageBox()
        dialog.setText("Do you want to save your work ?")
        dialog.addButton(QPushButton("Yes"),QMessageBox.YesRole)
        dialog.addButton(QPushButton("No"),QMessageBox.NoRole)
        dialog.addButton(QPushButton("Cancel"),QMessageBox.RejectRole)
        usr_reposne = dialog.exec_()
        if usr_reposne == 0:
            self.save_file()
            event.accept()
        elif usr_reposne == 2:
            event.ignore()





    def change_font(self, nom_fonte):
        self.police =nom_fonte
        self.apply_font()


    def change_size(self , size):
        self.taille_caracter = size
        self.apply_font()

    #cette fonction me permet de combiner les changements de taille et de police
    def apply_font(self):
        font = QFont(self.police, self.taille_caracter)
        self.plainTextEdit.setFont(font)


    
def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == '__main__' :
    main()