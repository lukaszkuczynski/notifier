'''
Created on 21 lut 2016

@author: luk
'''

import os, json
from datetime import datetime
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import email.charset
from jinja2 import Environment, FileSystemLoader
from config import config
FORMAT = '%(asctime)-24s %(levelname)-8s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger('MailNotifier')



class MailNotifier():
    '''
    classdocs
    '''

    def __init__(self, params=None):
        logger.debug('init notifier, params %s', params)
        if params != None and 'notifier' in params.keys() :
            self.recipients = params['notifier']['recipients']
            self.template = params['notifier']['template']
        else:
            logger.warn('params seems to be empty')

        
    def notify(self, diff):
        env_config = config.config()
        mail_config = env_config['mail']

        msg = self.build_msg_html(diff, mail_config, template_filename=self.template)

        s = smtplib.SMTP_SSL(mail_config['server']['name'])
        user = mail_config['server']['user']
        password = mail_config['server']['password']
        if not user and not password :
            logger.debug('no log in')
        else :
            logger.debug('logging in to smtp')
            s.login(user, password)        
        s.sendmail(msg['From'], self.recipients, msg.as_string())
        s.quit()


    def build_msg_html(self, diff, mail_config, template_filename):

        msg = MIMEMultipart("alternative")
        msg['Subject'] = mail_config['subject']
        msg['From'] = mail_config['from']
        msg['To'] = ",".join(self.recipients)

        template_folder = os.path.dirname(template_filename)
        template_file = os.path.basename(template_filename)

        env = Environment(loader=FileSystemLoader(template_folder))
        template = env.get_template(template_file)
        rendered_html = template.render(diff=diff.all_changes())
        part_html = MIMEText(rendered_html, "html", "utf-8")

        msg.attach(part_html)

        return msg


