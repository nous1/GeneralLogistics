#!/usr/bin/env python3

from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,f1_score
import pandas as pd
import matplotlib.pyplot as plt
from pandas import plotting

# Create Data Frame

csv_file = "agaricus-lepiota.data.csv";
column_names = ['edible', 'cap-sh','cap-sur','cap-col','brui',
        'odor','gill-att','gill-spa','gill-size','gill-col',
        'stalk-sh','stalk-root','stalk-surab-ring',
        'stalk-surbe-ring','stalk-col-abring',
        'stalk-col-bering', 'veil-ty', 'veil-col',
        'ring-nu', 'ring-ty', 'spore-printcol',
        'population','habitat'];
df = pd.read_csv(csv_file, na_values='.',
        names=column_names);


# Selected Categorical to one-hot

selected_categs = ['cap-sh','cap-sur',
        'brui','odor','stalk-sh',
        'stalk-root','stalk-surab-ring',
        'stalk-surbe-ring','stalk-col-abring',
        'stalk-col-bering','ring-ty','population',
        'habitat'];
for cat in selected_categs:
    df=pd.get_dummies(df,columns=[cat]);


# Classify

selected_atts = ['cap-sh_x','cap-sh_f','cap-sur_y',
        'brui_t','brui_f','odor_n','stalk-sh_e',
        'stalk-sh_t','stalk-root_b','stalk-surab-ring_s',
        'stalk-surbe-ring_s','stalk-col-abring_w',
        'stalk_col-bering_w','ring-ty_p','population_v',
        'habitat_d'];
X=df[selected_atts].values;
Y=df['edible'].values;

validation_size = 0.1; seed = 7;
Xtr,Xte,Ytr,Yte=model_selection.train_test_split(
        X,Y,test_size=validation_size, random_state=seed);

clf = RandomForestClassifier(n_jobs=2, random_state=seed);
clf.fit(Xtr,Ytr); preds = clf.predict(Xte);


# Show results

accu = accuracy_score(Yte, preds);
print('Accuracy:', "%.2f" % round(100*accu,2)+'%');
for i in range(len(selected_atts)):
   print(selected_atts[i],': ', "%.2f" %\
     round(100*clf.feature_importances_[i],2)+'%');

