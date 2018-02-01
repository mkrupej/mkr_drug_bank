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

        detailed_represent = ''

        for key, value in self.elem_dict["drug"].items():
            if key in ["name", "drugbank-id", "description"]:
                self.general_represent += "{}: {}\n".format(key.upper(), value)
                #print("{}: {}".format(key.upper(), value))
        #for key, value in self.elem_dict["drug"].items():
            #print("{} wartosc {}".format(key.upper(), value))
        return detailed_represent
