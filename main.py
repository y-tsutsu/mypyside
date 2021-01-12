import os
import random
import sys

from PySide2 import QtCore, QtGui, QtQml

from customproperty import Property, PropertyMeta


def whatIsArea(length, width):
    result = float(length * width) + random.random()
    return result


class Utils(QtCore.QObject):
    @QtCore.Slot()
    def do_something(self):
        print('Do something')


class Backend(QtCore.QObject, metaclass=PropertyMeta):
    length = Property(0)
    width = Property(0)
    area = Property(0)
    is_continuous = Property(False)

    @QtCore.Slot()
    def calculate_area(self):
        self.area = whatIsArea(self.length, self.width)


def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


def main():
    CURRENT_DIR = os.path.dirname(sys.argv[0])

    QtQml.qmlRegisterType(Backend, 'MyLibrary', 1, 0, 'Backend')

    app = QtGui.QGuiApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(resource_path('icon.ico')))

    engine = QtQml.QQmlApplicationEngine()

    utils = Utils()
    engine.rootContext().setContextProperty('Utils', utils)

    engine.load(os.path.join(CURRENT_DIR, resource_path('main.qml')))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
