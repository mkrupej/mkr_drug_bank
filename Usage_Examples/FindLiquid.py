import Parser
import Model
import main



# Search for drug in liquid state and return dict. Print drug overview and details of each drug.
search_dict = {"state": 'liquid'}


a = Parser.Search.Search(main.incremental_loader, search_dict)

print(a.result_dicts_list)
for elem in a.result_dicts_list:
    drug = Model.Drug.Drug(elem)
    print(drug.general_represent)  # overview
    #print(drug)  # drug details