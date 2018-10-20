from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog
)

from process_img import process

# basic GUI setup

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()



########

def selectImage():
    path = QFileDialog.getOpenFileName()[0]
    process(path)

openFileButton = QPushButton('Open an image')
openFileButton.clicked.connect(selectImage)
layout.addWidget(openFileButton)


########


# run the GUI

window.setLayout(layout)
window.show()

app.exec_()
