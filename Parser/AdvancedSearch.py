import enum

import Parser.Drug


class SupportedFile(enum.Enum):
    TARGET = "targets", "target"
    PATHWAY = "pathways", "pathway"
    PRODUCT = "products", "product"


class AdvancedSearch(Parser.Drug.Drug):

    def search_elem(self, generated_elem, search_dict, search_type=None):
        match = False
        result = generated_elem.findall(search_type.value[0])
        for elem in result:
            target = elem.findall(search_type.value[1])
            for target_elem in target:
                target_result = super(AdvancedSearch, self).search_elem(target_elem, search_dict)
                if target_result:
                    match = True
        return match