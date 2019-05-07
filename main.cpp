#include <QApplication>
#include <QQmlApplicationEngine>
#include "Cube.h"
 
int main( int argc, char** argv )
{
    QApplication app( argc, argv );
 
    qmlRegisterType<Cube>( "OpenGLCube", 1, 0, "Cube" );
 
    QQmlApplicationEngine engine;
    engine.load( QUrl( QStringLiteral( "qrc:///main.qml" ) ) );
 
    return app.exec( );
}