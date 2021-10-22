import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setGeometry(300, 300, 300, 220)
    w.setWindowTitle('关闭窗口')    
    qbtn = QPushButton('Quit', w)
    qbtn.clicked.connect(QCoreApplication.instance().quit)
    qbtn.resize(qbtn.sizeHint())
    qbtn.move(50, 50)        
    w.show()
    sys.exit(app.exec_())            
        
