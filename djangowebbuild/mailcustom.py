#!/usr/bin/python2.7
# coding=utf-8
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import Encoders
import re
import struct
import string
import binascii
from google.appengine.api import mail
import os
import datetime
from config.conf import *



def local_time(fmt="%Y-%m-%d %H:%M", tz=TIMEZONE):
    return (datetime.datetime.utcnow() + datetime.timedelta(hours=tz)).strftime(fmt)


def sendmail(sender, to, fullfilename):
    # sender = sender
    # to = 'kylinyau@gmail.com;975168367_81@kindle.cn;975168367@qq.com'
    lctime = local_time('%Y-%m-%d_%H-%M', TIMEZONE)
    # filename = 'abc.txt'
    with open(fullfilename, 'rb') as f:
        attbase64 = f.read()
    fileshortname = os.path.basename(fullfilename)
    mail.send_mail(sender, to, "kindle message {time}".format(time=lctime),
                   "Deliver from KindleEar {time}".format(time=lctime),
                   attachments=[(fileshortname, attbase64)])
