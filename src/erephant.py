import sys
from PySide.QtCore import *
from PySide.QtGui import *

if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    appLabel = QLabel()
    appLabel.setText("Hello, World\n Look at my first app PySide")
    appLabel.setAlignment(Qt.AlignCenter)
    appLabel.setWindowTitle("My first App")
    appLabel.setGeometry(300, 300, 250, 175)
    
    appLabel.show()
    
    myApp.exec_()
    sys.exit()