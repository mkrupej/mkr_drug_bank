# Drug Bank - implementacja wyszukarki dla lokalnej kopii bazy leków


Celem projektu jest stworzenie wyszukiwarki dla lokalnej kopii bazy leków (https://www.drugbank.ca/).
Parametry wyszukiwania wzorowane zostay na wyszukiwarce on-line.

Wyszukiwarka umozliwia znajdowanie lekow po wybranych wlasciwosciach danego leku, jak rowniez pozwala na znalezienie leku powiazanego z okreslonym TARGET lub PATHWAY.

Instrukcja uzycia

1. Ustaw bezwzgledna sciezke do bazy danych w zmiennej db_file w main
2. Ustaw kryteria wyszukiwania w zmiennej search_dict w formie {"wlasnosc": "wartosc", ...}
3. Ustaw rodzaj wyszukiwania. Dostepne sa nastepujace mozliwosci:
+ Wyszukiwanie po wybranej wlasciwosci / wlasciwosciach. Ustaw nastepujace parametry wyszukiwania
```
a = Parser.Search.Search(incremental_loader, search_dict)
```
+ Wyszukiwanie zaawansowane zwracajace leki dla okreslonego PATHWAY
```
a = Parser.AdvancedSearch.AdvancedSearch(incremental_loader, search_dict, search_type=Parser.AdvancedSearch.SupportedProperties.PATHWAY)
```
+ Wyszukiwanie zaawansowane zwracajace leki dla okreslonego TARGET
```
a = Parser.AdvancedSearch.AdvancedSearch(incremental_loader, search_dict, search_type=Parser.AdvancedSearch.SupportedProperties.TARGET)
```

Rezultaty zwracane sa w postaci listy OrderedDictow, gdzie kazdy lek stanowi osobny OrderedDict.
Lista dictow przechowywana jest w 
```
a.result_dicts_list
``` 
Wyniki mozna wypisac w nastepujacy sposob:
```
for elem in a.result_dicts_list:
    drug = Model.Drug.Drug(elem)
    print(drug.general_represent)  # wypisywanie overview - nazwy, description i ID leku
    print(drug) # wypisywanie wszystkich wlasnosci leku
``` 

Przyklady uzycia zostaly zamieszczone w katalogu Usage_Examples

```
FindLepirudin - znajdz lek o znazwie Lepirudin. Wypisz jego overview i szczegoly

FindByDescriptionAndMetabolism - znajdz leki o dwoch wlasciwosciach, description = histamine i metabolism = Hepatic. Wypisz overview

FindLiquid - znajdz wszystkie leki ktorych state = liquid. Wypisz overview

FindByIndication - znajdz leki ktore maja okreslone indication = bowel. Wypisz overview

FindByPathway - znajdz leki zawierajace pathway o nazwie = epirudin Action Pathway. Wypisz overview 

FindByTarget - znajdz leki zawierajace target o nazwie = human. Wypisz overview

```
