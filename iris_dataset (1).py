# -*- coding: utf-8 -*-
"""iris_dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JShWMsNQo9D6vXqraJhyyAPW27vVS9xW
"""

import numpy as np
import pandas as pd
import seaborn as sns

sns.set(color_codes=True)

df = pd.read_csv('datasets_17860_23404_IRIS.csv')

df.describe()

df.head()

df.info()

df.tail()

df['petal_width'].max() - df['petal_width'].min()

df.groupby('species')['species'].count()

df

df_ = df[df['species'] == 'Iris-setosa']

df_

df_.head()

df_.describe()

p50 = df_.sepal_length.quantile(0.50)
df1 = df_[df_['sepal_length'] >= p50]



df1.count()

df1.count()/df_.count()

p50

sns.kdeplot(df['sepal_length']);

sns.boxplot(df['sepal_length']);

sns.distplot(df['petal_length']);

sns.pairplot(df)

sns.scatterplot(x = df['sepal_length'], y = df['petal_width']);

sns.scatterplot(x = df['sepal_length'], y = df['petal_length'], hue=df['species']);

sns.pairplot(df[df['species'] == 'Iris-versicolor'], corner=True);

sns.pairplot(df[df['species'] == 'Iris-virginica'], corner=True);

sns.pairplot(df, hue='species', corner=True);

df1.head()

se_mean = df1['sepal_length'].mean()

df2 = df[df['species'] == 'Iris-virginica']

df2.head()

df3 = df[df['species'] == 'Iris-versicolor']

df3.head()

df2.describe()

df_.describe()/df2.describe()*100

df_.describe()/df3.describe()*100

df2.describe()/df3.describe()*100

sns.violinplot(x = df['sepal_length'], y = df['sepal_width'], hue = df['species'])

df1.describe()-df2.describe()

