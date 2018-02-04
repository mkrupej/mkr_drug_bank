import Parser
import Model
import main

search_dict = {"name": 'Lepirudin'}


a = Parser.Search.Search(main.incremental_loader, search_dict)

print(a.result_dicts_list)
for elem in a.result_dicts_list:
    drug = Model.Drug.Drug(elem)
    print(drug.general_represent)
    print(drug)