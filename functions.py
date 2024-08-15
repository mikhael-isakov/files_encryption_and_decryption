import os, sys
from PyQt5.QtGui import QIcon, QPixmap, QFont
import pyAesCrypt
from classes import date_time


def resource_path(relative_path, in_catalog='icons'):
    #
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(os.path.join(os.getcwd(), in_catalog))
    #
    return os.path.join(base_path, relative_path)


def set_window_sizes(obj):
    #
    obj.setFixedSize(obj.width(), obj.height())
    #
    return 0


def set_icons_and_title(obj):
    #
    obj.setWindowIcon(QIcon(resource_path('main_icon.ico')))
    obj.ui.label_1.setPixmap(QPixmap(resource_path('key.png')))
    obj.setWindowTitle(' Encrypting files using the AES standard')
    obj.ui.label_8.setPixmap(QPixmap(resource_path('green.png')))
    obj.ui.label_9.setPixmap(QPixmap(resource_path('green.png')))
    obj.ui.label_10.setPixmap(QPixmap(resource_path('green.png')))
    #
    return 0


def set_fonts(obj):
    #
    obj.font_courier_24_bold = QFont('Courier'); obj.font_courier_24_bold.setPixelSize(24); obj.font_courier_24_bold.setBold(True)
    obj.font_arial_16 = QFont('Arial'); obj.font_arial_16.setPixelSize(16); obj.font_arial_16.setBold(False)
    #
    obj.ui.label_2.setFont(obj.font_courier_24_bold)
    obj.ui.label_7.setFont(obj.font_arial_16)
    #
    return 0


def set_buttons_hover_properties(obj):
    #
    color_code = '#E7FFDD'
    #
    for i in range(1, 3+1):
        getattr(obj.ui, 'pushButton_{}'.format(i)).setStyleSheet("""
        QPushButton {
            color: rgb(176, 230, 134);
            background-color: rgb(70, 70, 80);
        }
        QPushButton:hover {
            color: rgb(176, 230, 134);
            background-color: rgb(50, 50, 60);
        }
        """)
    #
    return 0


def make_crypt(obj):
    #
    # Функция реализует работу по шифрованию (encrypt) или дешифрованию (decrypt) файла obj.file_for_work,
    # в зависимости от параметра obj.mode.
    #
    key = obj.pass_hash + obj.keyfile_hash
    buffer_size = 512 * 1024  # размер буфера в байтах
    #
    if obj.mode == 'encrypt':
        try:
            obj.ui.label_7.setText('{} - Encrypting start'.format(date_time.now().nice_view))
            pyAesCrypt.encryptFile(obj.path_to_file, obj.path_to_file+'_encr', key, buffer_size)
            obj.ui.label_7.setText('{} - Encrypting done'.format(date_time.now().nice_view))
        except:
            obj.ui.label_7.setText('{} - Encrypting error'.format(date_time.now().nice_view))
    #
    elif obj.mode == 'decrypt':
        try:
            obj.ui.label_7.setText('{} - Decrypting start'.format(date_time.now().nice_view))
            pyAesCrypt.decryptFile(obj.path_to_file, obj.path_to_file+'_decr', key, buffer_size)
            obj.ui.label_7.setText('{} - Decrypting done'.format(date_time.now().nice_view))
        except:
            obj.ui.label_7.setText('{} - Decrypting error'.format(date_time.now().nice_view))
    #
    obj.ui.pushButton_1.setEnabled(True)
    obj.ui.pushButton_2.setEnabled(True)
    obj.ui.pushButton_3.setEnabled(True)
    obj.ui.lineEdit_1.setEnabled(True)
    #
    return 0
