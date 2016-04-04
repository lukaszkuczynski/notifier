from input.web_element_receiver import WebElementReceiver
from unittest import TestCase


class WebElementReceiverTestI(TestCase):

    def test(self):
        # url = "http://wiadomosci.wp.pl/?ticaid=1169c4&_ticrsn=3"
        # params = {
        #     "input": {
        #         "url": url,
        #         "element": {
        #             "parentPath":"div#bxWiadPolska ul.wiadomosciLst li",
        #             "keys": {
        #                 "title": ["h2 a", "a"],
        #                 "content": ["h2 a", "a"],
        #             }
        #         }
        #     }
        # };
        url = "http://www.domiporta.pl/sprzedam-dzialke-dolnoslaskie_sroda_slaska"
        # url = "http://wiadomosci.wp.pl/?ticaid=1169c4&_ticrsn=3"
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