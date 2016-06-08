#!/usr/bin/python
# coding=utf-8
import datetime

from django.http import HttpResponse
from config.conf import *
import mailcustom
import os
from django.shortcuts import render_to_response
from settings import *


def tiebaform(request):
    showinfo = False
    if 'tiebaId' in request.GET and 'kindleAddress' in request.GET and 'fileshortname' in request.GET:
        tiebaId = request.GET['tiebaId']
        fileshortname = request.GET['fileshortname']
        kindleAddress = request.GET['kindleAddress']
        if (tiebaId and kindleAddress and fileshortname):
            fullfilename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "file2send", fileshortname)
            mailcustom.sendmail(HOSTMAIL, kindleAddress, fullfilename)
            showinfo = True
            return render_to_response("tieba.html", {'showinfo': showinfo, 'fileshortname': fileshortname,
                                                     'kindleAddress': kindleAddress})
    else:
        pass
    return render_to_response("tieba.html")


def search(request):
    # 目的：把用户提交的数据进行校验，并且将邮件发送出去
    if 'tiebaId' in request.GET:
        message = 'You searched for: %r' % request.GET['tiebaId']
    else:
        message = 'You submitted an empty form.'

    return HttpResponse(message)


def mail(request):
    print TEMPLATE_DIRS
    to = "kylinyau@gmail.com;975168367_81@kindle.cn;975168367@qq.com"
    fileshortname = "naruto__276.mobi"
    fullfilename = os.path.join(os.path.dirname(os.path.relpath(__file__)), "file2send", fileshortname)
    # mailtest.sendmail(HOSTMAIL, to, fullfilename)
    html = "<html><body>{result}</body></html>".format(result=TEMPLATE_DIRS)
    return HttpResponse(html)
