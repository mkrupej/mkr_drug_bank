import xml.etree.ElementTree
e = xml.etree.ElementTree.parse('full database.xml').getroot()
print(e)

for child in e:
    print(child.tag, child.attrib)
