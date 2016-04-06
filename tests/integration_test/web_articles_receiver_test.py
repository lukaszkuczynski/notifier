from input.web_element_receiver import WebElementReceiver
from unittest import TestCase
from mutate.mutator_factory import MutatorFactory


class WebElementReceiverTestI(TestCase):

    def test_receive(self):
        url = "http://www.domiporta.pl/sprzedam-dzialke-dolnoslaskie_sroda_slaska?LocalizationId=51620"
        params = {
            "input": {
                "url": url,
                "element": {
                    "parentPath":"div.WynikiLista div.NoweWyniki",
                    "keys": {
                        "title": ["div.Tytul a.TytulOgloszenia"],
                        "price": ["span.CenaTekst"],
                    }
                }
            }
        };
        w = WebElementReceiver(params)
        elements = w.receive()
        print("received %d elements"%(len(elements)))
        for e in elements: print(e)

    def test_receive_and_mutate(self):
        url = "http://www.domiporta.pl/sprzedam-dzialke-dolnoslaskie_sroda_slaska?LocalizationId=51620"
        params = {
            "input": {
                "url": url,
                "element": {
                    "parentPath":"div.WynikiLista div.NoweWyniki",
                    "keys": {
                        "title": ["div.Tytul a.TytulOgloszenia"],
                        "price": ["span.CenaTekst"],
                    }
                }
            },
            "mutate": {
                "key": {
                    "price" : "whitespace"
                }
            }
        };
        w = WebElementReceiver(params)
        elements = w.receive()
        mutator = MutatorFactory().get(params)
        mutated = mutator.mutate(elements)
        print("received %d elements"%(len(mutated)))
        for e in mutated: print(e)