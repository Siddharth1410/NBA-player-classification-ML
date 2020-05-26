#!/usr/bin/env python
# coding: utf-8

# In[724]:


'''
Siddharth Vadgama
1001397508
'''
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns
from sklearn.metrics import confusion_matrix
from collections import Counter
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
'''
Reading file and creating feature columns and target column.
'''
nba = pd.read_csv('NBAstats.csv')
original_headers = list(nba.columns.values)
class_column = 'Pos'
feature_columns = ['G', 'FG%',     '3P%',  '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB',      'AST', 'STL', 'BLK', 'TOV', 'PF', 'PS/G']
nba_feature = nba[feature_columns]
nba_class = nba[class_column]
'''
Scale the data using SKLearn Pre Processing to avoid overfitting.
'''
nba_feature=pd.DataFrame(StandardScaler().fit_transform(nba_feature))

train_feature, test_feature, train_class, test_class =     train_test_split(nba_feature, nba_class, stratify=nba_class,     train_size=0.75, test_size=0.25)
training_accuracy = []
test_accuracy = []
#for i in range(2,10):
#    model=RandomForestClassifier(max_depth=i)
'''
Creating a model and trainging it.
'''
model= RandomForestClassifier(max_depth=6)
model.fit(train_feature, train_class)
predict= model.predict(test_feature)
'''
Evaluation
'''
print("Test set predictions:\n{}".format(predict))
print("Test set accuracy: {:.2f}\n\n".format(model.score(test_feature, test_class)))
print("Confusion Matrix")
print("{}".format(test_class.unique()))
print(confusion_matrix(test_class,list(predict),labels=test_class.unique()))
'''
cross validation
'''
scores = cross_val_score(model, nba_feature, nba_class, cv=10)
print("\n\nAccuracy in each Fold:\n{}".format(scores))
print("\nAvg cross val score: {:.2f}\n\n".format(sum(scores)/10))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[477]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




