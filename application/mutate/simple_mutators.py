class MutatorNoop:

    def mutate(self, value):
        return value


class MutatorSpaceEliminator:

    def mutate(self, value):
        no_space = str(value).replace(" ","")
        return no_space.replace("\xa0","")
