from PySide2.QtCore import QUrl, QObject, Slot, Signal, Qt
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQml import qmlRegisterType
from PySide2.Qt3DRender import Qt3DRender
from PySide2.QtGui import QGuiApplication, QVector3D
from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView

import sys
import numpy as np
from array import array
import os


class VertexBuffer(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.data = [10.0, 0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 15.0, 0.0]

    @Slot(result=list)
    def getData(self): 
        return self.data


if __name__ == "__main__": 

    app = QApplication(sys.argv)
   
    qml_file = os.path.join(os.path.dirname(__file__), "main.qml")
    engine = QQmlApplicationEngine()

    # qmlRegisterType(VertexBufferModel, "VertexBufferModel", 1, 0, "VertexBufferModel")

    con = VertexBuffer()
    context = engine.rootContext()
    context.setContextProperty("con", con)

    # data = [10.0, 0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 15.0, 0.0]
    # my_model = QStringListModel()
    # my_model.setStringList(data)
    # engine.rootContext().setContextProperty("myModel", my_model)

    # QML的相对路径
    engine.load(os.path.normpath(qml_file))

    if not engine.rootObjects():
        sys.exit(-1) 

    app.exec_()