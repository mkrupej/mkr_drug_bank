import collections

import Parser.Drug
import Loader.Loader
import Model.Drug

#filename = './Source/minidrug2.xml'
filename = './Source/full database.xml'
#filename = './Source/single_drug.xml'

path = 'drug'
incremental_loader = Loader.Loader.load(filename, path)
search_dict = {"name": 'Patritumab'}


a = Parser.Drug.Drug(incremental_loader, search_dict)

print(a.result_dicts_list)
for elem in a.result_dicts_list:
    drug = Model.Drug.Drug(elem)
    print(drug.general_represent)
   # print(drug)
