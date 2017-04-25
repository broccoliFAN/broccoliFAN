
#encoding=utf8
import os
import sys
#sys.path.extend([os.path.dirname(__file__)+'/../../'])
#print([os.path.dirname(__file__)+'/'])

from common.sendMail import SendMail
from common.checkHiveData import CheckHiveData
from campus_baitiao_base_weekly.gene_campus_baitiao_base_weekly_sql import gene_campus_baitiao_base_weekly_sql
from campus_baitiao_base_weekly.gene_campus_baitiao_base_weekly_html import gene_campus_baitiao_base_weekly_html
import time
import email

#基本数据路径配置
SQL_DIR = '/exportfs/home/yangsen7/online/crontab/data/campus_baitiao_base_weekly/sql/'
SQL_RESULT_DIR = '/exportfs/home/yangsen7/online/crontab/data/campus_baitiao_base_weekly/sql_result/'

def check_YMDdate(date):
    if len(date)!=8:
        return False
    y = date[0:4]
    m = date[4:6]
    d = date[6:8]
    if int(y)!=2016:
        return False
    if int(m)<1 or int(m)>12:
        return False
    if int(d)<1 or int(d)>31:
        return False
    return True

#检测输入参数
if len(sys.argv)<2:
    exit('请输入执行批量日期,格式 20160620')
#报表时间
YMDdate = sys.argv[1]
if not check_YMDdate(YMDdate):
    exit('输入的批量日期格式不正确,格式 20160620')

#检测时间格式
Y_M_Ddate="%s-%s-%s"%(YMDdate[0:4],YMDdate[4:6],YMDdate[6:8])


sql_result_path = '/exportfs/home/yangsen7/online/crontab/data/campus_baitiao_base_weekly/sql_result/campus_baitiao_base_weekly_20160623.sql.result'
weekly_html = gene_campus_baitiao_base_weekly_html(sql_result_path)
if not weekly_html:
    exit('无有效结果数据 %s' % sql_result_path)

#发送邮件
mail = SendMail(host='smtp.jd.com',port='25',username='yangsen7',password='Yangsen123~')
msg=email.mime.multipart.MIMEMultipart()
#msg['from']='yangsen7@jd.com'
msg['from']='yangsen7@jd.com'
#msg['to']='yangyi6@jd.com,cuiru@jd.com,caoshuo3@jd.com,yangsen7@jd.com'
msg['to']='yangsen7@jd.com'

#msg['cc'] = 'yangyi6@jd.com'
msg['subject']='校园白条基础报表'+YMDdate

html=email.mime.text.MIMEText(weekly_html, 'html', 'utf-8')
msg.attach(html)
#mail.send('yangsen7@jd.com',['yangyi6@jd.com','cuiru@jd.com','yangsen7@jd.com','caoshuo3@jd.com'],str(msg))
mail.send('yangsen7@jd.com',['yangsen7@jd.com'],str(msg))
"sendtest.py" [readonly] 63L, 2204C               