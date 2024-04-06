# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from finddleHelper import FinddleHelper

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FinddleHelper()
    window.show()
    sys.exit(app.exec_())
