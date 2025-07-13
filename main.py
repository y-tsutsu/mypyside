import os
import random
import sys

from PySide6 import QtCore, QtGui, QtQml

from customproperty import Property, PropertyMeta


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
        self.area = self.whatIsArea(self.length, self.width)

    def whatIsArea(self, length, width):
        result = float(length * width) + random.random()
        return result


def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


def main():
    sys.argv += ['--style', 'Material']

    CURRENT_DIR = os.path.dirname(sys.argv[0])

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseOpenGLES)

    QtQml.qmlRegisterType(Backend, 'MyLibrary', 1, 0, 'Backend')

    app = QtGui.QGuiApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(resource_path('icon.ico')))

    engine = QtQml.QQmlApplicationEngine()

    utils = Utils()
    engine.rootContext().setContextProperty('Utils', utils)

    engine.load(os.path.join(CURRENT_DIR, resource_path('qml/main.qml')))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
