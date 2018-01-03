class Drug:
    def __init__(self, id_primary, id, name, description,
                 cas_number, unii, avg_mass, monoisotopic_mass, state, groups, articles):
        self.id_primary = id_primary
        self.id = id
        self.name = name
        self.description = description
        self.cas_number = cas_number
        self.unii = unii
        self.avg_mass = avg_mass
        self.monoisotopic_mass = monoisotopic_mass
        self.state = state
        self.groups = groups
        self.articles = articles
        self.synthesis_reference = synthesis_reference
        self.indication = indication
        self.pharmacodynamics = pharmacodynamics
        self.mechanism_of_action = mechanism_of_action
        self.toxicity = toxicity
        self.metabolism = metabolism
        self.absorption = absorption
        self.half_life = half_life
        self.protein_binding = protein_binding
        self.route_of_elimination = route_of_elimination

    def __repr__(self):
        return "{}".format(self.id_primary)