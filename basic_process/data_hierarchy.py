#!/usr/bin/python
# encoding=utf-8
import numpy as np
import pandas as pd


df=pd.read_excel('/Users/andpay/Documents/job/data/mode_data/moderesult/moderesult18.5.4.xlsx','未绑卡')

dict={'prob_xgc':[0,0.2,0.4,0.6,0.8,1]}

def data_hierarchy(dataframe,column_dict=None):
    '''
    :param dataframe: 目标数据框
    :param column_dict: 需要分类的列及其对应的分类区间
    :return: 变量与数值映射字典及分类处理后的新数据框
    '''
    for key in column_dict.keys():
        area=column_dict[key]

        max_value=len(area)
        for i in range(max_value):
            if i <max_value-1:
                bf_key=area[i]
                af_key=area[i+1]
                dataframe.loc[(dataframe[key]>=bf_key)&(dataframe[key]<af_key),key+'_cate']=str(bf_key)+'-'+str(af_key)
            else:
                dataframe.loc[dataframe[key]>=area[i],key+'_cate']='>='+str(area[i])

    return dataframe


df=data_hierarchy(df,column_dict=dict)
cate_list=df['prob_xgc_cate'].unique()


for i in range(len(cate_list)):
    cate_df=df[df['prob_xgc_cate']==cate_list[i]]['partyid'].sample(n=3000).reset_index()
    cate_df['cate']=cate_list[i]
    if i==0:
        new_df=cate_df
    else:
        new_df=pd.concat([cate_df,new_df],axis=0)


#new=df['partyid'].groupby(df['prob_xgc_cate']).count()
print(new_df)


excel_writer=pd.ExcelWriter('/Users/andpay/Documents/job/data/活动/4.26帮还名单/nobind_filter_data.xlsx')
new_df.to_excel(excel_writer,'未绑卡',index=False)
excel_writer.save()
