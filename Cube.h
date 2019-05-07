#ifndef CUBE_H
#define CUBE_H
 
#include <QVector3D>
#include <QMatrix4x4>
#include <QOpenGLFunctions>
#include <QOpenGLBuffer>
#include <QOpenGLShaderProgram>
#include <QQuickItem>
#include <QQuickWindow>
 
#define DECLRARE_Q_PROPERTY( aType, aProperty ) protected:\
    aType m_ ## aProperty; public:\
    aType aProperty( void ) { return m_ ## aProperty; } \
    void set ## aProperty( aType _ ## aProperty ) \
    {\
        m_ ## aProperty = _ ## aProperty;\
        if ( window( ) != Q_NULLPTR )\
        {\
            window( )->update( );\
        }\
    }
 
class Cube: public QQuickItem
{
    Q_OBJECT
    Q_PROPERTY( qreal rotateAngle READ RotateAngle
                WRITE setRotateAngle NOTIFY RotateAngleChanged )
    Q_PROPERTY( QVector3D axis READ Axis
                WRITE setAxis NOTIFY AxisChanged )
public:
    explicit Cube( void );
signals:
    void RotateAngleChanged( void );
    void AxisChanged( void );
protected slots:
    void Render( void );
    void OnWindowChanged( QQuickWindow* pWindow );
    void Release( void );
protected:
    bool RunOnce( void );
 
    QMatrix4x4                  m_ModelViewMatrix;
    QMatrix4x4                  m_ProjectionMatrix;
    QOpenGLBuffer               m_VertexBuffer, m_IndexBuffer;
    QOpenGLBuffer               m_ColorBuffer;
    QOpenGLShaderProgram        m_ShaderProgram;
 
    DECLRARE_Q_PROPERTY( qreal, RotateAngle )
    DECLRARE_Q_PROPERTY( QVector3D, Axis )
};
 
#endif // CUBE_H