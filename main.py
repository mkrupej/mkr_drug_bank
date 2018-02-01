import Parser.Drug
import Loader.Loader
import Model.Drug

#filename = './Source/minidrug2.xml'
filename = './Source/full database.xml'
path = 'drug'
incremental_loader = Loader.Loader.load(filename, path)
search_dict = {"name": 'Lepirudin'}


#search2(incremental_loader, search_dict)

a = Parser.Drug.Drug(incremental_loader, search_dict)
#print(type(a.result_dicts_list[0]))
#print(a.result_dicts_list)

drug = Model.Drug.Drug(a.result_dicts_list[0])
print(drug.general_represent)