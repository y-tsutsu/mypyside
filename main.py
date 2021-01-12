import sys
import os
import random

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Signal, Slot, Property


class TwoWayBindedParam(QObject):
    # A class to represent a variable that is two-binded in the Python logic and in QML gui

    def __init__(self, value):
        QObject.__init__(self)
        self.value = value
        self.typeOfParam = type(self.value)  # Determine if its a str, int, float, etc...

    @Signal
    def valueChanged(self):
        pass

    @Slot(int)
    def set(self, value):
        self.value = value
        self.valueChanged.emit()

    def get(self):
        return self.value

    # Problem: I must create different properties for each type
    # In the QML gui, I must use the correct type of property
    # The problem is when creating the Property() object,
    # I can NOT refer to the self.typeOfParam
    # Chagning the type to 'object' doesn't work: https://stackoverflow.com/a/5186587/4988010
    qml_prop_int = Property(int, get, set, notify=valueChanged)
    qml_prop_float = Property(float, get, set, notify=valueChanged)
    qml_prop_bool = Property(bool, get, set, notify=valueChanged)


class MyBackendLogic(QObject):

    def __init__(self, app_engine):
        QObject.__init__(self)

        # The app_engine object is needed to use the function rootContext().setContextProperty()
        # Is there a way to get the current instance of the app_engine that is created in the main
        # without it having to be passed as a paramter to the myBackendLogic() object?
        self.eng = app_engine

        self.init_default_params()

    def init_default_params(self):

        random.seed(23)
        length = random.randint(0, 100)
        width = random.randint(0, 100)
        area = self.whatIsArea(length, width)

        self.length_param = TwoWayBindedParam(length)
        self.eng.rootContext().setContextProperty('length_param', self.length_param)

        self.width_param = TwoWayBindedParam(width)
        self.eng.rootContext().setContextProperty('width_param', self.width_param)

        self.area_param = TwoWayBindedParam(area)
        self.eng.rootContext().setContextProperty('area_param', self.area_param)

        self.continuous_calc_param = TwoWayBindedParam(False)
        self.eng.rootContext().setContextProperty('continuous_calc_param', self.continuous_calc_param)

    def whatIsArea(self, length, width):
        result = float(length * width) + random.random()  # Add some noise
        return result

    @Slot()
    def calculate_area_param(self):
        area = self.whatIsArea(self.length_param.get(), self.width_param.get())
        self.area_param.set(area)


def do_something():
    print('Do something')


def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    mylogic = MyBackendLogic(engine)
    engine.rootContext().setContextProperty('mylogic', mylogic)

    engine.load(os.path.join(os.path.dirname(__file__), 'main.qml'))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
