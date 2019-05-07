import QtQuick 2.2
import QtQuick.Window 2.2
import OpenGLCube 1.0
 
Window
{
    id: root
    width: Qt.platform.os === "android"? Screen.width: 320
    height: Qt.platform.os === "android"? Screen.height: 480
    visible: true
 
    Cube
    {
        id: cube
        anchors.fill: parent
        ParallelAnimation
        {
            running: true
            NumberAnimation
            {
                target: cube
                property: "rotateAngle"
                from: 0
                to: 360
                duration: 5000
            }
 
            Vector3dAnimation
            {
                target: cube
                property: "axis"
                from: Qt.vector3d( 0, 1, 0 )
                to: Qt.vector3d( 1, 0, 0 )
                duration: 5000
            }
            loops: Animation.Infinite
        }
    }
 
    Rectangle
    {
        anchors.centerIn: parent
        width: textField.width * 1.2
        height: textField.height * 1.5
        radius: textField.height / 3
        color: "lightsteelblue"
        border.color: "white"
        border.width: 2
        Text
        {
            id: textField
            anchors.centerIn: parent
            text: "您好世界！"
            font.pixelSize: root.width / 20
        }
    }
}