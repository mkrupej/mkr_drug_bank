import enum

import Parser.Search


class SupportedProperties(enum.Enum):
    """
    Extending Enum. Defines supported advanced search types.
    """
    TARGET = "targets", "target"
    PATHWAY = "pathways", "pathway"
    PRODUCT = "products", "product"


class AdvancedSearch(Parser.Search.Search):
    """
    Extending Search class to provide AdvancedSearch through defined SupportedFile values
    """

    def search_elem(self, generated_elem, search_dict, search_type=None):
        """
        Returns true if specific drug matches search criteria
        :param generated_elem: drug as elem
        :param search_dict: expected properties of advanced search as dict
        :param search_type: SupportedProperties enum value defining type of search
        :return:
        """
        match = False
        result = generated_elem.findall(search_type.value[0])
        for elem in result:
            target = elem.findall(search_type.value[1])
            for target_elem in target:
                target_result = super(AdvancedSearch, self).search_elem(target_elem, search_dict)
                if target_result:
                    match = True
        return match
