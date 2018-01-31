#initial commit
import Parser.Drug
import Loader
import locale
from lxml import etree


def get_xml_from_elem(elem):
    return etree.tostring(elem)

def search(data, name):
    i = 0
    result_dict = ''
    #lista = list(data)
    #print("LISTA", lista)
#    tree = etree.parse()
    for generated_elem in data:
        i += 1
        #tree = etree.Element("root")
        #print(etree.tostring(tree.child))
        hoi_parser = etree.XMLParser()
        #print("root",tree)
        result = generated_elem.findall('name')
        for e in result:
            if e.text == name:
                print("GOOOOOOOOOOD")

        if result:
            elem = result[0]
            #print(type(elem))
           # print("ELEM", elem)
            #xml = get_xml_from_elem(elem)
            #print("znalazlem", xml)
#            print("znalazlem", etree.tostring(elem))

 #       print("\n" * 2)
    return result_dict
    # return self.result_dict


#locale.getdefaultlocale = (lambda *args: ['en_US', 'utf8'])
#locale.getlocale = (lambda *arge2s: ['en_US', 'utf8'])
#parsed_db = Loader.DatabaseLoader.get_db()
filename = './Source/minidrug2.xml'
#   filename = './Source/full database.xml'
path = 'drug'
incremental_loader = Loader.Loader.load(filename, path)
search(incremental_loader, "EEEE")

#a = Parser.Drug.DrugParser('AAAA', incremental_loader)

#print(a.result_dict)