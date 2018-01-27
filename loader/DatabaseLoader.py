from io import StringIO
from lxml import etree
from lxml.etree import tostring

def get_db(filepath=""):
    #root = etree.Element("../main/full database.xml")

    #file = open('../main/full database.xml', 'r', encoding='utf-8')
    file = open('../main/minidrug.xml', 'r', encoding='utf-8')
    xml = file.read()
    file.close()

    db = etree.XML(xml)
    find_text = etree.XPath("//drug[name ='Rasburicase']")
    text = find_text(db)
    return db
