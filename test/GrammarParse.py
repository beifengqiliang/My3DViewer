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
                    # grammar.addOperator(name, parseCompOperator(operator_node))
                elif operator_node.tag == "color":
                    print("color")
                    # grammar.addOperator(name, parseColorOperator(operator_node))
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
    return CenterOperator(axesSelector)


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


if __name__ == "__main__":
    parserGrammar('test/01.xml')
