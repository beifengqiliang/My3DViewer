import xml.etree.cElementTree as ET


# 对每个grammar的子节点解析
def parseGrammar(root):
    # 遍历grammar的子节点
    for child_of_root in root:
        # <attr> tag解析
        if child_of_root.tag == "attr":
            # print(child_of_root.tag, child_of_root.attrib)
            if child_of_root.get("name") is None:
                print("<attr> tag must contain name attribute.")
            name = child_of_root.get("name")
            # print(name)
            if child_of_root.get("value") is None:
                print("<attr> tag must contain value attribute.")
            value = child_of_root.get("value")
            # print(value)
            if not(child_of_root.get("range") is None):
                range = child_of_root.get("range")
                # print(range)
                # range.push_back(value[0].toFloat())
                # range.push_back(value[1].toFloat())
            # 添加属性
            # if range.size()> 0:
            # grammar.addAttr(name, Attribute(name, value, range[0], range[1]))
            # else:
                # grammar.addAttr(name, Attribute(name, value))
        # <rule> tag解析
        elif child_of_root.tag == "rule":
            # print(child_of_root.tag, child_of_root.attrib)
            if child_of_root.get("name") is None:
                print("<attr> tag must contain name attribute.")
            # 获得规则的名称
            name = child_of_root.get("name")
            # 添加规则
            # grammar.addRule(name)

            # 遍历规则的子节点（各种操作类），读取操作并设置
            for operator_node in child_of_root:
                if operator_node.tag == "copy":
                    print("copy")
                    # grammar.addOperator(name, parseCopyOperator(operator_node))
                elif operator_node.tag == "comp":
                    print("comp")
                    parseCompOperator(operator_node)
                    # addOperator(name, parseCompOperator(operator_node))
                elif operator_node.tag == "color":
                    print("color")
                    # addOperator(name, parseColorOperator(operator_node))
                elif operator_node.tag == "center":
                    print("center")
                elif operator_node.tag == "cornerCut":
                    print("cornerCut")
                elif operator_node.tag == "extrude":
                    print("extrude")
                elif operator_node.tag == "hemisphere":
                    print("hemisphere")
                elif operator_node.tag == "innerArch":
                    print("innerArch")
                elif operator_node.tag == "innerCircle":
                    print("innerCircle")
                elif operator_node.tag == "innerSemiCircle":
                    print("innerSemiCircle")
                elif operator_node.tag == "insert":
                    print("insert")
                elif operator_node.tag == "offset":
                    print("offset")
                elif operator_node.tag == "pyramid":
                    print("pyramid")
                elif operator_node.tag == "roofGable":
                    print("roofGable")
                elif operator_node.tag == "roofHip":
                    print("roofHip")
                elif operator_node.tag == "rotate":
                    print("rotate")
                elif operator_node.tag == "setupProjection":
                    print("setupProjection")
                elif operator_node.tag == "shapeL":
                    print("shapeL")
                elif operator_node.tag == "shapeU":
                    print("shapeU")
                elif operator_node.tag == "size":
                    print("size")
                elif operator_node.tag == "split":
                    print("split")
                elif operator_node.tag == "taper":
                    print("taper")
                elif operator_node.tag == "texture":
                    print("texture")
                elif operator_node.tag == "translate":
                    print("translate")


def parserGrammar(filename):
    file = open(filename, "rb")
    tree = ET.parse(file, parser=None)
    root = tree.getroot()
    print(root.tag, root.attrib)

    for child_of_root in root:
        if child_of_root.tag == "grammar":
            parseGrammar(child_of_root)


def parseCenterOperator(operator_node):
    if operator_node.get("axesSelector") is None:
        print("copy node has to have axesSelector attribute.")
    # 设置axesSelector
    if operator_node.get("axesSelector") == "xyz":
        axesSelector = "AXES_SELECTOR_XYZ"
        print(axesSelector)
    elif operator_node.get("axesSelector") == "x":
        axesSelector = "AXES_SELECTOR_X"
    elif operator_node.get("axesSelector") == "y":
        axesSelector = "AXES_SELECTOR_Y"
    elif operator_node.get("axesSelector") == "z":
        axesSelector = "AXES_SELECTOR_Z"
    elif operator_node.get("axesSelector") == "xy":
        axesSelector = "AXES_SELECTOR_XY"
    elif operator_node.get("axesSelector") == "xz":
        axesSelector = "AXES_SELECTOR_XZ"
    else:
        axesSelector = "AXES_SELECTOR_XYZ"
    # 返回坐标轴值
    # return CenterOperator(axesSelector)


def parseColorOperator(operator_node):
    if operator_node.get("r"):
        r = operator_node.get("r")
    if operator_node.get("g"):
        g = operator_node.get("g")
    if operator_node.get("b"):
        b = operator_node.get("b")
    if operator_node.get("s"):
        s = operator_node.get("s")
    # 返回颜色属性值
    if s is None:
        return ColorOperator(r, g, b)
    else:
        return ColorOperator(s)


def parseCompOperator(operator_node):
    name_map = {}
    for child_node in operator_node:
        if child_node.tag == "param":
            name = child_node.get("name")
            value = child_node.get("value")
            if name == "front":
                name_map["front"] = value
            elif name == "left":
                name_map["left"] = value
            elif name == "right":
                name_map["right"] = value
            elif name == "back":
                name_map["back"] = value
            elif name == "side":
                name_map["side"] = value
            elif name == "top":
                name_map["top"] = value
            elif name == "bottom":
                name_map["bottom"] = value
            elif name == "inside":
                name_map["inside"] = value
            elif name == "border":
                name_map["border"] = value
            elif name == "vertical":
                name_map["vertical"] = value
    print("name_map的键值对")
    print(name_map)
    # return CompOperator(name_map)


def parseCopyOperator(operator_node):
    if operator_node.get("name") is None:
        print("copy node has to have name attribute.")
    copy_name = operator_node.get("name")
    return CopyOperator(copy_name)


def parseCornerCutOperator(operator_node):
    if operator_node.get("type") is None:
        print("curnerCut node has to have type attribute.")
    if operator_node.get("type") == "straight":
        CornerCutType = "CORNER_CUT_STRAIGHT"
    elif operator_node.get("type") == "curve":
        CornerCutType = "CORNER_CUT_CURVE"
    else:
        CornerCutType = "CORNER_CUT_NEGATIVE_CURVE"
    if operator_node.get("length") is None:
        print("curnerCut node has to have length attribute.")
    length = operator_node.get("length")
    return CornerCutOperator(CornerCutType, length)


# 切角操作
def parseExtrudeOperator(operator_node):
    if operator_node.get("height") is None:
        print("extrude node has to have height attribute.")
    height = operator_node.get("height")
    return ExtrudeOperator(height)


# 半球形状操作
def parseHemisphereOperator(operator_node):
    return HemisphereOperator()


def parseInnerArchOperator(operator_node):
    inside = operator_node.get("inside")
    border = operator_node.get("border")
    return InnerArchOperator(inside, border)


# 内圆操作
def parseInnerCircleOperator(operator_node):
    return InnerCircleOperator()


# 内半圆操作
def parseInnerSemiCircleOperator(operator_node):
    return InnerSemiCircleOperator()


# 插入操作
def parseInsertOperator(operator_node):
    if operator_node.get("geometryPath") is None:
        print("insert node has to have geometryPath attribute.")
    geometryPath = operator_node.get("geometryPath")
    return InsertOperator(geometryPath)


def parseOffsetOperator(operator_node):
    if operator_node.get("offsetDistance") is None:
        print("offset node has to have offsetDistance attribute.")
    offsetDistance = operator_node.get("offsetDistance")
    inside = operator_node.get("inside")
    border = operator_node.get("border")
    return OffsetOperator(offsetDistance, inside, border)


# 椎体操作
def parsePyramidOperator(operator_node):
    if operator_node.get("height") is None:
        print("pyramid node has to have height attribute.")
    height = operator_node.get("height")
    return PyramidOperator(height)


def parseRoofGableOperator(operator_node):
    if operator_node.get("angle") is None:
        print("roofGable node has to have angle attribute.")
    angle = operator_node.get("angle")
    return RoofGableOperator(angle)


def parseRoofHipOperator(operator_node):
    if operator_node.get("angle") is None:
        print("roofHip node has to have angle attribute.")
    angle = operator_node.get("angle")
    return RoofHipOperator(angle)


def parseRotateOperator(operator_node):
    for child_node in operator_node:
        if not(child_node is None):
            if child_node.tag == "param":
                name = operator_node.get("name")
                if name == "xAngle":
                    xAngle = operator_node.get("xAngle")
                elif name == "yAngle":
                    yAngle = operator_node.get("yAngle")
                elif name == "zAngle":
                    zAngle = operator_node.get("zAngle")
    return RotateOperator(xAngle, yAngle, zAngle)


def parseSetupProjectionOperator(operator_node):
    if operator_node.get("axesSelector") is None:
        print("setupProjection node has to have axesSelector attribute.")
    sAxesSelector = operator_node.get("axesSelector")
    if sAxesSelector == "scope.xy":
        axesSelector = "AXES_SCOPE_XY"
    elif sAxesSelector == "scope.xz":
        axesSelector = "AXES_SCOPE_XZ"
    else:
        axesSelector = "AXES_SCOPE_XY"
    for child_node in operator_node:
        if child_node.tag == "param":
            name = child_node.get("name")
            if name == "texWidth":
                texWidthType = child_node.get("type")
                # 字符串转数字：数字 = string.atof("")
                value = child_node.get("value")
                if texWidthType == "absolute":
                    texWidth = abs(value)
                elif texWidthType == "relative":
                    texWidth = value
                else:
                    print("type of texWidth for texture has to be either absolute or relative.")
            elif name == "texHeight":
                texHeightType = child_node.get("type")
                value = child_node.get("value")
                if texHeightType == "absolute":
                    texHeight = abs(value)
                elif texHeightType == "relative":
                    texHeight = value
                else:
                    print("type of texHeight for texture has to be either absolute or relative.")
    SetupProjectionOperator(axesSelector, texWidth, texHeight)


def parseShapeLOperator(operator_node):
    frontWidthFound = False
    rightWidthFound = False

    for child_node in operator_node:
        if child_node.tag == "param":
            name = child_node.get("name")
            if child_node.get("type") is None:
                print("param node under size node has to have type attribute.")
            shapeLType = child_node.get("type")
            value = child_node.get("value")
            if name == "frontWidth":
                frontWidthFound = True
                if shapeLType == "absolute":
                    frontWidth = abs(value)
                elif shapeLType == "relative":
                    frontWidth = value
                else:
                    print("type attribute under shapeL node has to be either relative or absolute.")
            elif name == "rightWidth":
                rightWidthFound = True
                if shapeLType == "absolute":
                    rightWidth = abs(value)
                elif shapeLType == "relative":
                    rightWidth = value
                else:
                    print("type attribute under shapeL node has to be either relative or absolute.")
    if frontWidthFound is False:
        print("shapeL node has to have frontWidth parametter.")
    if rightWidthFound is False:
        print("shapeL node has to have rightWidth parametter.")
    return ShapeLOperator(frontWidth, rightWidth)


def parseShapeUOperator(operator_node):
    frontWidthFound = False
    backDepthFound = False
    for child_node in operator_node:
        if child_node.tag == "param":
            name = child_node.get("name")
            if child_node.get("type") is None:
                print("param node under size node has to have type attribute.")
            shapeUType = child_node.get("type")
            value = child_node.get("value")
            if name == "frontWidth":
                frontWidthFound = True
                if shapeUType == "absolute":
                    frontWidth = abs(value)
                elif shapeUType == "relative":
                    frontWidth = value
                else:
                    print("type attribute under shapeU node has to be either relative or absolute.")
            elif name == "backDepth":
                backDepthFound = True
                if shapeUType == "absolute":
                    backDepth = abs(value)
                elif shapeUType == "relative":
                    backDepth = value
                else:
                    print("type attribute under shapeU node has to be either relative or absolute.")
    if frontWidthFound is False:
        print("shapeU node has to have frontWidth parametter.")
    if backDepthFound is False:
        print("shapeU node has to have rightWidth parametter.")
    return ShapeUOperator(frontWidth, backDepth)


def parseSizeOperator(operator_node):
    centered = False
    if not(operator_node.get("centered") is None):
        if operator_node.get("centered") == "true":
            centered = True
    for child_node in operator_node:
        if child_node.tag == "param":
            name = child_node.get("name")
            if child_node.get("type") is None:
                print("param node under size node has to have type attribute.")
            sizeType = child_node.get("type")
            value = child_node.get("value")
            if name == "xSize":
                if sizeType == "relative":
                    xSize = value
                elif sizeType == "absolute":
                    xSize = value
                else:
                    print("type attribute under size node has to be either relative or absolute.")
            elif name == "ySize":
                if sizeType == "relative":
                    ySize = value
                elif sizeType == "absolute":
                    ySize = value
                else:
                    print("type attribute under size node has to be either relative or absolute.")
            elif name == "zSize":
                if sizeType == "relative":
                    zSize = value
                elif sizeType == "absolute":
                    zSize = value
                else:
                    print("type attribute under size node has to be either relative or absolute.")
    return SizeOperator(xSize, ySize, zSize, centered)


def parseSplitOperator(operator_node):
    if operator_node.get("splitAxis") is None:
        print("split node has to have splitAxis attribute.")
    if operator_node.get("splitAxis") == "x":
        splitAxis = "DIRECTION_X"
    elif operator_node.get("splitAxis") == "y":
        splitAxis = "DIRECTION_Y"
    else:
        splitAxis = "DIRECTION_Z"
    for child_node in operator_node:
        if child_node.tag == "param":
            splitType = child_node.get("type")
            value = child_node.get("value")
            repeat = False
            if not(child_node.get("repeat") is None):
                repeat = True
            if repeat:
                if splitType == "absolute":
                    print(value)
                    # sizes.push_back(Value(Value::TYPE_ABSOLUTE, value, true))
                elif splitType == "relative":
                    print(value)
                    # sizes.push_back(Value(Value::TYPE_RELATIVE, value, true))
                else:
                    print(value)
                    # sizes.push_back(Value(Value::TYPE_FLOATING, value, true))
            else:
                if splitType == "absolute":
                    print(value)
                    # sizes.push_back(Value(Value::TYPE_ABSOLUTE, value))
                elif splitType == "relative":
                    print(value)
                    # sizes.push_back(Value(Value::TYPE_RELATIVE, value))
                else:
                    print(value)
                    # sizes.push_back(Value(Value::TYPE_FLOATING, value))
            # names.push_back(name)
    # return SplitOperator(splitAxis, sizes, names)


def parseTaperOperator(operator_node):
    if operator_node.get("height") is None:
        print("taper node has to have height attribute.")
    if operator_node.get("slope") is None:
        print("taper node has to have slope attribute.")
    height = operator_node.get("height")
    slope = operator_node.get("slope")
    # return TaperOperator(height, slope)


def parseTextureOperator(operator_node):
    if operator_node.get("texturePath") is None:
        print("texture node has to have texturePathtexturePath attribute.")
    texture = operator_node.get("texturePath")
    # return TextureOperator(texture)


def parseTranslateOperator(operator_node):
    if operator_node.get("mode") is None:
        print("translate node has to have mode attribute.")
    if operator_node.get("mode") == "abs":
        mode = "MODE_ABSOLUTE"
    elif operator_node.get("mode") == "rel":
        mode = "MODE_RELATIVE"
    else:
        print("mode has to be either abs or rel.")
    # 坐标系统
    if operator_node.get("coordSystem") is None:
        print("translate node has to have coordSystem attribute.")
    if operator_node.get("coordSystem") == "world":
        coordSystem = "COORD_SYSTEM_WORLD"
    elif operator_node.get("coordSystem") == "object":
        coordSystem = "COORD_SYSTEM_OBJECT"
    else:
        print("coordSystem has to be either world or object.")
    # 读取参数param
    for child_node in operator_node:
        if child_node is None:
            break
        else:
            if child_node.tag == "param":
                if child_node.get("name") is None:
                    print("param has to have name attribute.")
                else:
                    name = child_node.get("name")
                if child_node.get("value") is None:
                    print("param has to have value attribute.")
                else:
                    value = child_node.get("value")
                if child_node.get("type") is None:
                    print("param has to have type attribute.")
                else:
                    translateType = child_node.get("type")
                if name == "x":
                    if translateType == "absolute":
                        # x=abs(value)
                        x = value
                    elif translateType == "relative":
                        x = value
                    else:
                        print("type of param for translate has to be either absolute or relative.")
                elif name == "y":
                    if translateType == "absolute":
                        # y=abs(value)
                        y = value
                    elif translateType == "relative":
                        y = value
                    else:
                        print("type of param for translate has to be either absolute or relative.")
                elif name == "z":
                    if translateType == "absolute":
                        # z=abs(value)
                        z = value
                    elif translateType == "relative":
                        z = value
                    else:
                        print("type of param for translate has to be either absolute or relative.")
    # return TranslateOperator(mode, coordSystem, x, y, z)


if __name__ == "__main__":
    parserGrammar('test/01.xml')
