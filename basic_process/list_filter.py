import pandas as pd
import numpy as np
from collections import Counter
from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE
import random
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve


# dataset=pd.read_excel('/Users/andpay/Documents/job/model/behave_model/behave_model_dataset_v2.xlsx')
# print(len(dataset))


# id_list=['1012222000007330','1012222600242259','1012222300103145','1012222000750426','1012222000890822','1012222000005061','1012222z00038830','1012222700089596','1012222200097074','1012222z00242166','1012222000734989','1012222100171321','1012222z00105389','1012222100039481','1012222000171518','1012222000213772','1012222e00052659','1012222m00216532','1012222l00157597','1012222000947599','1012222000003707','1012222z00069768','1012222600242259','1012222000842772','1012222000816764','1012222000889163','1012222m00261933','1012222000745642','1012222z00077028','1012222000023361','1012222000019066','1012222000853858','1012222f00149865','1012222000004441','1012222z00052112','1012222m00046767','1012222000006747','1012222600330615','1012222000913542','1012222100125304','1012222000023361','1012222000398349','1012222000901469','1012222000448287','1012222000854001','1012222000403147','1012222400091743','1012222000401808','1012222z00242166','1012222000734989','1012222000005061','1012222000416564','1012222000398247','1012222000005233','1012222000445780','1012222000753953','1012222000854038','1012222000816764','1012222000007330','1012222000408564','1012222000540156','1012222000823923','1012222000745186','1012222000853858','1012222000747957','1012222000006747','1012222600330615','1012222000758106','1012222000804611','1012222000004441','1012222000398349']
# end_list=set(id_list)
# print(len(id_list))
# print(len(end_list))

# dataset=dataset[~dataset['partyid'].isin(id_list)]
# print(len(dataset))


# excel_writer=pd.ExcelWriter('/Users/andpay/Documents/job/model/behave_model/behave_model_dataset_v2.xlsx')
# dataset.to_excel(excel_writer,'userlist',index=False)
# excel_writer.save()


# df=pd.read_excel('/Users/andpay/Desktop/smote_test.xlsx')
# var_list=list(df.columns)
# var_list.remove('sex')
# print(df.head())


#print(df['age'].groupby(df['sex']).count())

# sm=SMOTE(ratio=0.8,random_state=0)
# x,y=sm.fit_sample(df[var_list],df['sex'])

# print(Counter(y))
# print()

df=pd.DataFrame({'a':[1,2,2,5,0,5],'b':[2,5,6,7,3,2]})


# print(preprocessing.scale(df,axis=0))
# result=preprocessing.StandardScaler().fit(df)
# x_result=preprocessing.StandardScaler().fit_transform(df)
# print(result.get_params())
# print(result.transform(df))
# print('')
# print(x_result)