import Parser
import Model
import main



# Search for drug pathwayed to Lepirudin and print overview
search_dict = {"name": 'Lepirudin Action Pathway'}


a = Parser.AdvancedSearch.AdvancedSearch(main.incremental_loader, search_dict, search_type=Parser.AdvancedSearch.SupportedProperties.PATHWAY)

print(a.result_dicts_list)
for elem in a.result_dicts_list:
    drug = Model.Drug.Drug(elem)
    print(drug.general_represent)  # overview