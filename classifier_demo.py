# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 22:30:33 2018

@author: HP 15-E015TX
"""

Accuracy={}
######################## Naive Bayes Classifier##############################
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Accuracy Score
from sklearn.metrics import accuracy_score
print ('Accuracy Score :', accuracy_score(y_test, y_pred))
Accuracy['GaussianNB']= accuracy_score(y_test, y_pred)

######################### KNN Classifier #####################################
from sklearn.neighbors import KNeighborsClassifier
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Accuracy Score
from sklearn.metrics import accuracy_score
print ('Accuracy Score :', accuracy_score(y_test, y_pred))
Accuracy['KNeighborsClassifier']= accuracy_score(y_test, y_pred)

########################## Decision Tree ####################################
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Accuracy Score
from sklearn.metrics import accuracy_score
print ('Accuracy Score :', accuracy_score(y_test, y_pred))
Accuracy['DecisionTreeClassifier']= accuracy_score(y_test, y_pred)

############################ RandomForest ##################################
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Accuracy Score
from sklearn.metrics import accuracy_score
print ('Accuracy Score :', accuracy_score(y_test, y_pred))
Accuracy['RandomForestClassifier']= accuracy_score(y_test, y_pred)


############################ LogisticRegression ##############################
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Accuracy Score
from sklearn.metrics import accuracy_score
print ('Accuracy Score :', accuracy_score(y_test, y_pred))
Accuracy['LogisticRegression']= accuracy_score(y_test, y_pred)

########################### Support Vector Machine ##########################
from sklearn.svm import SVC
classifier = SVC()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Accuracy Score
from sklearn.metrics import accuracy_score
print ('Accuracy Score :', accuracy_score(y_test, y_pred))
Accuracy['SVC']= accuracy_score(y_test, y_pred)
