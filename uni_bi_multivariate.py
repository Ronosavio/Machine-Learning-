import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("D:/DS/CSV_files/iris.csv")
print(df.head())

#Univariate Analysis 
print(df.shape)

df_setosa = df.loc[df['species'] == 'setosa']
df_virginica = df.loc[df['species'] == 'virginica']
df_versicolor = df.loc[df['species'] == 'versicolor']

plt.plot(df_setosa['petal_length'], np.zeros_like(df_setosa['petal_length']), 'o')
plt.plot(df_virginica['petal_length'], np.zeros_like(df_virginica['petal_length']), 'o')
plt.plot(df_versicolor['petal_length'], np.zeros_like(df_versicolor['petal_length']), 'o')
plt.xlabel('Petal_Length')
plt.title('UNIVARIATE')

#bivariate 
grid = sns.FacetGrid(df, hue='species', height = 5)
grid.map(plt.scatter, 'sepal_length', 'sepal_width').add_legend();
grid.fig.suptitle('BIVARIATE', fontsize=16)

#multivariate
sns.pairplot(df, hue = 'species', height= 5).fig.suptitle('MULTIVARIATE')
plt.show()