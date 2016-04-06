#!/usr/bin/python
#  -*- coding: utf-8 -*-

from unittest import TestCase
from application.config import config
from application.notifier.mailnotifier import MailNotifier
from tests.integration_test.test_utils.test_objects_provider import TestProvider


class MailNotifierTestI(TestCase):

    def test_sendmail(self):

        recipients = config.config()['mail']['default_recipients']

        params = {
                  'notifier' : {
                    'recipients' : recipients,
                    'template' : "d://prj//notifier//mail_templates//articles.html"
                }
        }
        n = MailNotifier(params)

        diff = TestProvider.get_articles_diff(('łasdasdł','ZażółćGęśląJaźń'))
        n.notify(diff)
