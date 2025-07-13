import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Controls.Material

import MyLibrary 1.0

ApplicationWindow {
    title: qsTr("Hello World")
    width: 800
    height: 480
    visible: true

    Material.theme: Material.Dark
    Material.accent: Material.Pink

    Backend {
        id: backend
        length: 55
        width: 87
        Component.onCompleted: calculate_area()
    }

    Column {
        id: column
        x: 131
        y: 63
        width: 72
        height: 263

        Label {
            id: label_length
            text: backend.length
            font.pointSize: 12
        }

        Slider {
            id: slider_length
            to: 100
            orientation: Qt.Vertical
            value: backend.length
            onValueChanged: {
                backend.length = value;
                if (backend.is_continuous) {
                    backend.calculate_area();
                }
            }
        }
    }

    Column {
        id: column1
        x: 249
        y: 63
        width: 72
        height: 263

        Label {
            id: label_width
            text: backend.width
            font.pointSize: 12
        }

        Slider {
            id: slider_width
            to: 100
            value: backend.width
            orientation: Qt.Vertical
            onValueChanged: {
                backend.width = value;
                if (backend.is_continuous) {
                    backend.calculate_area();
                }
            }
        }
    }

    Row {
        id: row
        x: 110
        y: 332
        width: 274
        height: 53

        Slider {
            id: slider_area
            to: 10000
            value: backend.area
        }

        Label {
            id: label_area
            text: backend.area
            font.pointSize: 12
        }
    }

    Switch {
        id: continuous_switch
        x: 343
        y: 149
        text: qsTr("Continuous calculate")
        checked: backend.is_continuous
        onCheckedChanged: backend.is_continuous = checked
        font.pointSize: 12
    }

    Button {
        id: button
        x: 383
        y: 205
        text: qsTr("Calculate")
        onClicked: {
            backend.calculate_area();
        }
        font.pointSize: 12
    }

    Label {
        id: labelCaption_length
        x: 131
        y: 23
        text: qsTr("Length")
        font.pointSize: 12
    }

    Label {
        id: labelCaption_width
        x: 249
        y: 23
        text: qsTr("Width")
        font.pointSize: 12
    }

    Label {
        id: labelCaption_area
        x: 196
        y: 377
        text: qsTr("Area")
        font.pointSize: 12
    }

    Component.onCompleted: Utils.do_something()
}
