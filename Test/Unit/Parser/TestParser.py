import unittest
import Parser
import Model
import main


class ParserTestCase(unittest.TestCase):
    """
    Parser UnitTests
    """

    def test_parser(self):
        search_dict = {}
        a = Parser.Search.Search(main.incremental_loader, search_dict)
        self.assertLess(len(a.result_dicts_list), 1)
    #
    #
    # def test_find_drug_by_name(self):
    #     search_dict = {"name": 'Lepirudin'}
    #     a = Parser.Search.Search(main.incremental_loader, search_dict)
    #     for elem in a.result_dicts_list:
    #         drug = Model.Drug.Drug(elem)
    #         print(drug.general_represent)
    #         self.assertTrue(search_dict["name"] in drug.general_represent)
    #
