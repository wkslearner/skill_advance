
import ti_daf.sql_util
import ti_daf.sql_context
import re
from sklearn.feature_extraction import DictVectorizer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd

'''概率分层标签函数'''
def user_delamination(dataframe,prob):
    for i in range(5):
        dataframe.loc[(dataframe[prob] >= i * 0.2) & (dataframe[prob] < (i + 1) * 0.2), 'cate'] = 'cate_' + str(i)

    return dataframe


phone_df=pd.read_excel('/Users/andpay/Documents/job/data/临时活动/信用通循环活动/phone_text_new.xlsx')
partone_df=pd.read_excel('/Users/andpay/Documents/job/data/临时活动/信用通循环活动/result_partseven_userlist.xlsx')

phone_df['partyid']=phone_df['partyid'].astype(str)
partone_df['partyid']=partone_df['partyid'].astype(str)

new_part_df=partone_df[['partyid','prob_xgc']]
new_part_df=pd.merge(new_part_df,phone_df,on='partyid',how='left')


new_part_df=user_delamination(new_part_df,'prob_xgc')
print(new_part_df['partyid'].groupby(new_part_df['cate']).count())


new_part_df=new_part_df.astype(str)
excel_writer=pd.ExcelWriter('/Users/andpay/Documents/job/data/临时活动/信用通循环活动/ob_partseven_userlist.xlsx')
new_part_df.to_excel(excel_writer,'new_user',index=False)
excel_writer.save()



