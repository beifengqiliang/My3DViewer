from PySide2.QtCore import QObject


class Cube(QObject):
    def __init__(self):
        print("cube")
        m_VertexBuffer(QOpenGLBuffer.VertexBuffer)
        m_IndexBuffer(QOpenGLBuffer.IndexBuffer)
        m_ColorBuffer(QOpenGLBuffer.VertexBuffer)
        m_RotateAngle(0.0)
        m_Axis(1.0, 1.0, 0.0)
        windowChanged.connect(OnWindowChanged)
    
    def OnWindowChanged(self, pWindow):
        if (pWindow == Q_NULLPTR):
            return
        pWindow.beforeRendering().connect(Render())
        pWindow.setClearBeforeRendering(false)
        
    def Render(self):
        runOnce = RunOnce()
        Q_UNUSED(runOnce)
        
        # 运动
        m_ModelViewMatrix.setToIdentity()
        m_ModelViewMatrix.translate(0.0, 0.0, -60.0)
        m_ModelViewMatrix.rotate(m_RotateAngle, m_Axis.x(), m_Axis.y(), m_Axis.z())
        
        # 渲染
        glViewport(0, 0, window().width(), window().height())
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glFrontFace(GL_CW)
        
        m_ShaderProgram.bind()
        m_VertexBuffer.bind()
        posLoc = m_ShaderProgram.attributeLocation("position")
        m_ShaderProgram.enableAttributeArray(posLoc)
        m_ShaderProgram.setAttributeBuffer(posLoc, GL_FLOAT, 0, 3, 0)
        
        m_ColorBuffer.bind()
        colorLoc = m_ShaderProgram.attributeLocation("color")
        m_ShaderProgram.enableAttributeArray(colorLoc)
        m_ShaderProgram.setAttributeBuffer(colorLoc, GL_FLOAT, 0, 4, 0)
        m_IndexBuffer.bind()
        m_ShaderProgram.setUniformValue("modelViewMatrix", m_ModelViewMatrix)
        m_ShaderProgram.setUniformValue("projectionMatrix", m_ProjectionMatrix)
        glDrawElements(GL_TRIANGLES, 36, GL_UNSIGNED_BYTE, Q_NULLPTR)
        
        m_ShaderProgram.disableAttributeArray(posLoc)
        m_ShaderProgram.disableAttributeArray(colorLoc)
        m_IndexBuffer.release()
        m_VertexBuffer.release()
        m_ShaderProgram.release()
        
    def RunOnce(self):
        # 初始化着色器
        m_ShaderProgram.addShaderFromSourceFile(QOpenGLShader.Vertex, ":/shader/Shader.vsh")
        m_ShaderProgram.addShaderFromSourceFile(QOpenGLShader.Fragment, ":/shader/Shader.fsh")
        m_ShaderProgram.link()
        
        # 初始化顶点缓存
        length = 10.0
        vertices[] =
        {
            length, -length, length,
            length, -length, -length,
            -length, -length, -length,
            -length, -length, length,
            length, length, length,
            length, length, -length,
            -length, length, -length,
            -length, length, length
        }
 
        m_VertexBuffer.setUsagePattern(QOpenGLBuffer.StaticDraw)
        m_VertexBuffer.create()
        m_VertexBuffer.bind()
        m_VertexBuffer.allocate(vertices, sizeof(vertices))
 
        # 初始化颜色的缓存
        const GLfloat colors[] =
        {
            1.0, 0.0, 1.0, 1.0,
            1.0, 0.0, 0.0, 1.0,
            0.0, 0.0, 0.0, 1.0,
            0.0, 0.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 0.0, 1.0,
            0.0, 1.0, 0.0, 1.0,
            0.0, 1.0, 1.0, 1.0
        }
        m_ColorBuffer.setUsagePattern(QOpenGLBuffer.StaticDraw)
        m_ColorBuffer.create()
        m_ColorBuffer.bind()
        m_ColorBuffer.allocate(colors, sizeof(colors))
        
        
        # 初始化索引缓存
        indices[] =
        {
            0, 1, 2, 0, 2, 3,
            7, 6, 4, 6, 5, 4,
            7, 4, 3, 4, 0, 3,
            5, 6, 1, 6, 2, 1,
            4, 5, 0, 5, 1, 0,
            3, 2, 6, 3, 6, 7,
        }
 
        m_IndexBuffer.setUsagePattern(QOpenGLBuffer.StaticDraw)
        m_IndexBuffer.create()
        m_IndexBuffer.bind()
        m_IndexBuffer.allocate(indices, sizeof(indices))
 
        # 设定模型矩阵和投影矩阵
        aspectRatio  = window().width() / window().height()
        m_ProjectionMatrix.perspective(45.0, aspectRatio, 0.5, 500.0)
 
        window().openglContext().aboutToBeDestroyed().connect(Release)
 
        return true
        
    def Release(self):
        qDebug("Vertex buffer and index buffer are to be destroyed.")
        m_VertexBuffer.destroy()
        m_IndexBuffer.destroy()
        m_ColorBuffer.destroy()