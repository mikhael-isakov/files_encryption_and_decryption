design_origin = '.py'
if design_origin == '.py':
    from design import Ui_MainWindow
import os, sys, hashlib
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic
from threading import Thread
import functions as funcs
from classes import date_time



class MainWindow(QMainWindow):
    #
    def __init__(self):
        #
        super(MainWindow, self).__init__()
        #
        if design_origin == '.py':
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
        elif design_origin == '.ui':
            self.ui = uic.loadUi(os.path.join(os.getcwd(), 'design.ui'), self)
        #
        funcs.set_window_sizes(self)
        funcs.set_icons_and_title(self)
        funcs.set_fonts(self)
        funcs.set_buttons_hover_properties(self)
        #
        # пусть кнопка "зашифровать" (encrypt) вначале неактивна
        self.ui.pushButton_3.setEnabled(False)
        #
        # установка начальных значений некоторых переменных
        self.mode = self.ui.comboBox_1.currentText()
        self.path_to_file = ''
        self.is_pass = False
        self.pass_hash = hashlib.sha256(self.ui.lineEdit_1.text().encode('utf-8')).hexdigest()
        self.path_to_keyfile = ''
        self.keyfile_hash = ''
        #
        # установка функциональности комбобокса выбора режима работы
        self.ui.comboBox_1.currentTextChanged.connect(self.mode_changed)
        #
        # установка функциональности поля ввода пароля
        self.ui.lineEdit_1.textChanged.connect(self.pass_changed)
        #
        # установка функциональности кнопок
        self.ui.pushButton_1.clicked.connect(self.select_file_for_work)
        self.ui.pushButton_2.clicked.connect(self.select_keyfile)
        self.ui.pushButton_3.clicked.connect(self.make_crypt)
    #
    def mode_changed(self, value):
        # функция осуществляет действия при изменении в комбобоксе с типом работы
        self.mode = value
        #
        if self.mode == 'encrypt':
            self.ui.pushButton_3.setText('Encrypt')
        elif self.mode == 'decrypt':
            self.ui.pushButton_3.setText('Decrypt')
        #
        self.ui.label_7.setText('{} - Mode selected: {}'.format(date_time.now().nice_view, self.mode))
        #
        return 0
    #
    def pass_changed(self):
        # функция осуществляет действия при изменении в поле ввода пароля
        try:
            self.pass_hash = hashlib.sha256(self.ui.lineEdit_1.text().encode('utf-8')).hexdigest()
            self.ui.label_7.setText('{} - Password changed'.format(date_time.now().nice_view))
            if len(self.ui.lineEdit_1.text()) > 0:
                self.is_pass = True 
                self.ui.lineEdit_1.resize(270, 30)
            else:
                self.is_pass = False
                self.ui.lineEdit_1.resize(300, 30)
        except:
            self.is_pass = False
            self.ui.lineEdit_1.resize(300, 30)
        #
        self.encrypt_or_decrypt_allowed()
        #
        return 0
    #
    def select_file_for_work(self):
        try:
            self.path_to_file = QFileDialog.getOpenFileName(self, 'Select File, please')[0]
            filename = os.path.split(self.path_to_file)[1]
            if len(filename) > 0:
                self.ui.label_7.setText('{} - File selected: {}'.format(date_time.now().nice_view, filename))
                self.ui.pushButton_1.resize(290, 30)
            else:
                self.ui.label_7.setText('{} - File not selected.'.format(date_time.now().nice_view, ))
                self.ui.pushButton_1.resize(320, 30)
        except:
            self.ui.pushButton_1.resize(320, 30)
            self.ui.label_7.setText('{} - File selected error'.format(date_time.now().nice_view))
        #
        self.encrypt_or_decrypt_allowed()
        #
        return 0
    #
    def select_keyfile(self):
        try:
            self.path_to_keyfile = QFileDialog.getOpenFileName(self, 'Select Keyfile, please')[0]
            filename = os.path.split(self.path_to_keyfile)[1]
            #
            filesize = os.path.getsize(self.path_to_keyfile)
            if filesize > 10*1024**2:
                self.ui.label_7.setText('{} - Select file less than 10 MB'.format(date_time.now().nice_view))
            else:
                sha256_hash = hashlib.new('sha256')
                with open(self.path_to_keyfile, 'rb') as file:
                    while True:
                        data = file.read(1024)
                        if not data:
                            break
                        sha256_hash.update(data)
            self.keyfile_hash = sha256_hash.hexdigest()
            #
            if len(filename) > 0:
                self.ui.label_7.setText('{} - Keyfile selected: {}'.format(date_time.now().nice_view, filename))
                self.ui.pushButton_2.resize(270, 30)
            else:
                self.ui.label_7.setText('{} - Keyfile not selected.'.format(date_time.now().nice_view, ))
                self.ui.pushButton_2.resize(300, 30)
        except:
            self.ui.pushButton_2.resize(300, 30)
            self.ui.label_7.setText('{} - Keyfile selected error'.format(date_time.now().nice_view))
        #
        self.encrypt_or_decrypt_allowed()
        #
        return 0
    #
    def encrypt_or_decrypt_allowed(self):
        #
        if self.mode and self.path_to_file and self.is_pass:
            self.ui.pushButton_3.setEnabled(True)
        else:
            self.ui.pushButton_3.setEnabled(False)
        #
        return 0
    #
    def make_crypt(self):
        #
        self.ui.pushButton_1.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)
        self.ui.lineEdit_1.setEnabled(False)
        #
        self.make_crypt_in_new_thread = Thread(target=funcs.make_crypt, args=(self, ), daemon=True)
        self.make_crypt_in_new_thread.start()



CSS = '''
QComboBox {
    color: rgb(255, 255, 191);
    background-color: rgb(70, 70, 80);
    selection-background-color: rgb(70, 70, 80);
}
QListView {
    color: rgb(255, 255, 191);
    background-color: rgb(70, 70, 80);
    selection-background-color: rgb(70, 70, 80);
}
'''



def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(CSS)
    main_window = MainWindow()
    main_window.move(300, 100)
    main_window.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
