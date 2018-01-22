import xml.sax

class Drug(xml.sax.ContentHandler ):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.created = ""
        self.updated = ""
        self.id_primary = ""
        self.id = ""
        self.name = ""
        self.description = ""
        self.cas_number = ""
        self.unii = ""
        self.avg_mass = ""
        self.monoisotopic_mass = ""
        self.state = ""
        self.groups = ""
        self.articles = ""
        self.synthesis_reference = ""
        self.indication = ""
        self.pharmacodynamics = ""
        self.mechanism_of_action = ""
        self.toxicity = ""
        self.metabolism = ""
        self.absorption = ""
        self.half_life = ""
        self.protein_binding = ""
        self.route_of_elimination = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        # print(tag)
        # print("START#" * 10)
        if tag == 'drug':
            print("DRUG")
            for (k,v) in attributes.items():
                print (k + " " + v)

    def endElement(self, tag):
        if self.CurrentData == "name":
            print("name:", self.name)
        elif self.CurrentData == "description":
            print("description", self.description)
        elif self.CurrentData == "cas_number":
            print("cas_number", self.description)
        else:
            print("nic")
        # print("END#" * 10)

    def characters(self, content):
        if self.CurrentData == "name":
            self.name = content
        elif self.CurrentData == "description":
            self.name = content
        elif self.CurrentData == "cas_number":
            self.name = content

    # def __repr__(self):
    #     return "{}".format(self.id_primary)