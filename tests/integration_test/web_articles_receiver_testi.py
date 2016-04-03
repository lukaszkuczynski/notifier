from input.webarticlesreceiver import WebArticlesReceiver
from unittest import TestCase, skip


class WebArticlesReceiverTestI(TestCase):

    @skip
    def test(self):
        url = "http://wiadomosci.wp.pl/?ticaid=1169c4&_ticrsn=3"
        article = "div#bxWiadPolska ul.wiadomosciLst li"
        titles = ["h2 a", "a"]
        contents = titles
        link = ""
        params = {
            "input": {
                "type": "web.element",
                "url": url,
                "article": {
                    "path":article,
                },
                "articleElement": {
                    "titles":titles,
                    "contents":contents,
                    "link":link,
                }
            }
        };

        w = WebArticlesReceiver(params)
        arts = w.receive()
        print("received %d elements"%(len(arts)))
        print(arts)