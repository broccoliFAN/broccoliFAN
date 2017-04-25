select '累计',
       b.tot_person,
       0,
       b.tot_order,
       b.tot_amt,
       b.tot_average,
       case when b.tot_person=0 then 0 else b.tot_amt/b.tot_person end,
       case when b.tot_person=0 then 0 else b.tot_order/b.tot_person end,
       b.tot_merchant,
       0
  from (select dt,qudao_id,tot_person,tot_order,tot_amt,tot_average,tot_merchant
          from cf_dev.czw_btwb_report_qudao
         where dt='%s'
           and qudao_id=1) b;
"""
    #YMDdate_minut_7 = time.strftime('%Y%m%d',time.localtime(time.mktime(time.strptime(YMDdate,"%Y%m%d")) - 7*24*60*60))
    sql = sql % (Y_M_Ddate,Y_M_Ddate,Y_M_Ddate)

    file_name = YMDdate+'.sql'
    file_path = dir_path + 'btwb_report_qudao_jdzhifu' + file_name
    with open(file_path,'w') as f:
        f.write(sql)

    return file_path


def gene_sql_qudao_qbsaoyisao(dir_path, YMDdate, Y_M_Ddate):

    sql="""
use cf_dev;
use cf_dev;
select a.today,
       a.day_person,
       a.tot_person_new_2,
       a.day_order,
       a.day_amt,
       a.day_average,
       case when a.day_person=0 then 0 else a.day_amt/a.day_person end,
       case when a.day_person=0 then 0 else a.day_order/a.day_person end,
       a.day_merchant,
       a.tot_merchant_new_2
  from (select dt,qudao_id,today,day_person,day_order,day_amt,day_average,day_merchant
              ,(case when tot_person_new is not null then tot_person_new else 0 end) as tot_person_new_2
              ,(case when tot_merchant_new is not null then tot_merchant_new else 0 end) as tot_merchant_new_2
          from cf_dev.czw_btwb_report_qudao
         where dt<='%s'
           and dt>=date_sub('%s',6)
           and dt>='2016-10-17'
           and qudao_id=4
        order by dt desc,qudao_id asc
        limit 7) a
union
select '累计',
       b.tot_person,
       0,
       b.tot_order,
       b.tot_amt,
       b.tot_average,
       case when b.tot_person=0 then 0 else b.tot_amt/b.tot_person end,
       case when b.tot_person=0 then 0 else b.tot_order/b.tot_person end,
       b.tot_merchant,
       0
  from (select dt,qudao_id,tot_person,tot_order,tot_amt,tot_average,tot_merchant
"gene_sql.py" [readonly] 441L, 14473C                                            