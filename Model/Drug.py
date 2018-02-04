import collections


class Drug:

    drug_dict = dict()
    general_represent = ''

    def __init__(self, drug_dict):
        """

        :param drug_dict:
        """
        self.drug_dict = drug_dict
        self.general_overview()

    def general_overview(self):
        """

        :return:
        """
        for key, value in self.drug_dict["drug"].items():
            if key in ["name", "drugbank-id", "description"]:
                self.general_represent += "{}: {}\n".format(key.upper(), value)
        return

    def __repr__(self):
        """

        :return:
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

        :param property_list:
        :return:
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

        :param property_dict:
        :return:
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
