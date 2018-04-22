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

# Load dataset
url = "/home/corvus/Desktop/CREDITRISK_RAW.xlsx"
names = ['ID', 'GENERO', 'RENTA', 'EDAD', 'NIV_EDUC','E_CIVIL','COD_OFI','COD_COM','CIUDAD','Credito_1','Credito_2',
'Credito_3','Credito_4','Monto_solicitado','Dias_de_mora','Monto_deuda_promedio','meses_inactivo','numero_cuotas','aval','PAGA']
dataset = pandas.read_excel(url, names=names, float_format='%.f')

# Console size
pandas.set_option('display.height', 2000)
pandas.set_option('display.max_rows', 500)
pandas.set_option('display.max_columns', 500)
pandas.set_option('display.width', 2000)



# print(dataset['numero_cuotas'].describe())
# print(dataset.dtypes) -- TIPOS DE DATOS




#fig, ax = plt.subplots()
#dataset.plot.scatter(x='ID',y='Credito_4',s=1, color='red', label='RENTA')
#ax.ticklabel_format(style='plain')
#plt.show()

# Transformar columnas nominales a numericas
dataset['NIV_EDUC_ENCODED'] = LabelEncoder().fit_transform(dataset['NIV_EDUC']) 
dataset['GENERO_ENCODED'] = dataset['GENERO'].map({'F       ':0,'M       ':1})
dataset['E_CIVIL_ENCODED']  = LabelEncoder().fit_transform(dataset['E_CIVIL'])
dataset['CIUDAD_ENCODED'] = LabelEncoder().fit_transform(dataset['CIUDAD'])
# Eliminar columnas originales
del dataset['GENERO']
del dataset['NIV_EDUC']
del dataset['E_CIVIL']
del dataset['CIUDAD']
# Eliminar todas las filas donde Monto_solicitado sea cero.
dataset = dataset.drop(dataset[dataset['Monto_solicitado']==0].index)










