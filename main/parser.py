import collections as collections
import xml.sax
import xml.etree.ElementTree as ET
from model import drug


# create an XMLReader
parser = xml.sax.make_parser()
# turn off namepsaces
#parser.setFeature(xml.sax.handler.feature_namespaces, 0)

# override the default ContextHandler
#Handler = drug.Drug()
parser.setContentHandler(drug.Drug())

parser.parse(open('full database.xml', "r", encoding="utf8"))
