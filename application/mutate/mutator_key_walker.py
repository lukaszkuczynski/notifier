from mutate.simple_mutators import MutatorNoop, MutatorSpaceEliminator
from copy import deepcopy

class MutatorKeyWalker:

    def __init__(self, options):
        self.mutators = {}
        if 'mutate' in options:
            if 'key' in options['mutate']:
                self.mutators = options['mutate']['key']

    def mutator_by_text(self, text):
        if text == 'whitespace' : return MutatorSpaceEliminator()
        return MutatorNoop()

    ## do the yielding staff
    # def mutate_superb(self, value):
    #     if isinstance(value, (list, tuple)) :
    #         newlist = []
    #         for k in value:
    #             newlist.append(self.mutate(k))
    #             return newlist
    #     if isinstance(value, dict):
    #         raise Exception('NYI for dict')
    #     if isinstance(value, type):
    #         for n in value.__dict__:
    #             mutator = self.mutator_by_text(self.mutators[n])
    #             if not mutator is None:
    #                 yield mutator.mutate(value.__dict__[n])
        # self.mutators

    def mutate_single_object(self, value):
        if isinstance(value, dict):
            raise Exception('NYI for dict')
        # if isinstance(value, type):
        mutated_object = deepcopy(value)
        for k,v in value.__dict__.items():
            # no mutator found, nothing to do
            if not k in self.mutators.keys(): continue
            mutator = self.mutator_by_text(self.mutators[k])
            mutated_object.__dict__[k] = mutator.mutate(value=v)
        return mutated_object

    def mutate(self, list):
        new_list = []
        for element in list :
           new_list.append(self.mutate_single_object(element))
        return new_list