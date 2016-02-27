'''
Created on 21 lut 2016

@author: luk
'''

import os, json
from datetime import datetime
import logging
import smtplib
from email.mime.text import MIMEText
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
        self.recipients = params['notifier']['recipients']

        
    def notify(self, diff):
        diffdump = json.dumps(diff)
        msg = MIMEText('sie pozmienialo ' + diffdump)
        
        env_config = config.config()
        mail_config = env_config['mail'] 
        # me == the sender's email address
        # you == the recipient's email address
        msg['Subject'] = mail_config['subject']
        me = mail_config['from']
        msg['From'] = me
        s = smtplib.SMTP(mail_config['server']['name'])        
        user = mail_config['server']['user']
        password = mail_config['server']['password']
        if not user and not password :
            logger.debug('no log in')
        else :
            logger.debug('logging in to smtp')
            s.login(user, password)        
        msg['To'] = ",".join(self.recipients)        
        s.sendmail(me, self.recipients, msg.as_string())
#         for recipient in self.recipients :
#             msg['To'] = recipient        
#             s.sendmail(me, [recipient], msg.as_string())
        s.quit()        
        

if __name__ == '__main__' :
    recipients = config.config()['mail']['default_recipients'] 
        
    params = {
              'notifier' : {
                'recipients' : recipients 
            }
    }
    n = MailNotifier(params)
    diff = 'diff'
    n.notify(diff)
    
