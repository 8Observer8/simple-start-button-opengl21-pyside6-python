import sys

from OpenGL.GL import *
from PySide6.QtCore import QSize, Qt
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout


class OpenGLWidget(QOpenGLWidget):

    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(300, 300))
        self.setWindowTitle("OpenGL21 PyQt6 Python")

        vbox = QVBoxLayout()
        startButton = QPushButton("Start Game")
        vbox.addWidget(startButton)
        self.setLayout(vbox)

        startButton.clicked.connect(self.onStartButtonClick)

    def initializeGL(self):
        glClearColor(0.1, 0.3, 0.2, 1)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)

    def onStartButtonClick(self):
        print("Start game");

if __name__ == "__main__":
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseDesktopOpenGL)
    app = QApplication(sys.argv)
    widget = OpenGLWidget()
    widget.show()
    sys.exit(app.exec())
