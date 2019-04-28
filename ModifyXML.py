#!/usr/bin/python
import os
import os.path
import xml.dom.minidom


def set_skip_false(pom):
    # parse an xml file by name
    dom = xml.dom.minidom.parse(pom)
    with open('bak_'+pom,'w',encoding='UTF-8') as fh:
        dom.writexml(fh,encoding='UTF-8')
# find skip tag & set false
    items = dom.getElementsByTagName('skip')
    for item in items:
        if "configuration" == item.parentNode.localName:
            item.firstChild.data = "false"
            print("*********** done! set skip false ***********")
    with open(pom,'w',encoding='UTF-8') as fh:
        dom.writexml(fh,indent='',encoding='UTF-8')
    print("*********** ModifyPOM Done! set skip false ***********")


if __name__ == '__main__':
    set_skip_false("pom.xml")

