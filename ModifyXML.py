#!/usr/bin/python
import os
import os.path
import sys
import xml.dom.minidom
reload(sys)
sys.setdefaultencoding('utf8')


def set_skip_false(path,f):
    # parse an xml file by name
    pom=os.path.join(path, f)
    dom = xml.dom.minidom.parse(pom)
    bak_pom = os.path.join(path, "bak_pom.xml")
    with open(bak_pom,'w',encoding='UTF-8') as fh:
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


def print_file_name(root_dir):
    for root,dirs,files in os.walk(root_dir):
        ##print("root:",root)
        ##print("dirs:",dirs)
        ##print("files:",files)
        for f in files:
            # print(os.path.join(root, f))
            if f =="pom.xml":
                set_skip_false(root,f)


if __name__ == '__main__':
    print_file_name(".")

