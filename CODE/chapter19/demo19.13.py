from PyQt5.QtWidgets import (QWidget, QSlider, 
    QLabel, QApplication)
from PyQt5.QtCore import Qt

import sys

class Slider(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        sld = QSlider(Qt.Horizontal, self)    
        sld.setMinimum(10) 
        sld.setMaximum(500)     
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)
        
        self.label = QLabel(self)      
        self.label.setGeometry(160, 40, 80, 30)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider控件')
        self.show()
                
    def changeValue(self, value):
        self.label.setText(str(value))
       
            

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Slider()
    sys.exit(app.exec_())