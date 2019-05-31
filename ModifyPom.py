#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import os.path
import xml.etree.ElementTree

def test(pomPath):
    et = xml.etree.ElementTree.parse(pomPath)
    for skip in et.iter('skip'):
        skip.text = str("false")
        skip.set('updated', 'yes')
    et.write('file_new.xml')


if __name__=='__main__':
    test("pom.xml")