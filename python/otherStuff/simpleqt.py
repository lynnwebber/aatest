#!/usr/bin/python
#

import sys
from PyQt4 import QtGui

# ---- main -----
def main():
    '''
    build a widget
    '''
    app = QtGui.QApplication(sys.argv)
    widget = QtGui.QWidget()
    widget.resize(250, 150)
    widget.setWindowTitle('Simple test')
    widget.show()

    sys.exit(app.exec_())

# ---------- run main -------------
if __name__ == "__main__":
    main()
