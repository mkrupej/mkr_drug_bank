import collections
import xml.sax
import Parser

class Drug:

    elem_dict = dict()
    general_represent = ''

    def __init__(self, dict):
        self.elem_dict = dict
        self.general_overview()

    def general_overview(self):
        for key, value in self.elem_dict["drug"].items():
            if key in ["name", "drugbank-id", "description"]:
                self.general_represent += "{}: {}\n".format(key.upper(), value)
        return

    def __repr__(self):

        detailed_represent = 'IDENTIFICATION\n'+self.general_represent

        for key, value in self.elem_dict["drug"].items():
            if key not in ["name", "drugbank-id", "description"]:
                detailed_represent += "\n{} : ".format(key.upper())
                if type(value) is collections.OrderedDict:
                    detailed_represent += Drug.extract_from_dict(value)
                else:
                    detailed_represent += "{}\n".format(value)
        return detailed_represent.replace("\n\n", "\n")

    @staticmethod
    def extract_from_list(property_list):
        detailed_represent = "\t"
        for elem in property_list:
            if type(elem) is collections.OrderedDict:
                detailed_represent += Drug.extract_from_dict(elem)
            elif type(elem) is list:
                detailed_represent += elem
        return detailed_represent

    @staticmethod
    def extract_from_dict(property_dict):
        detailed_represent = "\n\t"

        for elem in property_dict:
           # print(type(property_dict[elem]), property_dict[elem])
            detailed_represent += "{} : ".format(elem.upper())
            if type(property_dict[elem]) is collections.OrderedDict:
                detailed_represent += Drug.extract_from_dict(property_dict[elem])
            elif type(property_dict[elem]) is list:
                detailed_represent += Drug.extract_from_list(property_dict[elem])
            else:
                detailed_represent += "{}\n\t".format(property_dict[elem])

        return detailed_represent



