import Parser.AdvancedSearch
import Loader.Loader
import Model.Drug


db_file = 'C:/full database.xml' #set absoulte path to DB file

drug_xml_selector = 'drug'
incremental_loader = Loader.Loader.load(db_file, drug_xml_selector) #set loader

#SIMPLE
# search_dict = {"name": 'Lepirudin'} #set search criteria {"property_name": "value"}
#
#
# a = Parser.Search.Search(incremental_loader, search_dict)
#
# print(a.result_dicts_list)
# for elem in a.result_dicts_list:
#     drug = Model.Drug.Drug(elem)
#     print(drug.general_represent)
#     print(drug)

#ADVANCED
#search_dict = {"name": 'Action Pathway', "category" : "drug_action"} #set search criteria {"property_name": "value"}

# b = Parser.AdvancedSearch.AdvancedSearch(incremental_loader, search_dict, search_type=Parser.AdvancedSearch.SupportedFile.PATHWAY)
# #
# print(b.result_dicts_list)
#
# for elem in b.result_dicts_list:
#      drug = Model.Drug.Drug(elem)
#      print(drug.general_represent)
#      print(len(b.result_dicts_list))
#      #print(drug)