#!/usr/bin/python
# encoding=utf-8
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn2pmml.pipeline import PMMLPipeline
from sklearn2pmml import sklearn2pmml
from sklearn.datasets import load_iris
from sklearn_pandas import DataFrameMapper

iris=load_iris()

iris_df=pd.DataFrame(iris.data,columns=iris.feature_names)
iris_df['Species']=iris.target

pipeline = PMMLPipeline([("classifier", DecisionTreeClassifier())])
print(pipeline)

pipeline.fit(iris_df[iris_df.columns.difference(["Species"])], iris_df["Species"])
sklearn2pmml(pipeline, "DecisionTreeIris.pmml", with_repr = True)


# 用Mapper定义特征工程
mapper = DataFrameMapper([
    (['sbp'], MinMaxScaler()),
    (['tobacco'], MinMaxScaler()),
    ('ldl', None),
    ('adiposity', None),
    (['famhist'], LabelBinarizer()),
    ('typea', None),
    ('obesity', None),
    ('alcohol', None),
    (['age'], FunctionTransformer(np.log)),
])


#用pipeline定义使用的模型，特征工程等
pipeline = PMMLPipeline([
   ('mapper', mapper),
   ("classifier", linear_model.LinearRegression())
])

pipeline.fit(heart_data[heart_data.columns.difference(["chd"])], heart_data["chd"])
#导出模型文件
sklearn2pmml(pipeline, "lrHeart.xml", with_repr = True)
