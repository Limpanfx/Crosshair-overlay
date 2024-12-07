from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class CrosshairOverlay(QtWidgets.QWidget):
    def __init__(self, size=20, color=(255, 0, 0, 255), thickness=2):
        super().__init__()
        self.size = size
        self.color = color
        self.thickness = thickness
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        self.setGeometry(0, 0, screen.width(), screen.height())
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowTransparentForInput)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        pen = QtGui.QPen(QtGui.QColor(*self.color), self.thickness)
        painter.setPen(pen)
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        center_x = screen.width() // 2
        center_y = screen.height() // 2
        painter.drawLine(center_x - self.size, center_y, center_x + self.size, center_y)
        painter.drawLine(center_x, center_y - self.size, center_x, center_y + self.size)

def main():
    app = QtWidgets.QApplication(sys.argv)
    overlay = CrosshairOverlay(size=20, color=(0, 255, 0, 255), thickness=3)
    overlay.showFullScreen()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
