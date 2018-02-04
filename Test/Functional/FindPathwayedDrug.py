import unittest
import Parser
import Model
import main


class FindPathwayedDrugTestCase(unittest.TestCase):
    """

    """


    def test_find_pathwayed_drug_by_empy_dict_error_case(self):
        search_dict = {}
        a = Parser.AdvancedSearch.AdvancedSearch(main.incremental_loader, search_dict, search_type=Parser.AdvancedSearch.SupportedFile.PATHWAY)
        self.assertLess(len(a.result_dicts_list), 1)


    def test_find_drug_by_pathway(self):
        search_dict = {"name": 'Lepirudin Action Pathway'}
        name = {"name" : "Lepirudin"}
        a = Parser.AdvancedSearch.AdvancedSearch(main.incremental_loader, search_dict, search_type=Parser.AdvancedSearch.SupportedFile.PATHWAY)
        match = False
        for elem in a.result_dicts_list:
            drug = Model.Drug.Drug(elem)
            print(drug.general_represent)
            if ((name["name"] in drug.general_represent)):
                match = True
        self.assertTrue(match)


    def test_find_drug_by_pathway_error_case(self):
        search_dict = {"name": 'non existing'}
        a = Parser.AdvancedSearch.AdvancedSearch(main.incremental_loader, search_dict, search_type=Parser.AdvancedSearch.SupportedFile.PATHWAY)
        self.assertLess(len(a.result_dicts_list), 1)


    def test_find_multiple_drugs_by_pathway(self):
        search_dict = {"name": 'Lepirudin Action Pathway'}
        a = Parser.AdvancedSearch.AdvancedSearch(main.incremental_loader, search_dict, search_type=Parser.AdvancedSearch.SupportedFile.PATHWAY)
        self.assertGreater(len(a.result_dicts_list), 1)


    def test_find_drug_by_multiple_pathway_properties_(self):
        search_dict = {"category": 'drug_action', "smpdb-id" : "SMP00278"}
        a = Parser.AdvancedSearch.AdvancedSearch(main.incremental_loader, search_dict, search_type=Parser.AdvancedSearch.SupportedFile.PATHWAY)
        for elem in a.result_dicts_list:
            drug = Model.Drug.Drug(elem)
            print(drug.general_represent)
        self.assertGreater(len(a.result_dicts_list), 1)