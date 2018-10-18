import argparse
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split

df=pd.DataFrame({'col1':[1,2,3,4],'col2':['a','b','a','c'],'col3':[7,8,9,10],'col4':[87,83,98,19]})
df=pd.pivot_table(df,index='col1',columns='col2',values=['col3','col4']).reset_index(level='col1',col_level=0,col_fill='d')
df.columns.names=['col','cate']

df=df.swaplevel('cate','col',axis=1)

# df=df.sortlevel(level=[0,1],ascending=[0,0],axis=1)
# df=df.sortlevel(level=[1],ascending=[0],axis=1)
# df=df.reset_index(level='col1',col_level=1)
df.columns.names=[None,None]
print(df)

excel_writer=pd.ExcelWriter('',engine='xlsxwriter')
df.to_excel(excel_writer,index=False)
excel_writer.save()

# parser = argparse.ArgumentParser()
# parser.add_argument("echo",default=10)
# args = parser.parse_args()
# print (args)

