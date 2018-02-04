import unittest
import Parser
import Model
import main


class FindPathwayedDrugTestCase(unittest.TestCase):


    def test_find_drug_by_empy_dict_error_case(self):
        search_dict = {}
        a = Parser.Search.Search(main.incremental_loader, search_dict)
        self.assertLess(len(a.result_dicts_list), 10)
