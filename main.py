from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QCheckBox,
    QLineEdit,
    QFormLayout,
    QPushButton,
    QFileDialog
)
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt

from process_img import process

# basic GUI setup
app = QApplication(['Advanced Image Processing Project'])
window = QWidget()
window.setFixedSize(500, 200)
layout = QVBoxLayout()
flo = QFormLayout()
bottom = QHBoxLayout()
layout.addLayout(flo)
layout.addLayout(bottom)

# setup flags
segmentCharacters = False
segmentLines = True
segmentParagraphs = True

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

def flagChanged(flag):
    checked = lambda state: state == Qt.Checked
    if flag == 'characters':
        def f(state):
            global segmentCharacters
            segmentCharacters = checked(state)
        return f
    if flag == 'lines':
        def f(state):
            global segmentLines
            segmentLines = checked(state)
        return f
    if flag == 'paragraphs':
        def f(state):
            global segmentParagraphs
            segmentParagraphs = checked(state)
        return f

c1 = QCheckBox()
c1.setChecked(segmentCharacters)
c1.stateChanged.connect(flagChanged('characters'))
c2 = QCheckBox()
c2.setChecked(segmentLines)
c2.stateChanged.connect(flagChanged('lines'))
c3 = QCheckBox()
c3.setChecked(segmentParagraphs)
c3.stateChanged.connect(flagChanged('paragraphs'))

e1 = QLineEdit()
e1.setValidator(QIntValidator(1, 100))
e1.setText('40')
e1.textChanged.connect(lckwChanged)
e2 = QLineEdit()
e2.setValidator(QIntValidator(1, 50))
e2.setText('10')
e2.textChanged.connect(pckwChanged)

flo.addRow('Segment characters', c1)
flo.addRow('Segment lines', c2)
flo.addRow('Segment paragraphs', c3)
flo.addRow('Kernel height for joining paragraphs', e2)
flo.addRow('Kernel width for joining lines', e1)

# setup open image button
def selectImage():
    path = QFileDialog.getOpenFileName()[0]
    if path != '':
        flags = {
            'characters': segmentCharacters,
            'lines': segmentLines,
            'paragraphs': segmentParagraphs
        }
        process(path, flags, lineCloseKernelWidth, paragraphCloseKernelHeight)

bottom.addWidget(QLabel('Select an image to process!'))

openFileButton = QPushButton('Open an image')
openFileButton.clicked.connect(selectImage)
bottom.addWidget(openFileButton)

# run the GUI
window.setLayout(layout)
window.show()

app.exec_()
