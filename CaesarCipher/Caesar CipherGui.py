# Gui Edition Made by Edgar Ray Tuyor 
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QGridLayout)
import sys, string

class CaesarCipher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Caesar Cipher GUI Edition")
        self.setFixedWidth(320)
        self.setFixedHeight(120)

        layout = QGridLayout()

        #Text Input
        label_name = QLabel('<font size="4"> Text to be Encrypted </font>')
        self.lineEdit_inputText = QLineEdit()
        self.lineEdit_inputText.setPlaceholderText('Enter Your Text')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_inputText, 0, 1)

        #Shift
        label_shift = QLabel('<font size="4"> Shift number for Encryption </font>')
        self.lineEdit_inputshift = QLineEdit()
        self.lineEdit_inputshift.setPlaceholderText('Enter Your Shiftnumber')
        layout.addWidget(label_shift, 1, 0)
        layout.addWidget(self.lineEdit_inputshift, 1, 1)

        #EncryptButton
        encrypt_button = QPushButton('Encrypt')
        encrypt_button.clicked.connect(self.check_encrypt)
        layout.addWidget(encrypt_button, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        #DecryptButton
        decrypt_button = QPushButton('Decrypt')
        decrypt_button.clicked.connect(self.check_decrypt)
        layout.addWidget(decrypt_button, 3, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    #Check Encryption
    def check_encrypt(self):
        res = ""
        for i in range(len(self.lineEdit_inputText.text())):
            char = self.lineEdit_inputText.text()[i]
            if(char.isupper()):
                res += chr((ord(char) + int(self.lineEdit_inputshift.text()) -65) % 26 + 65)
            else:
                res += chr((ord(char) + int(self.lineEdit_inputshift.text())  - 97) % 26 + 97)
        msg.setText(res)
        msg.exec_()

    def check_decrypt(self):
        alphabet = string.ascii_lowercase
        decrypted_message = ""
        for i in self.lineEdit_inputText.text():
            if i in alphabet:
                position = alphabet.find(i)
                new_position = (position - int(self.lineEdit_inputshift.text()) % 26)
                new_character = alphabet[new_position]
                decrypted_message += new_character
            else:
                decrypted_message += i
        msg.setText(decrypted_message)
        msg.exec_()
            
#Main 
if __name__ == '__main__':
   app = QApplication(sys.argv)
   form = CaesarCipher()
   msg = QMessageBox()
   msg.setWindowTitle("Result!")
   msg.setStyleSheet("QMessageBox { messagebox-text-interaction-flags: 5; width:250px; font-size: 24px; min-width:500 px; }") # Make New Text Copyable and Size
   form.show()
   sys.exit(app.exec_())