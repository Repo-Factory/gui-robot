#!/usr/bin/python3
# import os
# from PyQt5.QtCore import QLibraryInfo

# os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = QLibraryInfo.location(
#     QLibraryInfo.PluginsPath
#     )
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys
from home_page.mainwindow import MyWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    qss = "../styles/indigo.qss"
    with open(qss, "r") as fh:
        app.setStyleSheet(fh.read())
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
