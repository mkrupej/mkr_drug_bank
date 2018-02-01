from lxml import etree
import xmltodict


class Drug:

    result_dicts_list = []

    def __init__(self, data, search_dict):
        self.result_dicts_list = self.search(data, search_dict)

    @staticmethod
    def get_xml_from_elem(elem):
        return etree.tostring(elem)

    @staticmethod
    def get_dict_from_xml(xml):
        return xmltodict.parse(xml, process_namespaces=True)

    def get_dict_list_from_elem_list(self, list_results):

        list_of_elem_dicts = []
        for elem in list_results:
            xml = self.get_xml_from_elem(elem)
            result_dict = self.get_dict_from_xml(xml)
            list_of_elem_dicts.append(result_dict)
        return list_of_elem_dicts

    @staticmethod
    def search_elem(generated_elem, search_dict):

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

    def search(self, data, search_dict):

        list_of_elem_results = []

        for generated_elem in data:

            if Drug.search_elem(generated_elem, search_dict):
                list_of_elem_results.append(generated_elem)

        list_of_dict_results = self.get_dict_list_from_elem_list(list_of_elem_results)
        return list_of_dict_results
