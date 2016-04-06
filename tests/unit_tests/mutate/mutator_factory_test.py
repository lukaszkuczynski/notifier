from unittest import TestCase
from mutate.simple_mutators import MutatorNoop
from mutate.mutator_key_walker import MutatorKeyWalker
from mutate.mutator_factory import MutatorFactory


class MutatorFactoryTest(TestCase):

    def when_no_options_return_noop_test(self):
        options = {
        }
        factory = MutatorFactory()
        mutator = factory.get(options)
        self.assertTrue(isinstance(mutator, MutatorNoop))

    def when_key_in_options_return_keywalker_test(self):
        options = {
            'mutate' : {
                'key' : {
                    'key1' : 'whitespace'
                }
            }
        }
        factory = MutatorFactory()
        mutator = factory.get(options)
        self.assertTrue(isinstance(mutator, MutatorKeyWalker))