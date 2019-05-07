# -*- coding:utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine, qmlRegisterType
from Cube import Cube


if __name__ == "__main__":

    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine("qml/main.qml")
    qmlRegisterType(Cube, "OpenGLCube", 1, 0, "Cube")
    engine.quit.connect(app.quit)
    app.exec_()