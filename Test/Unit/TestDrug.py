import unittest
import Parser, Model
import main


class TestDrug(unittest.TestCase):

    def test(self):
        self.assertTrue(True)
        search_dict = {"name": 'Action Pathway', "category": "drug_action"}
        a = Parser.Search.Search(main.incremental_loader, search_dict)
        print(a.result_dicts_list)
        for elem in a.result_dicts_list:
            drug = Model.Drug.Drug(elem)
        self.assertTrue("Lepirudin" in drug.general_represent)