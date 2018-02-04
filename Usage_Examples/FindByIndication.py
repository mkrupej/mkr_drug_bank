import Parser
import Model
import main



# Search for drug indicated to bowel and print overview
search_dict = {"indication": 'bowel'}


a = Parser.Search.Search(main.incremental_loader, search_dict)

print(a.result_dicts_list)
for elem in a.result_dicts_list:
    drug = Model.Drug.Drug(elem)
    print(drug.general_represent)  # overview