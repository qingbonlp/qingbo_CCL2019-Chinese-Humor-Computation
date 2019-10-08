import pandas as pd
import os
import random

from collections import Counter


train_df=pd.read_csv("task1_train.csv")
add_df = pd.read_csv("task2_train.csv")
add_df = pd.concat([add_df,pd.read_csv["task2_test.csv"]])
add_df['label'] = 1
count_fold = add_df.shape[0]//5
test_df=pd.read_csv("task1_test.csv")
train_df['label']=train_df['label'].fillna(-1)
train_df=train_df[train_df['label']!=-1]
train_df['label']=train_df['label'].astype(int)
test_df['label']=0

test_df['joke']=test_df['joke'].fillna('无')
train_df['joke']=train_df['joke'].fillna('无')

index=set(range(train_df.shape[0]))
K_fold=[]
for i in range(5):
    if i == 4:
        tmp=index
    else:
        tmp=random.sample(index,int(1.0/5*train_df.shape[0]))
    index=index-set(tmp)
    print("Number:",len(tmp))
    K_fold.append(tmp)
    
import random
for i in range(5):
    print("Fold",i)
    os.system("mkdir data_{}".format(i))
    dev_index=list(K_fold[i])
    train_index=[]
    for j in range(5):
        if j!=i:
            train_index+=K_fold[j]
    train_csv = pd.concat([train_df.iloc[train_index],add_df.iloc[i*count_fold:(i+1)*count_fold]])
    _index = list(range(train_csv.shape[0]))
    random.shuffle(_index)
    train_csv = train_csv.iloc[_index]
    train_csv.to_csv("data_{}/train.csv".format(i))
    print(Counter(test_df["label"]))
    train_df.iloc[dev_index].to_csv("data_{}/dev.csv".format(i))
    test_df.to_csv("data_{}/test.csv".format(i))