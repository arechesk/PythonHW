import xml.etree.ElementTree as ET

a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'


def foo(xml, level=-1, depth=[0]):
    root = ET.fromstring(xml)
    if len(list(root)) == 0:
        depth.append(level+1)
        return {'name':root.tag, 'children':[]}, max(depth)
    else:
        return {'name':root.tag, 'children': [foo(ET.tostring(i),level+1)[0] for i in list(root)]} , max(depth)


if __name__=="__main__":
    print(foo(a))