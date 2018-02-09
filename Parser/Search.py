"""
Module providing search functions
"""
from lxml import etree
import xmltodict


class Search:
    """
    Class providing search functions.
    """

    result_dicts_list = []  # contains result as a list of drug elements

    def __init__(self, data, search_dict, search_type=None):
        """
        Initialize Search
        :param data: drug data as generator
        :param search_dict: expected properties as dict
        :param search_type: search_type (used in AdvancedSearch)
        """
        self.search(data, search_dict, search_type=search_type)

    @staticmethod
    def get_xml_from_elem(elem):
        """
        Get XML as string from given ELEM type
        :param elem: ELEM
        :return: XML as string
        """
        return etree.tostring(elem)

    @staticmethod
    def get_dict_from_xml(xml):
        """
        Get OrderedDict element from given XML (string)
        :param xml: as string
        :return: Ordered Dict
        """
        return xmltodict.parse(xml, process_namespaces=True)

    def get_dict_list_from_elem_list(self, list_results):
        """
        Get List of OrderedDicts from List of Elems
        :param list_results: List of Elems
        :return: List of Ordered Dicts
        """

        list_of_elem_dicts = []
        for elem in list_results:
            xml = self.get_xml_from_elem(elem)
            result_dict = self.get_dict_from_xml(xml)
            list_of_elem_dicts.append(result_dict)
        return list_of_elem_dicts

    def search_elem(self, generated_elem, search_dict, search_type=None):
        """
        Search through specific drug to find expected values
        :param generated_elem: drug as elem
        :param search_dict: expected properties as dict
        :param search_type: used in AdvancedSearch
        :return: boolean value, true if drug matches search_dict
        """
        match = False

        for key in search_dict:
            result = generated_elem.findall(key)
            if result:
                specific_node = result[0].text
                # print(specific_node)
                if specific_node and (search_dict[key] in specific_node):
                    match = True
                else:
                    match = False
                    break
            else:
                match = False
                break
        return match

    def search(self, data, search_dict, search_type=None):
        """
        Search through generated data to find drugs with expected properties.
        Saving results as list of orderedDicts into result_dicts_list
        :param data: DB data as drug generator
        :param search_dict: expected properties as dict
        :param search_type: used in AdvancedSearch)
        """

        list_of_elem_results = []

        for generated_elem in data:

            if self.search_elem(generated_elem, search_dict, search_type):
                list_of_elem_results.append(generated_elem)

        self.result_dicts_list = self.get_dict_list_from_elem_list(list_of_elem_results)
        try:
            if not self.result_dicts_list:
                raise ValueError
        except ValueError:
            print("Drug was not found.")

        return
