import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel
from PyQt5 import QtCore  # Import QtCore module for alignment constants

class InputBoxes(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Input Boxes Example')
        self.setGeometry(100, 100, 800, 500)  # Adjusted window size for visibility

        # Create widgets
        self.input_box1 = QLineEdit(self)
        self.input_box2 = QLineEdit(self)
        self.input_box3 = QLineEdit(self)
        self.input_box4 = QLineEdit(self)
        self.input_box5 = QLineEdit(self)

        # Labels for the input boxes
        self.input_label1 = QLabel('Input 1:', self)
        self.input_label2 = QLabel('Input 2:', self)
        self.input_label3 = QLabel('Input 3:', self)
        self.input_label4 = QLabel('Input 4:', self)
        self.input_label5 = QLabel('Input 5:', self)

        # Set fixed size for box3, box4, box5
        box3_width = 300
        box3_height = 300
        box4_width = 450
        box4_height = 300
        box5_width = 450
        box5_height = 300

        self.input_box3.setFixedSize(box3_width, box3_height)
        self.input_box4.setFixedSize(box4_width, box4_height)
        self.input_box5.setFixedSize(box5_width, box5_height)

        # Set initial sizes for box1 and box2
        bottom_box1_width = 770  # Decreased width for input_box1
        bottom_box2_width = 500  # Increased width for input_box2
        bottom_box_height = 400  # Adjust this height as needed

        self.input_box1.setFixedWidth(bottom_box1_width)
        self.input_box1.setMinimumHeight(bottom_box_height)

        self.input_box2.setFixedWidth(bottom_box2_width)
        self.input_box2.setMinimumHeight(bottom_box_height)

        # Set layout
        main_layout = QVBoxLayout()

        # Top row layout (three boxes)
        top_row_layout = QHBoxLayout()
        top_row_layout.addWidget(self.input_label3)
        top_row_layout.addWidget(self.input_box3)
        top_row_layout.addWidget(self.input_label4)
        top_row_layout.addWidget(self.input_box4)
        top_row_layout.addWidget(self.input_label5)
        top_row_layout.addWidget(self.input_box5)

        # Bottom row layout (two boxes with spacers)
        bottom_row_layout = QHBoxLayout()
        bottom_row_layout.addWidget(self.input_label1)
        bottom_row_layout.addWidget(self.input_box1)
        bottom_row_layout.addStretch()  # Adds stretchable space between box1 and box2
        bottom_row_layout.addWidget(self.input_box2)
        bottom_row_layout.setAlignment(self.input_label1, QtCore.Qt.AlignLeft)  # Align label1 to the left
        bottom_row_layout.setAlignment(self.input_box2, QtCore.Qt.AlignRight)  # Align box2 to the right

        main_layout.addLayout(top_row_layout)
        main_layout.addLayout(bottom_row_layout)

        self.setLayout(main_layout)  
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InputBoxes()
    sys.exit(app.exec_())
