import QtQuick 2.7
import QtQuick.Controls 2.3
import QtQuick.Scene3D 2.0
// import VertexBufferModel 1.0


ApplicationWindow {
    id: rootWindow
    title: "Grid3D Test"
    width: 800
    height: 600
    visible: true



    // ListView {
    //     model: myModel
    //     delegate: Text {
            
    //         function getData(){
    //             console.log(myModel)
    //         }
    //         text: getData()
    //     }
    // }
    MouseArea {
        id: mouse_area
        anchors.fill: parent  // 有效区域
        onClicked: {
            console.log(con.getData())  // 控制台打印信息
        }
    }

    // Scene3D { //三维场景
    //     id: scene3d
    //     anchors.fill: parent
    //     anchors.margins: 10
    //     focus: true
    //     aspects: ['input', 'logic']
    //     cameraAspectRatioMode: Scene3D.AutomaticAspectRatio
    //     hoverEnabled: true

    //     ShapeRender {}
    // }
   
}
