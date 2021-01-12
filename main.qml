import QtQuick 2.13
import QtQuick.Window 2.13
import QtQuick.Controls 2.2

Window {
    title: qsTr("Hello World")
    width: 640
    height: 480
    visible: true

    Column {
        id: column
        x: 131
        y: 63
        width: 72
        height: 263

        TextInput {
            id: textInput_length
            width: 80
            height: 20
            text: length_param.qml_prop_int
            font.pixelSize: 12
        }

        Slider {
            id: slider_length
            to: 100
            orientation: Qt.Vertical
            value: length_param.qml_prop_int
            onValueChanged: {
                length_param.set(value)
                if (continuous_switch.checked) { mylogic.calculate_area_param() }
            }
        }
    }

    Column {
        id: column1
        x: 249
        y: 63
        width: 72
        height: 263

        TextInput {
            id: textInput_width
            width: 80
            height: 20
            text: width_param.qml_prop_int
            font.pixelSize: 12
        }

        Slider {
            id: slider_width
            to: 100
            value: width_param.qml_prop_int
            orientation: Qt.Vertical
            onValueChanged: {
                width_param.set(value)
                if (continuous_switch.checked) { mylogic.calculate_area_param() }
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
            value: area_param.qml_prop_float
        }

        Label {
            id: label_area
            text: area_param.qml_prop_float
        }
    }

    Switch {
        id: continuous_switch
        x: 343
        y: 149
        text: qsTr("Continuous calculate")
        checked: continuous_calc_param.qml_prop_bool
    }

    Button {
        id: button
        x: 383
        y: 205
        text: qsTr("Calculate")
        onClicked: {
            mylogic.calculate_area_param()
        }
    }

    Label {
        id: label
        x: 131
        y: 23
        text: qsTr("Length")
        font.pointSize: 12
    }

    Label {
        id: label1
        x: 249
        y: 23
        text: qsTr("Width")
        font.pointSize: 12
    }

    Label {
        id: label3
        x: 196
        y: 377
        text: qsTr("Area")
        font.pointSize: 12
    }
}