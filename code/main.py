# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 23:25:09 2018

@author: XZF
"""


from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
import numpy as np
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
import pandas as pd
from functools import reduce
from sklearn.svm import SVC
import utils.tools as utils
import scipy.io as sio
import lightgbm as lgb
from sklearn.preprocessing import scale,StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score
from L1_Matine import elasticNet
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import StratifiedKFold,LeaveOneOut




def SelectModel(modelname):

    if modelname == "SVM":
        
        model = SVC(kernel='rbf', C=16, gamma=0.0313,probability=True)
    

    elif modelname == "GBDT":
        
        model = GradientBoostingClassifier()

    elif modelname == "RF":
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier(n_estimators=500)

    elif modelname == "XGBOOST":
        from xgboost.sklearn import XGBClassifier
        #import xgboost as xgb
        #model = xgb()
        print('+++++++++++++++++++++++++')
        model = XGBClassifier()

    elif modelname == "KNN":
        from sklearn.neighbors import KNeighborsClassifier as knn
        model = knn()
    elif modelname == "lgb":
        model = lgb.LGBMClassifier(n_estimators=500,max_depth=15,learning_rate=0.2)
    else:
        pass
    return model

def calculate_performace(test_num, pred_y, labels):
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for index in range(test_num):
        if labels[index] == 1:
            if labels[index] == pred_y[index]:
                tp = tp + 1
            else:
                fn = fn + 1
        else:
            if labels[index] == pred_y[index]:
                tn = tn + 1
            else:
                fp = fp + 1

    acc = float(tp + tn) / test_num
    precision = float(tp) / (tp + fp)
    sensitivity = float(tp) / (tp + fn)
    specificity = float(tn) / (tn + fp)
    MCC = float(tp * tn - fp * fn) / (np.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)))
    return acc, precision, sensitivity, specificity, MCC

def get_oof(clf,n_folds,X_train,y_train,X_test):
    ntrain = X_train.shape[0]
    ntest =  X_test.shape[0]
    classnum = len(np.unique(y_train))
    kf = KFold(n_splits=n_folds,random_state=1)
    oof_train = np.zeros((ntrain,classnum))
    oof_test = np.zeros((ntest,classnum))


    for i,(train_index, test_index) in enumerate(kf.split(X_train)):
        kf_X_train = X_train[train_index] # 
        kf_y_train = y_train[train_index] # 

        kf_X_test = X_train[test_index]  # k-fold

        clf.fit(kf_X_train, kf_y_train)
        oof_train[test_index] = clf.predict_proba(kf_X_test)

        oof_test += clf.predict_proba(X_test)
    oof_test = oof_test/float(n_folds)
    return oof_train, oof_test



data1 = sio.loadmat(r'E:/code/all_3_optemDim_rand50.mat')

data2=data1.get('label_mappedX')


row=data2.shape[0]
column=data2.shape[1]
index = [i for i in range(row)]
np.random.shuffle(index)
index=np.array(index)
data_1=data2[index,:]
shu=data_1[:,np.array(range(1,column))]
label=data_1[:,0]


X=shu
label[label==-1]=0
y=label
sepscores = []
ytest=np.ones((1,2))*0.5
yscore=np.ones((1,2))*0.5
ypred=np.ones((1,2))*0.5
skf= StratifiedKFold(n_splits=3)
loo = LeaveOneOut()

for train, test in skf.split(X,y):

   print((train.shape, test.shape))
   modelist = ['lgb','XGBOOST','SVM','RF','KNN']
   #modelist = ['lgb','XGBOOST','SVM','GBDT','RF']
   #modelist = ['lgb','XGBOOST','SVM']
   newfeature_list = []
   newtestdata_list = []
   for modelname in modelist:
       clf_first = SelectModel(modelname)
       oof_train_ ,oof_test_= get_oof(clf=clf_first,n_folds=10,X_train=X[train],y_train=y[train],X_test=X[test])
       newfeature_list.append(oof_train_)
       newtestdata_list.append(oof_test_)
   newfeature = reduce(lambda x,y:np.concatenate((x,y),axis=1),newfeature_list)    
   newtestdata = reduce(lambda x,y:np.concatenate((x,y),axis=1),newtestdata_list)
  
   
   clf_second1 = SVC(kernel='rbf', C=8, gamma=0.0313,probability=True)
   clf_second1.fit(newfeature, y[train])
   y_score=clf_second1.predict_proba(newtestdata) #clf.predict_proba
   y_test=utils.to_categorical(y[test]) 
   pred = clf_second1.predict(newtestdata)
   y_pred = utils.to_categorical(pred)
   print(pred.shape)
   print(y_pred.shape)
   yscore=np.vstack((yscore,y_score))
   print(ytest.shape)
   print(y_test.shape)
   ytest = np.vstack((ytest, y_test))
   ypred=np.vstack((ypred,y_pred))
    
   accuracy = metrics.accuracy_score(y[test], pred)*100
   print (accuracy)
    #utils.plothistory(hist)
    #prediction probability
      
   fpr, tpr, _ = roc_curve(y_test[:,0], y_score[:,0])
   roc_auc = auc(fpr, tpr)
   y_class= utils.categorical_probas_to_classes(y_score)
   y_test_tmp=y[test]
   acc, precision,npv, sensitivity, specificity, mcc,f1 = utils.calculate_performace(len(y_class), y_class, y_test_tmp)
   sepscores.append([acc, precision,npv, sensitivity, specificity, mcc,f1,roc_auc])
   gbm=[]
   print('gbm:acc=%f,precision=%f,npv=%f,sensitivity=%f,specificity=%f,mcc=%f,f1=%f,roc_auc=%f'
          % (acc, precision,npv, sensitivity, specificity, mcc,f1, roc_auc))
    
scores=np.array(sepscores)
print("acc=%.2f%% (+/- %.2f%%)" % (np.mean(scores, axis=0)[0]*100,np.std(scores, axis=0)[0]*100))
print("precision=%.2f%% (+/- %.2f%%)" % (np.mean(scores, axis=0)[1]*100,np.std(scores, axis=0)[1]*100))
print("npv=%.2f%% (+/- %.2f%%)" % (np.mean(scores, axis=0)[2]*100,np.std(scores, axis=0)[2]*100))
print("sensitivity=%.2f%% (+/- %.2f%%)" % (np.mean(scores, axis=0)[3]*100,np.std(scores, axis=0)[3]*100))
print("specificity=%.2f%% (+/- %.2f%%)" % (np.mean(scores, axis=0)[4]*100,np.std(scores, axis=0)[4]*100))
print("mcc=%.2f%% (+/- %.2f%%)" % (np.mean(scores, axis=0)[5]*100,np.std(scores, axis=0)[5]*100))
print("f1=%.2f%% (+/- %.2f%%)" % (np.mean(scores, axis=0)[6]*100,np.std(scores, axis=0)[6]*100))
print("roc_auc=%.2f%% (+/- %.2f%%)" % (np.mean(scores, axis=0)[7]*100,np.std(scores, axis=0)[7]*100))
result1=np.mean(scores,axis=0)

H1=result1.tolist()
sepscores.append(H1)

result=sepscores

data_csv = pd.DataFrame(data=result)
data_csv.to_csv('all_result.csv')


row=yscore.shape[0]
yscore=yscore[np.array(range(1,row)),:]
yscore_sum = pd.DataFrame(data=yscore)
yscore_sum.to_csv('all_Fscore.csv')

ytest=ytest[np.array(range(1,row)),:]
ytest_sum = pd.DataFrame(data=ytest)
ytest_sum.to_csv('alltest.csv')

ypred=ypred[np.array(range(1,row)),:]
ypred_sum = pd.DataFrame(data=ypred)
ypred_sum.to_csv('allypred.csv')

fpr, tpr, _ = roc_curve(ytest[:,0], yscore[:,0])
#auc_score=np.mean(scores, axis=0)[7]

