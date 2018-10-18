#!/usr/bin/python3
# coding: utf-8

from ti_daf import SqlTemplate,sql_util

class Person(object):

    #类属性，实例属性每个实例都各自拥有，互相独立，而类属性有且只有一份
    address='shanghai'

    #**kw未可变参数，用户可自行设定
    def __init__(self, name='David', gender='Male', score=0,**kw):
        #self为类实例
        self.name = name
        self.gender = gender
        self.__score=score   #私有属性，不能在类外被访问

        #设置可变属性
        for k,v in kw.items():
            setattr(self, k, v )


    #装饰器可以在类初始化前，对数据进行处理(可用于处理)
    @classmethod
    def get_para(cls,name,gender):
        para=cls(name,gender)

        return para


    def get_basicinfo(self):
        name=self.name
        gender=self.gender

        return name,gender


    #私有类方法，只能在类内被调用
    def __caculate(self):
        pass



xiaoming = Person.get_para('Xiao Ming', 'Male')

print(xiaoming.get_basicinfo())
print(xiaoming.address)