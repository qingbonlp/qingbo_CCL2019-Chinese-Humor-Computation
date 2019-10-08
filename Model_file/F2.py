import pandas as pd
import numpy as np
from sklearn.metrics import f1_score, classification_report, confusion_matrix
from collections import Counter
import pickle
import os

def get_id(df):
    id_need = []
    for i, j in zip(df.to_dict("records"),range(df.shape[0])):
        if i["id"] < 16670:
            id_need.append(j)   
    return id_need

def out_dict(path,label):
    best_k, all_t, all_p, all_id = [], [], [], []
    for i in os.listdir(path):
        if "model_bert" not in i:
            continue
        file = os.path.join(path, i, "dev.csv")
        temp = pd.read_csv(file)
        need_id = get_id(temp)
        temp = temp.iloc[need_id]
        y_pre = np.argmax(temp[["label_0","label_1","label_2"]].values,-1)
        true = [label[int(i)] for i in temp["id"]]
        y_true = []
        for i in true:
            if i == 1:
                y_true.append(0)
            elif i == 3:
                y_true.append(1)
            elif i == 5:
                y_true.append(2)
        out = {}
        for h in range(33,100):
            label_add = []
            for i ,j, k, pre in zip(temp["label_0"],temp["label_1"],temp["label_2"], y_pre):
                if k < h/100 and pre == 2:
                    if i > j:
                        label_add.append(0)
                    else:
                        label_add.append(1)
                else:
                    label_add.append(pre)
            out[h] = label_add
        f = 0
        k = 0
        for i in out:
            f1 = f1_score(y_true,out[i],average='macro')
            if f1 > f :
                f = f1
                k = i
                label_add = out[i]
        best_k.append(k)
        print(Counter(label_add))
        all_t.extend(y_true)
        all_p.extend(label_add)
        all_id.extend(temp["id"])
    print("model:{}\nF1:{}\nbest_k:{}\n".format(path,f1_score(all_t,all_p,average='macro'),best_k))
    models_pre = []
    count = 0
    for i in os.listdir(path):
        if "model_bert" not in i:
            continue
        file = os.path.join(path, i, "sub.csv")
        temp = pd.read_csv(file)
        y_pre = np.argmax(temp[["label_0","label_1","label_2"]].values,-1)
        test_label = []
        for i ,j, k, pre in zip(temp["label_0"],temp["label_1"],temp["label_2"], y_pre):
                if k < best_k[count]/100 and pre == 2:
                    if i > j:
                        test_label.append(0)
                    else:
                        test_label.append(1)
                else:
                    test_label.append(pre)
        models_pre.append(test_label)
        count += 1
    return models_pre, all_p, all_id

def work(pres):
    count = [0,0,0]
    for i in pres:
        count[i] += 1
    out = count.index(max(count))
    if out == 0:
        return 1
    elif out == 1:
        return 3
    elif out == 2:
        return 5

def cosVector(x,y):
    if(len(x)!=len(y)):
        print('error input,x and y is not in the same space')
        return
    result1=0.0
    result2=0.0
    result3=0.0
    for i in range(len(x)):
        result1+=x[i]*y[i]   #sum(X*Y)
        result2+=x[i]**2     #sum(X*X)
        result3+=y[i]**2     #sum(Y*Y)
    return result1/((result2*result3)**0.5)

if __name__ == '__main__':
    paths = ["bert_task2","task1modelalldata_wwm","task2_xia_model","task2_robert_1005","task2_robert_alldata_1005","task2_wwm_1005","task2_wwm_alldata_1005",]
    label = pd.read_csv("../data_task2/task2_train.csv")["label"]
    out = []
    train_out = []
    for path in paths:
        model_pre, all_p, all_id = out_dict(path,label)
        train_out.append([all_p[all_id.index(i)]for i in range(len(all_id))])
        out.extend(model_pre)
    add_1 = [work(i) for i in np.transpose(np.array(out[:5])).tolist()]
    for i in range(6):
        add = [work(i) for i in np.transpose(np.array(out[:5*(i+2)])).tolist()]
        train_add = [work(i) for i in np.transpose(np.array(train_out[:i+2])).tolist()]
        cos = cosVector(add_1,add)
        print(paths[:i+2])
        print(f1_score(label,train_add,average='macro'))
        print(cos)
        print(Counter(add))
    train_final = [work(i) for i in np.transpose(np.array(train_out)).tolist()]  
    print(f1_score(label,train_final,average='macro'))
    print(Counter(train_final))
    pre_final = [work(i) for i in np.transpose(np.array(out)).tolist()]
    print(Counter(pre_final))
    df = pd.DataFrame({"id":list(range(len(pre_final))),"label":pre_final})
    df[["id","label"]].to_csv("task2_unite8_F1:{}.csv".format(round(f1_score(label,train_final,average='macro'),5)),index = False)