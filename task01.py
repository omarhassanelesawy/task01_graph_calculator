# importing various libraries
import sys
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
import numpy as np
from numpy import *

def plot_x_y(x,y):
  fig, ax = plt.subplots()
  ax.plot(x, y)
  fig.show()
  return fig,ax

  

def evaluate_expression(equation,x_max,x_min,number_of_points=1000):
  step = (x_max-x_min)/number_of_points
  x = np.arange(x_min,x_max,step)
  y_points = eval(equation.replace('^','**'))
  if(type(y_points) == int):
      y_points = np.full(x.shape,y_points)
  return x,y_points
   
# main window
# which inherits QDialog
class Window(QMainWindow):
       
    # constructor
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Graphs")
        self.setGeometry(400, 400, 700, 400)

        
        layout = QVBoxLayout()

        # expression label and textbox
        exp_lay = QHBoxLayout()

        label = QLabel ('Expression ')
        exp_lay.addWidget(label)
        
        self.exp_text = QLineEdit()
        exp_lay.addWidget(self.exp_text)

        layout.addLayout(exp_lay)

        # max_value label and textbox
        exp_lay = QHBoxLayout()

        label = QLabel ('Max Value ')
        exp_lay.addWidget(label)
        
        self.max_text = QLineEdit()
        exp_lay.addWidget(self.max_text)

        layout.addLayout(exp_lay)

        # min_value label and textbox
        exp_lay = QHBoxLayout()

        label = QLabel ('Min Value ')
        exp_lay.addWidget(label)
        
        self.min_text = QLineEdit()
        exp_lay.addWidget(self.min_text)

        layout.addLayout(exp_lay)

        
        # plot button 
        pb = QPushButton()
        pb.setText("Plot")
        pb.clicked.connect(self.plot)
        layout.addWidget(pb)




        # Setting the parent layout as the main layout
        container = QWidget()
        container.setLayout(layout)
        self.setMenuWidget(container)


        # Open in full screen
        # self.showMaximized()     
    def display_error(self,message_text='Error',auto=True):
        if(auto):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(message_text + " Error")
            msg.setInformativeText('invalid '+message_text+' entered')
            msg.setWindowTitle("Invalid Input")
            msg.exec_()   
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(message_text)
            msg.setInformativeText(message_text)
            msg.setWindowTitle(message_text)
            msg.exec_()   
   
    # action called by the draw button
    def plot(self):

        # get expression,max value,min value from the textbox
        expression = self.exp_text.text()

        try:
            max_value = int(self.max_text.text())
        except:
            self.display_error('Max Value')
            return

        try:
            min_value = int(self.min_text.text())
        except:
            self.display_error('Min Value')
            return

        if(max_value == min_value):
            self.display_error('Min and Max values are equal !!',auto=False)
            return

        # evaluate function
        try:
            x,y = evaluate_expression(expression,max_value,min_value)
        except:
            self.display_error('Expression')
            return

        # plotting function 
        plot_x_y(x,y)
   
# driver code
if __name__ == '__main__':
       
    # creating apyqt5 application
    app = QApplication(sys.argv)
   
    # creating a window object
    main = Window()
       
    # showing the window
    main.show()
   
    # loop
    sys.exit(app.exec_())
