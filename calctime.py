# coding=UTF-8
import myemail
import datetime
import time
from myemail import read_file_as_str



while True:
    # 获取现在时间
    now_time = datetime.datetime.now()
    now_day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    now_hour = now_time.hour
    now_min = now_time.minute
    now_sec = now_time.second
    # 0点到1点之间不刷新
    if (now_hour >= 23 and now_min >= 50 or True):
        costDict={} #求和
        countDict={} #计数
        avgDict={}#平均
        # 读配置文件方法二
        f2 = open("./config.ini", "r")
        lines = f2.readlines()
        for linein in lines:
            if ('=' in linein):
                tmp = linein.replace('\n', '').split('=')
                if (tmp[0] == 'interval'):
                    WAITTIME = int(tmp[1])
                if (tmp[0] == 'timeout'):
                    TIMEOUT = tmp[1]
                if (tmp[0] == 'ReceiverList'):
                    receiverList_ini = tmp[1]
                    receivers = receiverList_ini.split(',')
                if (tmp[0] == 'UrlList'):
                    urlList_ini = tmp[1]
                    urlList = urlList_ini.split(',')
        #初始化时间字典
        for url in urlList:
            costDict[url]=0
            countDict[url]=0
            avgDict[url]=0
        timelog='./log/'+now_day+'.log'
        ftimelog=open(timelog,"r")
        lineslog = ftimelog.readlines()
        for linelog in lineslog:
            result=linelog.replace('\n', '').split(',')
            reUrl=result[0]
            strReTime=result[1]
            if(strReTime=="FAIL"):
                continue
            flReTime=float(strReTime)
            costDict[reUrl]+=flReTime
            countDict[reUrl]+=1

        for (key,value) in costDict.items():
            count=countDict[key]
            sumtime=value
            avgDict[key]=sumtime/count if count!=0 else 0


        tableBody=""
        for (key,value) in avgDict.items():
            avgtime=value
            row='''<tr>
                      <td>{0}</td>
                      <td>{1}</td>
                      <td>{2}</td>
                    </tr>'''.format(key,countDict[key],avgDict[key])
            row=row+'</br>'
            tableBody+=row

        htmlmd = read_file_as_str('./module.html')
        sendmsg=htmlmd.format(now_day,tableBody)

        myemail.sendMail_no_img(sendmsg, "【内容站】{0} 响应时间统计", sendmsg)








