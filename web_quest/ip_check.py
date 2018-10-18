# -*- coding:gbk -*-

import requests
import pandas as pd

xygj_df=pd.read_excel('/Users/andpay/Documents/job/data/question/信用管家交易失败.xlsx','all_data')

ip_list=xygj_df['ip'].unique()


def checkip(ip):
    URL = "http://ip.taobao.com/service/getIpInfo.php?ip="+ip
    try:
        r = requests.get(URL,timeout=10)
    except requests.RequestException as e:
        print(e)
    else:
        json_data = r.json()
        area_data=json_data['data']
        province=area_data['region']
        city=area_data['city']
        isp=area_data['isp']

        return province,city,isp


for ip in ip_list:
    province,city,isp=checkip(ip)
    ip_city=province+city
    xygj_df.loc[xygj_df['ip']==ip,'ip_city']=ip_city
    xygj_df.loc[xygj_df['ip']==ip,'isp']=isp


print(xygj_df)
excel_writer=pd.ExcelWriter('/Users/andpay/Documents/job/data/question/ip_result.xlsx',engine='xlsxwriter')
xygj_df.to_excel(excel_writer,index=False)
excel_writer.save()

#checkip(ip)
# URL =  "http://ip.taobao.com/service/getIpInfo.php?ip="+ip
# r=requests.get(URL,timeout=10)
# json_data = r.json()
# print(json_data)




