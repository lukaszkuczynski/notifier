from mutate.simple_mutators import MutatorNoop, MutatorSpaceEliminator
from unittest import TestCase

class MutatorsTest(TestCase):

    def noop_return_thesame_test(self):
        mutator = MutatorNoop()
        val = mutator.mutate(1)
        self.assertEquals(val, 1)

    def eliminator_trims_text_test(self):
        mutator = MutatorSpaceEliminator()
        val = mutator.mutate(" aa   bb ")
        self.assertEquals(val, "aabb")

    def eliminator_trims_unicode_space_text_test(self):
        mutator = MutatorSpaceEliminator()
        val = mutator.mutate(" aa \xa0  bb ")
        self.assertEquals(val, "aabb")

