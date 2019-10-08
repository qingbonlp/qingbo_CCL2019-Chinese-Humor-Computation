# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:39:07 2019

@author: qingbo
"""

import pandas as pd
import numpy as np


df = pd.read_csv('datasets/data_car/train.csv')
df1 = pd.read_csv('datasets/data_car/test.csv')

'''df2 = pd.read_csv('datasets/data_humor/task1_test.csv')
df3 = pd.read_csv('datasets/data_humor/task1.csv')

df4 = pd.read_excel('datasets/data_humor/test2.xlsx')
df5 = pd.read_excel('datasets/data_humor/test30.xlsx')

df6 = pd.read_excel('datasets/data_humor/joke_category.xlsx')
df7 = pd.read_excel('datasets/data_humor/joke_degree.xlsx')'''

df = df.append(df1)
df.index = range(len(df))
'''dfx = df2.append(df3)
dfxx = df4.append(df5)
dfxxx = df6.append(df7)

df.index = range(len(df))
dfx.index = range(len(dfx))
dfxx.index = range(len(dfxx))
dfxxx.index = range(len(dfxxx))'''

with open('corpora/ccfcar_bert.txt','w', encoding="utf-8") as f:    #设置文件对象
    for i in range(len(df)):
        title = df['title'][i]
        content = df['content'][i]
        if not pd.isna(title): 
            num = int(len(title)/2) 
            str = title[0:num] + '\n'
            f.write(str)
            str = title[num+1:len(title)] + '\n'
            f.write(str)
            f.write('\n')
        if not pd.isna(content):
            num = int(len(content)/2) 
            str = content[0:num] + '\n'
            f.write(str)
            str = content[num+1:len(content)] + '\n'
            f.write(str)
            f.write('\n')
    '''for i in range(len(df)):
        title = df['joke'][i]
        #content = df['transform_joke'][i]
        if not pd.isna(title):
            num = int(len(title)/2)
            str = title[0:num] + '\n'
            f.write(str)
            str = title[num+1:len(title)] + '\n'
            f.write(str)
            f.write('\n')
    for i in range(len(dfxx)):
        try:
            title = dfxx['content'][i]
            title = title.replace(' ', '').replace('\n', '')
            # content = df['transform_joke'][i]
            if not pd.isna(title):
                num = int(len(title) / 2)
                str = title[0:num] + '\n'
                f.write(str)
                str = title[num + 1:len(title)] + '\n'
                f.write(str)
                f.write('\n')
        except:
            print(i)
    for i in range(len(dfxxx)):
        try:
            title = dfxxx['joke'][i]
            #title = title.replace(' ', '').replace('\n', '')
            # content = df['transform_joke'][i]
            if not pd.isna(title):
                num = int(len(title) / 2)
                str = title[0:num] + '\n'
                f.write(str)
                str = title[num + 1:len(title)] + '\n'
                f.write(str)
                f.write('\n')
        except:
            print(i)'''
