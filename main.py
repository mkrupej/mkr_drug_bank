#initial commit
import Parser.Drug
import Loader
import locale
from lxml import etree

def get_xml_from_elem2(elem):
    return etree.tostring(elem)

def search2(data, search_dict):
    result_dict = ''

    for generated_elem in data:

        for key in search_dict:
            result = generated_elem.findall(key)
            if result:
                specific_node = result[0].text
            #print(specific_node)
                if specific_node and (search_dict[key] in specific_node):
                    print("GOOOOOOOOOOD")
                else:
                    break
            else:
                break

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

#filename = './Source/minidrug2.xml'
filename = './Source/full database.xml'
path = 'drug'
incremental_loader = Loader.Loader.load(filename, path)
search_dict = {"state": 'liquid'}


#search2(incremental_loader, search_dict)

a = Parser.Drug.Drug(incremental_loader, search_dict)
print(a.result_dicts_list)