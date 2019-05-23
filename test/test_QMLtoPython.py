from PySide2.QtCore import QUrl, Slot
from PySide2.QtGui import QGuiApplication
from PySide2.QtQuick import QQuickView


@Slot(str)
def outputString(string):
    """
    功能: 输出字符串
    参数: 输出的数据string
    返回值: 无
    """
    print(string)


if __name__ == '__main__':
    path = 'test/test_QMLtoPython.qml'   # 加载的QML文件
    app = QGuiApplication([])
    view = QQuickView()
    view.engine().quit.connect(app.quit)
    view.setSource(QUrl(path))
    view.show()
    context = view.rootObject()
    context.sendClicked.connect(outputString)   # 连接QML信号sendCLicked
    app.exec_()
