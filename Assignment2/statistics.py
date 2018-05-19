#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

# Create dataframe

csv_file = "agaricus-lepiota.data.csv";
column_names = ['edible','cap-sh','cap-sur','cap-col','brui',
        'odor','gill-att','gill-spa','gill-size','gill-col',
        'stalk-sh','stalk-root','stalk-surab-ring',
        'stalk-surbe-ring','stalk-col-abring',
        'stalk-col-bering', 'veil-ty', 'veil-col',
        'ring-nu', 'ring-ty', 'spore-printcol',
        'population','habitat'];
df = pd.read_csv(csv_file, na_values='.',
        names=column_names);

titles = ['Edible','Cap Shape','Cap Surface','Cap Color',
        'Bruises', 'Odor','Gill Attchment','Gill Spacing',
        'Gill Size','Gill Color',
        'Stalk Shape','Stalk Root','Stalk Surface Above Ring',
        'Stalk Surface Below Ring','Stalk Color-Above Ring',
        'Stalk Color Below Ring', 'Veil Type', 'Veil Color',
        'Ring Number', 'Ring Type', 'Spore Print Color',
        'Population','Habitat'];

# Show categorical

for i in range(len(titles)):
    (df[column_names[i]].value_counts()/8142.).plot(kind='bar',
            title=titles[i]);
    plt.ylabel('Percent');
    plt.xlabel('Value');
    plt.show();

