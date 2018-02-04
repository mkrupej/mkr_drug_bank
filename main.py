import Parser.AdvancedSearch
import Loader.Loader
import Model.Drug


#set DB file
#filename = './Source/minidrug2.xml'
db_file = 'C:/Users/michal/PycharmProjects/mkr_drug_bank/Source/full database.xml'
#filename = './Source/single_drug.xml'

drug_xml_selector = 'drug'
incremental_loader = Loader.Loader.load(db_file, drug_xml_selector)
print(type(incremental_loader))
print(next(incremental_loader))
# search_dict = {"name": 'Action Pathway', "category" : "drug_action"}

#
# a = Parser.Drug.Drug(incremental_loader, search_dict)
#
# print(a.result_dicts_list)
# for elem in a.result_dicts_list:
#     drug = Model.Drug.Drug(elem)
#     print(drug.general_represent)
#     print(drug)

# b = Parser.AdvancedSearch.AdvancedSearch(incremental_loader, search_dict, search_type=Parser.AdvancedSearch.SupportedFile.PATHWAY)
# #
# print(b.result_dicts_list)
#
# for elem in b.result_dicts_list:
#      drug = Model.Drug.Drug(elem)
#      print(drug.general_represent)
#      print(len(b.result_dicts_list))
#      #print(drug)