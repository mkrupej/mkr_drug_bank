import unittest
import Parser
import Model
import main


class FindTargetedDrugTestCase(unittest.TestCase):
    """
    Functional TestCases for Target search using different set of properties.
    """

    def test_find_targeted_drug_by_empy_dict_error_case(self):
        search_dict = {}
        a = Parser.AdvancedSearch.AdvancedSearch(main.incremental_loader, search_dict, search_type=Parser.AdvancedSearch.SupportedFile.TARGET)
        self.assertLess(len(a.result_dicts_list), 1)


    def test_find_drug_by_target(self):
        search_dict = {"name": 'Prothrombin'}
        name = {"name" : "Lepirudin"}
        a = Parser.AdvancedSearch.AdvancedSearch(main.incremental_loader, search_dict, search_type=Parser.AdvancedSearch.SupportedFile.TARGET)
        match = False
        for elem in a.result_dicts_list:
            drug = Model.Drug.Drug(elem)
            print(drug.general_represent)
            if (name["name"] in drug.general_represent):
                match = True
        self.assertTrue(match)


    def test_find_drug_by_target_error_case(self):
        search_dict = {"name": 'non existing'}
        a = Parser.AdvancedSearch.AdvancedSearch(main.incremental_loader, search_dict, search_type=Parser.AdvancedSearch.SupportedFile.TARGET)
        self.assertLess(len(a.result_dicts_list), 1)


    def test_find_multiple_drugs_by_pathway(self):
        search_dict = {"name": 'Prothrombin'}
        a = Parser.AdvancedSearch.AdvancedSearch(main.incremental_loader, search_dict, search_type=Parser.AdvancedSearch.SupportedFile.TARGET)
        self.assertGreater(len(a.result_dicts_list), 1)


    def test_find_drug_by_multiple_pathway_properties_(self):
        search_dict = {"organism": 'Human', "id": "BE0000048"}
        a = Parser.AdvancedSearch.AdvancedSearch(main.incremental_loader, search_dict, search_type=Parser.AdvancedSearch.SupportedFile.TARGET)
        for elem in a.result_dicts_list:
            drug = Model.Drug.Drug(elem)
            print(drug.general_represent)
        self.assertGreater(len(a.result_dicts_list), 1)
