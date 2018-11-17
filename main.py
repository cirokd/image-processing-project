from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QFormLayout,
    QPushButton,
    QFileDialog
)

from PyQt5.QtGui import QIntValidator

from process_img import process

# basic GUI setup
app = QApplication(['Advanced Image Processing Project'])
window = QWidget()
window.setFixedSize(500, 100)
layout = QVBoxLayout()
flo = QFormLayout()
bottom = QHBoxLayout()
layout.addLayout(flo)
layout.addLayout(bottom)

# setup parameter inputs
lineCloseKernelWidth = 40
paragraphCloseKernelHeight = 10

def lckwChanged(val):
    if val != '':
        global lineCloseKernelWidth
        lineCloseKernelWidth = int(val)

def pckwChanged(val):
    if val != '':
        global paragraphCloseKernelHeight
        paragraphCloseKernelHeight = int(val)

e1 = QLineEdit()
e1.setValidator(QIntValidator(1, 100))
e1.setText('40')
e1.textChanged.connect(lckwChanged)
e2 = QLineEdit()
e2.setValidator(QIntValidator(1, 50))
e2.setText('10')
e2.textChanged.connect(pckwChanged)

flo.addRow('Kernel height for joining paragraphs', e2)
flo.addRow('Kernel width for joining lines', e1)

# setup open image button
def selectImage():
    path = QFileDialog.getOpenFileName()[0]
    if path != '':
        process(path, lineCloseKernelWidth, paragraphCloseKernelHeight)

bottom.addWidget(QLabel('Select an image to process!'))

openFileButton = QPushButton('Open an image')
openFileButton.clicked.connect(selectImage)
bottom.addWidget(openFileButton)

# run the GUI
window.setLayout(layout)
window.show()

app.exec_()
