import Parser
import Model
import main



# Search for drugs targeted to Human and print overview
search_dict = {"organism": 'Human'}


a = Parser.AdvancedSearch.AdvancedSearch(main.incremental_loader, search_dict, search_type=Parser.AdvancedSearch.SupportedProperties.TARGET)

print(a.result_dicts_list)
for elem in a.result_dicts_list:
    drug = Model.Drug.Drug(elem)
    print(drug.general_represent)  # overview