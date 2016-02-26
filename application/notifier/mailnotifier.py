'''
Created on 21 lut 2016

@author: luk
'''

import os, json
from datetime import datetime
import logging
import smtplib
from email.mime.text import MIMEText


FORMAT = '%(asctime)-24s %(levelname)-8s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger('MailNotifier')



class MailNotifier():
    '''
    classdocs
    '''

    def __init__(self, params=None):
        logger.debug('init notifier, params %s', params)
        self.server = params['notifier']['server']
        
    def notify(self, diff):
        msg = MIMEText('tekst')
        
        config = json.load(open('config.json', 'r'))
        mail_config = config['mail'] 
        
        # me == the sender's email address
        # you == the recipient's email address
        msg['Subject'] = mail_config['subject']
        me = mail_config['from']
        you = mail_config['to']
        msg['From'] = me
        msg['To'] = you
        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP(mail_config['server']['name'])
        user = mail_config['server']['user']
        password = mail_config['server']['password']
        s.login(user, password)
        s.sendmail(me, [you], msg.as_string())
        s.quit()        
        pass
        

if __name__ == '__main__' :
    params = {
              'notifier' : {
                'server' : 1
            }
    }
    n = MailNotifier(params)
    diff = 'diff'
    n.notify(diff)
    
