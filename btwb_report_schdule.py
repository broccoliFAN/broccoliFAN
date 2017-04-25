
        print('cf_dev.czw_btwb_report_all表不存在%s数据，等待数据到位。'%(Y_M_Ddate))
    else:
        print('cf_dev.czw_btwb_report_all ok')

    if not chd.check_table_data(Y_M_Ddate,'cf_dev.czw_btwb_report_qudao','dt'):
        flag_predata = False
        print('cf_dev.czw_btwb_report_qudao表不存在%s数据，等待数据到位。'%(Y_M_Ddate))
    else:
        print('cf_dev.czw_btwb_report_qudao ok')

    if not chd.check_table_data(Y_M_Ddate,'cf_dev.czw_btwaibu_shanfu_kaihushu','dt'):
        flag_predata = False
        print('cf_dev.czw_btwaibu_shanfu_kaihushu表不存在%s数据，等待数据到位。'%(Y_M_Ddate))
    else:
        print('cf_dev.czw_btwaibu_shanfu_kaihushu ok')

    if not chd.check_table_data(Y_M_Ddate,'cf_dev.czw_btwaibu_shanfu_boundchannel','dt'):
        flag_predata = False
        print('cf_dev.czw_btwaibu_shanfu_boundchannel表不存在%s数据，等待数据到位。'%(Y_M_Ddate))
    else:
        print('cf_dev.czw_btwaibu_shanfu_boundchannel ok')

    if not flag_predata:
        time.sleep(3600)
    else:
        break

if i==11 and flag_predata==False:
    exit('数据依赖不存在。需人工参与')

#执行日期脚本
sql_path = [
#       gene_sql_all(SQL_DIR, YMDdate, Y_M_Ddate),
        gene_sql_shanfu(SQL_DIR, YMDdate, Y_M_Ddate),
        gene_sql_wyzx(SQL_DIR, YMDdate, Y_M_Ddate),
        gene_sql_qudao_jdzhifu(SQL_DIR, YMDdate, Y_M_Ddate),
        gene_sql_qudao_qbshenghuo(SQL_DIR, YMDdate, Y_M_Ddate),
        gene_sql_qudao_qbfukuanma(SQL_DIR, YMDdate, Y_M_Ddate),
        gene_sql_qudao_qbsaoyisao(SQL_DIR, YMDdate, Y_M_Ddate)
        ]

sql_name = map(os.path.basename,sql_path)
sql_result_path = map(lambda x:SQL_RESULT_DIR+x+'.result',sql_name)

map(lambda x:os.system("/soft/hive/bin/hive -i /soft/hive/conf/hive.config -f %s > %s" % (x[0],x[1])),zip(sql_path,sql_result_path))

data_html = gene_html(sql_result_path)
#if not data_html:
#    exit('无有效结果数据 %s' % sql_result_path)

mail = SendMail()
msg=email.mime.multipart.MIMEMultipart()
msg['from']='cuizhiwei@jd.com'
msg['to']='guoxiaoinfo@jd.com,liufenfang@jd.com,huzhidan@jd.com,meiyu@jd.com,zhouchao1@jd.com,wangpengyuan@jd.com,zhangbing5@jd.com,renzhefeng@jd.com,hanxu8@jd.com,zhangxinyu9@jd.com,cuizhiwei@jd.com,caohong1@jd.com,jiangjingxiao@jd.com,machiyu@jd.com,yuwanqing@jd.com,jiayunxiao@jd.com'
msg['cc']='ouli@jd.com,chengjianbo@jd.com,bjlizhi@jd.com,wangjian1@jd.com,kongjiebin@jd.com,wangxinyu1@jd.com'

msg['subject']='白条外部支付交易监控日报-'+YMDdate
html=email.mime.text.MIMEText(data_html, 'html', 'utf-8')
msg.attach(html)
mail.send('cuizhiwei@jd.com',['guoxiaoinfo@jd.com','bjlizhi@jd.com','liufenfang@jd.com','huzhidan@jd.com','meiyu@jd.com','zhouchao1@jd.com','wangpengyuan@jd.com','zhangbing5@jd.com','renzhefeng@jd.com','hanxu8@jd.com','zhangxinyu9@jd.com','chengjianbo@jd.com','cuizhiwei@jd.com','caohong1@jd.com','jiangjingxiao@jd.com','machiyu@jd.com','ouli@jd.com','wangjian1@jd.com','kongjiebin@jd.com','wangxinyu1@jd.com','jiayunxiao@jd.com','yuwanqing@jd.com'],str(msg))
#mail.send('cuizhiwei@jd.com',['cuizhiwei@jd.com'],str(msg))
"btwb_report_schdule.py" [readonly] 115L, 4583C             