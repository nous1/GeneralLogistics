# -*- coding: utf-8 -*-

# Load libraries
import pandas
import numpy as np
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Imputer
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier

# Load dataset
url = "/home/corvus/Desktop/CREDITRISK_RAW.xlsx"
names = ['ID', 'GENERO', 'RENTA', 'EDAD', 'NIV_EDUC','E_CIVIL','COD_OFI','COD_COM','CIUDAD','Credito_1','Credito_2',
'Credito_3','Credito_4','Monto_solicitado','Dias_de_mora','Monto_deuda_promedio','meses_inactivo','numero_cuotas','aval','PAGA']
dataset = pandas.read_excel(url, names=names, float_format='%.f')

# Console size
pandas.set_option('display.height', 2000)
pandas.set_option('display.max_rows', 500)
pandas.set_option('display.max_columns', 500)
pandas.set_option('display.width', 1300)

#==============================================================================
# print(dataset['numero_cuotas'].describe())
# print(dataset.dtypes) -- TIPOS DE DATOS
#==============================================================================

#==============================================================================
# GRAFICAR
# fig, ax = plt.subplots()
# dataset.plot.scatter(x='ID',y='NIV_EDUC_ENCODED',s=1, color='red', label='Credito_2')
# ax.ticklabel_format(style='plain')
# plt.show()
#==============================================================================

# Transformar columnas nominales
dataset['NIV_EDUC'] = LabelEncoder().fit_transform(dataset['NIV_EDUC'])
dataset['GENERO'] = dataset['GENERO'].map({'F       ':0,'M       ':1})
dataset['aval'] = dataset['aval'].map({'SI':0,'NO':1})
dataset['E_CIVIL']  = LabelEncoder().fit_transform(dataset['E_CIVIL'])
dataset['PAGA']=LabelEncoder().fit_transform(dataset['PAGA']);

# ----PENDIENTE------
# HOT ONE Encoding para ciudades (78 ciudades)
#pandas.get_dummies(dataset['CIUDAD'], prefix='CIUDAD').head(1)
dataset = pandas.concat([dataset, pandas.get_dummies(dataset['CIUDAD'], prefix='CIUDAD')], axis=1)
# --------------------

# Mostrar valores unicos de NIV_EDUC
#print(dataset.NIV_EDUC.unique())

# Eliminar columnas originales
#==============================================================================
# del dataset['GENERO']
# del dataset['CIUDAD']
# del dataset['NIV_EDUC']
# del dataset['E_CIVIL']
# del dataset['CIUDAD']
#==============================================================================

# Eliminar todas las filas donde Monto_solicitado sea cero. (406 Filas)
dataset = dataset.drop(dataset[dataset['Monto_solicitado']==0].index)
# Eliminar todas las filas donde Credito_2 sea negativo. (52 filas)
dataset = dataset.drop(dataset[dataset['Credito_2']<0].index)


array = dataset[['GENERO','EDAD','aval','Credito_1','Credito_2','Credito_3','Credito_4','RENTA',
   'Monto_solicitado','Monto_deuda_promedio','PAGA']].values;


imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp = imp.fit(array)
array= imp.transform(array)

X = array[:,0:10]
Y = array[:,10]

validation_size = 0.2
seed = 7

X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

#==============================================================================
# clf = RandomForestClassifier(n_jobs=2, random_state=0);
# clf.fit(Xtr,Ytr);
#==============================================================================


# Test options and evaluation metric
seed = 7
scoring = 'accuracy'

models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
models.append(('RF', RandomForestClassifier()))
models.append(('BG', BaggingClassifier()));
# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    chars = ["GENERO","EDAD","aval",'Credito_1','Credito_2','Credito_3','Credito_3','Credito_','RENTA','Monto_solicitado','Monto_deuda_promedio']
    if name=='RF':
        model.fit(X_train,Y_train)
        for i in range(len(chars)-1):
            print(chars[i],': ',model.feature_importances_[i]);    
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)


# Compare Algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()
    
    
# Feature importances

    
