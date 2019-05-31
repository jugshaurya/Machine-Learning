#!/usr/bin/env python
# coding: utf-8

# # Challenge - Chemicals Segregation
# 
# Chemical Segregation(Classification)
# A chemist has two chemical flasks labelled 1 and 0 which contains two different chemicals. He extracted 3 features from these chemicals in order to distinguish between them. You are provided with the results derived by the chemist and your task is to create a model that will label chemical 0 or 1 given its three features.
# 
# 
# Data Description
# You are provided with two files test and train.
# 
# Train: This files consists of two csv files LogisticXtrain and LogisticYtrain. Xtrain consists of the features whereas Ytrain consists of the labels associated with the features.
# 
# Test: This file consists of two files LogisticXtest consisting of the features of test data and sample_output which represents in which format your solution csv must be submitted.
# 
# You need to implement any classifier from scratch, don't use any sklearn based classifier.

# In[15]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# returning hx for each sample hence, a numpy array of size (m X 1)
def hypothesis(X,theta):
    return np.sum(X*theta[1:], axis=1) + theta[0] # using numpy broadcasting


# In[17]:


# retuning sigmoid for each sample hence, a numpy array of size (m X 1)
def sigmoid(X,theta):
    hx = hypothesis(X,theta)
    return 1.0 / (1.0 + np.exp(-1*hx))


# In[18]:


def gradient(X,Y,theta):
    try: 
        grad = np.zeros(X.shape[1] + 1)
        hx = sigmoid(X,theta)

        grad[0] = np.sum(hx - Y)
        for i in range(1, X.shape[1] + 1):
            grad[i] = np.sum((hx - Y)*X[:,i-1])
    except : 
        print('fsalhfhjdsflHh')
    return grad


# In[20]:


def negative_log_likelihood(X,Y,theta):
    try:    
        g_h_x = sigmoid(X,theta)
        print(g_h_x)
        log_liklihood = np.sum( Y * np.log(g_h_x) + (1 - Y) * np.log(1 - g_h_x) )
    except Exception as e :
        print('this is wrong', e)
    return  -1 * log_liklihood


# In[21]:


# goal of this function is to minimize the ``Negative of log of likelihood`` using graident descent
# code is similar to Linear Regression but hypothesis function is different

def classifier(X,Y,learning_rate=0.001):
    theta = np.zeros(X.shape[1] + 1)
    error = []
    err = negative_log_likelihood(X,Y,theta)
    error.append(err)
    while True:        
        grad = gradient(X,Y,theta)
        theta = theta - learning_rate * grad
        err = negative_log_likelihood(X,Y,theta)
        if abs(err - error[-1]) < 0.001:
            break
        error.append(err)
        
    return theta


# In[22]:


def predict(X_test, theta):
    Y_pred = np.zeros(X_test.shape[0])
    g_h_x = sigmoid(X_test,theta)
    
    for i in range(X_test.shape[0]):
        if g_h_x[i] >= 0.5:
            Y_pred[i] = 1
        else:
            Y_pred[i] = 0
    return Y_pred

    
def accuracy(Y_actual, Y_predict):
    total = Y_actual.shape[0]
    
    diff = np.sum(Y_actual == Y_predict) 
    return diff/total


# In[23]:


# loading data
X = pd.read_csv('Datasets/Assignment3_Logistic_X_Train.csv')
Y = pd.read_csv('Datasets/Assignment3_Logistic_Y_Train.csv')
test = pd.read_csv('Datasets/Assignment3_Logistic_X_Test.csv')


# In[24]:


X.shape


# In[25]:


Y.shape


# In[26]:


test.shape


# In[29]:


# preprocessing
from sklearn.preprocessing import StandardScaler
s = StandardScaler()
s.fit_transform(X)
s.transform(test)


# In[30]:


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=101)


# In[ ]:


thetas = classifier(X_train.values,Y_train.values)

print(thetas)