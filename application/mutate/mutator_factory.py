from mutate.mutator_key_walker import MutatorKeyWalker
from mutate.simple_mutators import MutatorNoop

class MutatorFactory:

    def get(self, params):
        if 'mutate' in params:
            if 'key' in params['mutate']:
                return MutatorKeyWalker(params)
        return MutatorNoop()