import loader.DatabaseLoader
from lxml import etree
from lxml.etree import tostring
import xmltodict

class DrugParser:

    VALUE_XPATH = "/drugbank/drug[name ='{}']"

    name = ""
    result_dict = ""

    def __init__(self, name):
        self.name = name
        self.search()

    def get_elem_from_name(self, name):
        parsed_db = loader.DatabaseLoader.get_db()
        drug_xpath = etree.XPath(self.VALUE_XPATH.format(name))
        result_elem = drug_xpath(parsed_db)[0]
        return result_elem

    def get_xml_from_elem(self, elem):
        return etree.tostring(elem)

    def get_dict_from_xml(self, xml):
        self.result_dict = xmltodict.parse(xml)
        pass

    def search(self):
        elem = self.get_elem_from_name(self.name)
        xml = self.get_xml_from_elem(elem)
        self.get_dict_from_xml(xml)
        return self.result_dict


a = DrugParser("Rasburicase")

print(a.result_dict)