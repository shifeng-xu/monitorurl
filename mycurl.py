# !/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import subprocess

def execurl(url,TIMEOUT):
    #res = os.popen('curl %s' % url)
    #res = os.popen('curl %s' % url).readlines()
    cmd='curl -sL -w "%{http_code},%{time_total}" '+url+' --connect-timeout  '+TIMEOUT+' -o /dev/null'
    #cmd='curl -sL -w "%{http_code}" '+url+' -o /dev/null'
    res = os.popen(cmd).readlines()
    #res=subprocess.call('curl %s' % url, shell=True)
    print(res)
    return res

