# coding=UTF-8
import myemail
import requrl
import mycurl
import datetime
import time

#from configparser import ConfigParser


#requrl.getUrl("http://beautycareapp.com/")


#curl -I -m 10 -o /dev/null -s -w http://beautycareapp.com

#res=mycurl.execurl("http://beautycareapp.com.cn/")
#刷新间隔（vi秒）
WAITTIME=600
#curl判断超时时间
TIMEOUT=30

urlList=[
    'beautycareapp.com',
    'fundideas4u.com',
    'mobilecarvehicle.com',
    'oursneaker.com',
    'playerforyou.com',
    'diy-meal.com',
    'movie-ninjia.com',
    'dozodiac.com',
    'triviaist.com',
    'novelsyousetu.com',
]
receivers = ["xushifeng@do-global.com"]
#receivers = ["lixingxing@do-global.com","xushifeng@do-global.com","haoyinpeng@do-global.com","mishuai@do-global.com","chenfeifan@do-global.com","lufei@do-global.com","nieminglu@do-global.com","zhangtingting@do-global.com"]


while True:
    #读取配置文件方法一
    # conf = ConfigParser()
    # conf.read("config.ini")
    # # url超时时间，
    # TIMEOUT = conf.get("Time", "timeout")
    # WAITTIME = conf.getint("Time", "interval")
    # receiverList_ini = conf.get("Receiver", "ReceiverList")
    # urlList_ini = conf.get("TestUrl", "UrlList")
    # urlList=urlList_ini.split(',')
    # receivers=receiverList_ini.split(',')

    #读配置文件方法二
    f2 = open("./config.ini", "r")
    lines = f2.readlines()
    for linein in lines:
        if('=' in linein):
            tmp=linein.replace('\n', '').split('=')
            if(tmp[0]=='interval'):
                WAITTIME = int(tmp[1])
            if (tmp[0] == 'timeout'):
                TIMEOUT = tmp[1]
            if (tmp[0] == 'ReceiverList'):
                receiverList_ini = tmp[1]
                receivers = receiverList_ini.split(',')
            if (tmp[0] == 'UrlList'):
                urlList_ini = tmp[1]
                urlList = urlList_ini.split(',')
    #创建响应时间字典，key=url，value=time

    # 获取现在时间
    now_time = datetime.datetime.now()
    now_day=time.strftime('%Y-%m-%d', time.localtime(time.time()))
    now_hour=now_time.hour
    now_min=now_time.minute
    now_sec=now_time.second
    #0点到1点之间不刷新
    if(now_hour>=0 and now_hour<=1):
        time.sleep(WAITTIME)
        continue
    for url in urlList:
        res=mycurl.execurl(url,TIMEOUT)
        res_list=res[0].split(',')
        code=res_list[0] #返回码
        str_costtime=res_list[1]  #耗时
        costtime=float(str_costtime)*1000
        costtime=round(costtime,3)
        timestr=""
        if code=="200":
            msg="正常响应："+str(now_time)+"\n"
            msg+="正常URL："+url+"\n"
            timestr +=url+","+str(costtime)+"\n"
        else:
            msg="告警时间："+str(now_time)+",\n"
            msg+="告警URL："+url+",\n"
            msg+="HTTP状态码："+res[0]+",\n"
            timestr += url + ",FAIL\n"
            if(res[0]=="000"):
                msg += "告警原因：超时或链接不存在！\n"
            myemail.sendMail_no_img(receivers,"【内容站】HTTP告警",msg)

        fileTime = './log/' + now_day + '.log'
        with open(fileTime, mode='a') as filename2:
            filename2.write(timestr)

        file = 'myurl.log'
        with open(file, mode='a') as filename:
            filename.write(msg)
            filename.write('\n')  # 换行

    time.sleep(WAITTIME)
