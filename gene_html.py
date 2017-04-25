th {
    font: bold 14px 'SimSun';
    width: 120px;
    border-right: 1px solid #C1DAD7;
    border-left: 1px solid #C1DAD7;
    border-bottom: 1px solid #C1DAD7;
    border-top: 1px solid #C1DAD7;
    letter-spacing: 2px;
    text-transform: uppercase;
    text-align: left;
    padding: 6px 6px 6px 12px;
    background: #CAE8EA  no-repeat;
    font-weight: bold;
}
td {
    font: 14px 'Microsoft YaHei';
    border: 1px solid #C1DAD7;
    background: #fff;
    font-size:12px;
    padding: 6px 6px 6px 12px;
}
.title {
    font: bold 18.5px 'SimSun';
}
.title2 {
    font: bold 16px 'SimSun';
}
</style>

    """

#    html += '''<br /> <font styple="font-family: 'Microsoft YaHei'" size="5">1.京东支付&钱包接入白条支付交易及风险情况日报</font>'''
#    html += report_all_html

    html += '''<br /><br /> <div class='title'>1.闪付渠道交易日报</div>'''
    html += report_shanfu_html

    html += '''<br /><br /> <span><span class='title'>2.网银在线数据汇总</span><span class='title2'>（京东支付、钱包生活、钱包付款码、钱包扫一扫）</span>'''
#    html += '''<div class='title2'>（京东支付、钱包生活、钱包付款码、钱包扫一扫）</div>'''
    html += report_wyzx_html

    html += '''<br /><br /> <div class='title'>2.1京东支付渠道交易日报</div>'''
    html += report_jdzhifu_html

    html += '''<br /><br /> <div class='title'>2.2钱包生活渠道交易日报</div>'''
    html += report_qbshenghuo_html

    html += '''<br /><br /> <div class='title'>2.3钱包付款码渠道交易日报</div>'''
    html += report_qbfukuanma_html

    html += '''<br /><br /> <div class='title'>2.4钱包扫一扫渠道交易日报</div>'''
    html += report_qbsaoyisao_html


    html +='''<br/><br/><p><font style="font-family: 'Microsoft YaHei'">robot.</font><p>
    <br/>'''
    html += "</body></html>"

    return html

if __name__ == '__main__':
    print(gene_html('/exportfs/home/yangsen7/online/crontab/data/campus_stcd_reject_dist/sql_result/campus_stcd_reject_dist_20160807.sql.result'))