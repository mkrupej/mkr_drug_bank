import Parser.Drug


class Target(Parser.Drug.Drug):

    def search_elem(self, generated_elem, search_dict):
        match = False
        result = generated_elem.findall("targets")
        for elem in result:
            target = elem.findall("target")
            for target_elem in target:
                target_result = super(Target, self).search_elem(target_elem, search_dict)
                if target_result:
                    match = True
        return match
