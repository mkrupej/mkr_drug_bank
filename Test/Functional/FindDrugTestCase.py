import unittest
import Parser
import Model
import main


class FindDrugTestCase(unittest.TestCase):
    """
    Functional TestCases for Simple search using different set of properties.
    Search through indications included.
    """

    def test_find_drug_by_empy_dict_error_case(self):
        search_dict = {}
        a = Parser.Search.Search(main.incremental_loader, search_dict)
        self.assertLess(len(a.result_dicts_list), 1)


    def test_find_drug_by_name(self):
        search_dict = {"name": 'Lepirudin'}
        a = Parser.Search.Search(main.incremental_loader, search_dict)
        for elem in a.result_dicts_list:
            drug = Model.Drug.Drug(elem)
            print(drug.general_represent)
            self.assertTrue(search_dict["name"] in drug.general_represent)


    def test_find_drug_by_name_error_case(self):
        search_dict = {"name": 'notavailable'}
        a = Parser.Search.Search(main.incremental_loader, search_dict)
        self.assertLess(len(a.result_dicts_list), 1)


    def test_find_drug_by_property(self):
        search_dict = {"cas-number": '138068-37-8'}
        name_to_assert = "Lepirudin"
        a = Parser.Search.Search(main.incremental_loader, search_dict)
        for elem in a.result_dicts_list:
            drug = Model.Drug.Drug(elem)
            print(drug.general_represent)
            print("drugdict", drug.drug_dict)
            self.assertTrue(name_to_assert in drug.general_represent)
            self.assertTrue(search_dict["cas-number"] in drug.drug_dict["drug"]["cas-number"])


    def test_find_drug_by_property_error_case(self):
        search_dict = {"notexisting" : "notexisting"}
        a = Parser.Search.Search(main.incremental_loader, search_dict)
        self.assertLess(len(a.result_dicts_list), 1)


    def test_find_multiple_drugs_by_property(self):
        search_dict = {"state": 'liquid'}
        result = Parser.Search.Search(main.incremental_loader, search_dict)
        print(len(result.result_dicts_list))
        for elem in result.result_dicts_list:
            drug = Model.Drug.Drug(elem)
            #print(drug.general_represent)
            self.assertTrue("liquid" in drug.__repr__())
        print(len(result.result_dicts_list))
        self.assertGreater(len(result.result_dicts_list),1)


    def test_find_drug_by_multiple_properties(self):
        search_dict = {"cas-number": '138068-37-8', "state" : 'Liquid', "unii" : 'Y43GF64R34'}
        name_to_assert = "Lepirudin"
        a = Parser.Search.Search(main.incremental_loader, search_dict)
        for elem in a.result_dicts_list:
            drug = Model.Drug.Drug(elem)
            print(drug.general_represent)
            self.assertTrue(name_to_assert in drug.general_represent)


    def test_find_drug_by_multiple_properties_error_case(self):
        search_dict = {"cas-number": 'notexists', "state" : 'Liquid', "unii" : 'Y43GF64R34'}
        name_to_assert = "Lepirudin"
        a = Parser.Search.Search(main.incremental_loader, search_dict)
        self.assertLess(len(a.result_dicts_list), 1)


    def test_find_indicated_drugs(self):
        search_dict = {"indication": 'heparin'}
        name_to_assert = "Lepirudin"
        match = False
        a = Parser.Search.Search(main.incremental_loader, search_dict)
        for elem in a.result_dicts_list:
            drug = Model.Drug.Drug(elem)
            print(drug.general_represent)
            if (name_to_assert in drug.general_represent):
                match = True
        self.assertTrue(match)