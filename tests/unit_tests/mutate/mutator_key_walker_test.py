from unittest import TestCase, skip
from mutate.mutator_key_walker import MutatorKeyWalker

class TwoKeyObject:
        def __init__(self, key1, key2):
            self.key1 = key1
            self.key2 = key2

class MutatorKeyWalkerTest(TestCase):


    @skip('unskip when dict implemented')
    def apply_options_dict_test(self):

        options = {
            'mutate' : {
                'key' : {
                    'key1' : 'whitespace'
                }
            }
        }
        mutatorKeyWalker = MutatorKeyWalker(options)
        dict = {
            'key1' : 'aa bb',
            'key2' : 'aa bb cc'
        }
        mutated = mutatorKeyWalker.mutate(dict)

        self.assertEquals(mutated['key1'], 'aabb')

    def apply_options_object_test(self):
        options = {
            'mutate' : {
                'key' : {
                    'key1' : 'whitespace'
                }
            }
        }
        mutatorKeyWalker = MutatorKeyWalker(options)
        tko = TwoKeyObject('aa bb', 'aa cc')
        tko2 = TwoKeyObject(' aa    bb  2 ', 'aa cc2')
        tkos = [tko, tko2]
        mutated = mutatorKeyWalker.mutate(tkos)
        self.assertEquals(mutated[0].key1, 'aabb')
        self.assertEquals(mutated[0].key2, 'aa cc')
        self.assertEquals(mutated[1].key1, 'aabb2')
        self.assertEquals(mutated[1].key2, 'aa cc2')

    def when_empty_options_all_noop_test(self):
        options = {
        }
        mutatorKeyWalker = MutatorKeyWalker(options)
        tko = TwoKeyObject('aa bb', 'aa cc')
        tko2 = TwoKeyObject(' aa    bb  2 ', 'aa cc2')
        tkos = [tko, tko2]
        mutated = mutatorKeyWalker.mutate(tkos)
        self.assertEquals(mutated[0].key1, 'aa bb')
        self.assertEquals(mutated[0].key2, 'aa cc')
        self.assertEquals(mutated[1].key1, ' aa    bb  2 ')
        self.assertEquals(mutated[1].key2, 'aa cc2')
