import pandas as pd
import os
import random

from collections import Counter


train_df=pd.read_csv("task2_train.csv")
test_df=pd.read_csv("task2_test.csv")
train_df['label']=train_df['label'].fillna(-1)
train_df=train_df[train_df['label']!=-1]
train_df['label']=train_df['label'].astype(int)
test_df['label']=0
label = []
for i in train_df['label']:
    if i == 1:
        label.append(0)
    elif i == 3:
        label.append(1)
    elif i == 5:
        label.append(2)
train_df["label"] = label

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
    

for i in range(5):
    print("Fold",i)
    os.system("mkdir data_{}".format(i))
    dev_index=list(K_fold[i])
    train_index=[]
    for j in range(5):
        if j!=i:
            train_index+=K_fold[j]
    train_df.iloc[train_index].to_csv("data_{}/train.csv".format(i))
    print(Counter(train_df.iloc[train_index]["label"]))
    train_df.iloc[dev_index].to_csv("data_{}/dev.csv".format(i))
    test_df.to_csv("data_{}/test.csv".format(i))
