# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from finddleHelper import Finddle_Helper

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Finddle_Helper()
    window.show()
    sys.exit(app.exec_())
