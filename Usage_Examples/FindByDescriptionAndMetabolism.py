import Parser
import Model
import main



# Search for drug related to histamine and with hepatic metabolism and print drug overview
search_dict = {"metabolism": 'Hepatic', "description": "histamine"}


a = Parser.Search.Search(main.incremental_loader, search_dict)

print(a.result_dicts_list)
for elem in a.result_dicts_list:
    drug = Model.Drug.Drug(elem)
    print(drug.general_represent)  # overview