#!/usr/bin/python
# encoding=utf-8
import numpy as np
import pandas as pd

'''概率分层标签函数'''
def user_delamination(dataframe,prob):
    for i in range(5):
        dataframe.loc[(dataframe[prob] >= i * 0.2) & (dataframe[prob] < (i + 1) * 0.2), 'cate'] = 'cate_' + str(i)

    return dataframe


'''dataframe拼接'''
def df_concat(df_list):
    end_df=pd.DataFrame()
    for df in df_list:
        end_df=pd.concat([end_df,df],axis=0)

    return end_df

origin_dataset=pd.read_excel('/Users/andpay/Documents/job/data/信用通活动/信用通活动18.9.4/origin_userlist.xlsx')
drop_dataset=pd.read_excel('/Users/andpay/Documents/job/data/信用通活动/信用通活动18.8.28/result_userlist.xlsx')

result_dataset=origin_dataset[~origin_dataset['partyid'].isin(drop_dataset['partyid'])]

excel_writer=pd.ExcelWriter('/Users/andpay/Documents/job/data/信用通活动/信用通活动18.9.4/result_userlist.xlsx')
result_dataset.to_excel(excel_writer,'userlist',index=False)
excel_writer.save()





