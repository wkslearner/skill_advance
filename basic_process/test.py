

import pandas as pd


'''概率分层标签函数'''
def user_delamination(dataframe,prob):
    for i in range(5):
        dataframe.loc[(dataframe[prob] >= i * 0.2) & (dataframe[prob] < (i + 1) * 0.2), 'cate'] = 'cate_' + str(i)

    return dataframe


data_df=pd.read_excel('/Users/andpay/Documents/job/model/newuser_marketing_credithands/model_practice/model_practice_v4_predict1.xlsx')
login_df=pd.read_excel('/Users/andpay/Documents/job/data/question/新户营销分析/login_list.xlsx')
# addition_df=pd.read_excel('/Users/andpay/Documents/job/data/question/新户营销分析/addition_data_p1.xlsx')

end_df=pd.merge(data_df,login_df,on='partyid',how='left')
# end_df=pd.merge(end_df,addition_df,on='partyid',how='left')


print(end_df.head())
# target_df=data_df[['partyid','diff_time','renew_yesornot','cate','prob_xgc']]
# target_df['result_cate']=target_df['diff_time'].apply(lambda x: 1 if x>=7 else 0)
# print(target_df.head())


# new_part_df=user_delamination(target_df,'prob_xgc')
# print(new_part_df['diff_time'].groupby([new_part_df['cate'],new_part_df['renew_yesornot']]).count())


excel_writer=pd.ExcelWriter('/Users/andpay/Documents/job/data/question/新户营销分析/model_practice_v4_predict_result.xlsx')
end_df.to_excel(excel_writer,index=False)
excel_writer.save()