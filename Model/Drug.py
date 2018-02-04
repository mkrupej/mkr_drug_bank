"""
Module is used to create Drug from Dict
"""

import collections


class Drug:

    drug_dict = dict()  # ordered dict containing properties of drug
    general_represent = ''  # string containing drug [name, id and description]

    def __init__(self, drug_dict):
        """
        Initialize drug item. Set general properties and dictionary.
        :param drug_dict: dict returned from Drug parsing containing single drug element
        """
        self.drug_dict = drug_dict
        self.general_overview()

    def general_overview(self):
        """
        Extracting main properties of the drug [name, id and description] from drug_dict
        """
        for key, value in self.drug_dict["drug"].items():
            if key in ["name", "drugbank-id", "description"]:
                self.general_represent += "{}: {}\n".format(key.upper(), value)
        return

    def __repr__(self):
        """
        Preparing string which contains drug with its every property in readable form
        As this function overwrites standard __repr__ it can be called as print(drug)
        :return: string contains detailed represent of drug
        """

        detailed_represent = 'IDENTIFICATION\n'+self.general_represent

        for key, value in self.drug_dict["drug"].items():
            if key not in ["name", "drugbank-id", "description"]:
                detailed_represent += "\n{} : ".format(key.upper())
                if type(value) is collections.OrderedDict:
                    detailed_represent += "\t{}".format(Drug.extract_from_dict(value))
                else:
                    detailed_represent += "\t{}".format(value)
        return detailed_represent.replace("\n\n", "\n")

    @staticmethod
    def extract_from_list(property_list):
        """
        Extracting drug properties defined within list into string.
        :param property_list: list of properties
        :return: string containing list of properties
        """
        detailed_represent = "\t"
        for elem in property_list:
            if type(elem) is collections.OrderedDict:
                detailed_represent += "\t{}".format(Drug.extract_from_dict(elem))
            elif type(elem) is list:
                detailed_represent += "\t{}".format(elem)
        return detailed_represent

    @staticmethod
    def extract_from_dict(property_dict):
        """
        Extracts properties defined within dict into string.
        :param property_dict: drug dict
        :return: string containing list of properties
        """
        detailed_represent = "\n\t"

        for elem in property_dict:
            # print(type(property_dict[elem]), property_dict[elem])
            detailed_represent += "{} : ".format(elem.upper())
            if type(property_dict[elem]) is collections.OrderedDict:
                detailed_represent += "\t{}".format(Drug.extract_from_dict(property_dict[elem]))
            elif type(property_dict[elem]) is list:
                detailed_represent += "\t{}".format(Drug.extract_from_list(property_dict[elem]))
            else:
                detailed_represent += "{}\n\t".format(property_dict[elem])

        return detailed_represent
