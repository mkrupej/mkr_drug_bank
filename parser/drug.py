import json

import loader.DatabaseLoader
from lxml import etree
from lxml.etree import tostring
import xmltodict

class DrugParser:

    VALUE_XPATH = "/drugbank/drug[name ='{}']"


    def search_for_drug_by_name(self, name):
        parsed_db = loader.DatabaseLoader.get_db()
        drug_xpath = etree.XPath(self.VALUE_XPATH.format(name))

        result = drug_xpath(parsed_db)
        return drug_xpath(parsed_db)[0]


a = DrugParser()


xml = (etree.tostring(a.search_for_drug_by_name(name="Rasburicase")))

xdict = xmltodict.parse(xml)

print(xdict['drug'])
print(xdict['drug']['products'])