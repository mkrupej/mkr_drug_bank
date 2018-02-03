import collections

import Parser.Search
import Parser.AdvancedSearch
import Loader.Loader
import Model.Drug

#filename = './Source/minidrug2.xml'
#filename = './Source/full database.xml'
filename = './Source/single_drug.xml'

path = 'drug'
incremental_loader = Loader.Loader.load(filename, path)
search_dict = {"name": 'Action Pathway'}

#
# a = Parser.Drug.Drug(incremental_loader, search_dict)
#
# print(a.result_dicts_list)
# for elem in a.result_dicts_list:
#     drug = Model.Drug.Drug(elem)
#     print(drug.general_represent)
#     print(drug)

b = Parser.AdvancedSearch.AdvancedSearch(incremental_loader, search_dict, search_type=Parser.AdvancedSearch.SupportedFile.PATHWAY)
#
print(b.result_dicts_list)

for elem in b.result_dicts_list:
     drug = Model.Drug.Drug(elem)
     print(drug.general_represent)
     print(len(b.result_dicts_list))
     #print(drug)