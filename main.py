from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog
)

from process_img import process

# basic GUI setup
app = QApplication(['Advanced Image Processing Project'])
window = QWidget()
window.setFixedSize(500, 50)
layout = QHBoxLayout()

layout.addWidget(QLabel('Select an image to process!'))

# setup open image button
def selectImage():
    path = QFileDialog.getOpenFileName()[0]
    if path != '':
        process(path)

openFileButton = QPushButton('Open an image')
openFileButton.clicked.connect(selectImage)
layout.addWidget(openFileButton)

# run the GUI
window.setLayout(layout)
window.show()

app.exec_()
