import Loader.Loader
from lxml import etree
import xmltodict

class DrugParser:

    VALUE_XPATH = "//drug[name ='{}']"

    name = ""
    result_dict = ""

    def __init__(self, name, data):
        self.name = name
        self.search(data)

    def get_elem_from_name(self, name, data):
        drug_xpath = etree.XPath(self.VALUE_XPATH.format(name))
        print(self.VALUE_XPATH.format(name))
        print(etree.tostring(data))
        if not (drug_xpath(data)):
            pass
        else:
            print("XXXXXX")
            return drug_xpath(data)[0]

    def get_xml_from_elem(self, elem):
        return etree.tostring(elem)

    def get_dict_from_xml(self, xml):
        print("REZULTADO")
        print(xml)
        self.result_dict = xmltodict.parse(xml, process_namespaces=True)
        pass

    def search(self, data):
        i = 0
        for generated_elem in data:
            # print(type(data))
            # print(type(generated_elem))
            # print(etree.tostring(generated_elem))
            #print(generated_elem)
            #print("iiii")
            i += 1
            print(i)
            elem = self.get_elem_from_name(self.name, generated_elem)
            print("ELEM", elem)
            if elem is not None:
                xml = self.get_xml_from_elem(elem)
                self.get_dict_from_xml(xml)
        return self.result_dict


