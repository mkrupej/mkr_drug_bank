#initial commit
import Parser.Drug
import Loader
import locale
#locale.getdefaultlocale = (lambda *args: ['en_US', 'utf8'])
#locale.getlocale = (lambda *args: ['en_US', 'utf8'])
#parsed_db = Loader.DatabaseLoader.get_db()
filename = './Source/minidrug.xml'
#filename = './Source/full database.xml'
path = 'drug'
incremental_loader = Loader.Loader.load(filename, path)
#print(type(incremental_loader))
#print(len(list(incremental_loader)))
#print(list(next(incremental_loader)))
# print(a.result_dict)

a = Parser.Drug.DrugParser('Bivalirudin', incremental_loader)
#print(a.result_dict)