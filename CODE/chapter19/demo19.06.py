import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class CenterWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        self.resize(250, 150)
        self.center()        
        self.setWindowTitle('窗口居中')    
        self.show()
    def center(self):        
        qr = self.frameGeometry()
        desktop = app.desktop()
        self.move((desktop.width() - self.width())/2,(desktop.height() - self.height())/2)
     
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = CenterWindow()
    sys.exit(app.exec_())