import Loader.Loader
from lxml import etree
import xmltodict

class DrugParser:

    VALUE_XPATH = "/drug[name ='{}']"
    name = ""

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
            return drug_xpath(data)[0]

    def get_xml_from_elem(self, elem):
        return etree.tostring(elem)

    def get_dict_from_xml(self, xml):
        #print(xml)
        self.result_dict = xmltodict.parse(xml, process_namespaces=True)
        pass

    def search(self, data):
        i = 0
        result_dict = ''
        lista = list(data)
        print(type(lista))
        for generated_elem in lista:
            # print(type(data))
            # print(type(generated_elem))
            # print(etree.tostring(generated_elem))
            #print(generated_elem)
            #print("iiii")
            i += 1
            print(i)
            print("id elem", generated_elem)
            generated_elem_xml = self.get_xml_from_elem(generated_elem)
            print("GENERATED XML",generated_elem_xml)
            #elem = self.get_elem_from_name(self.name, generated_elem)
            drug_xpath = etree.XPath(("//drug[name ='{}']").format(self.name))
            print("XPATHED ELEM", drug_xpath(generated_elem))
            if drug_xpath(generated_elem):
                elem = drug_xpath(generated_elem)[0]

            #if elem is not None:
                print(type(elem))
                print("ELEM", elem)
                xml = self.get_xml_from_elem(elem)
                self.get_dict_from_xml(xml)
                print("znalazlem", xml)
        return result_dict
        #return self.result_dict

