#!/usr/bin/env python3

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
#  print(titanic.head())

   #  survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
#  0         0       3    male  22.0      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False
#  1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
#  2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True
#  3         1       1  female  35.0      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False
#  4         0       3    male  35.0      0      0   8.0500        S  Third    man        True  NaN  Southampton    no   True

#  sns.jointplot(x='fare', y='age', data=titanic)

#  sns.histplot(titanic['fare'], bins=30, color='red')

#  sns.boxplot(x='class', y='age', data=titanic)

#  sns.swarmplot(x='class', y='age', data=titanic, palette='Set2')

#  sns.countplot(x='sex', data=titanic)

#  sns.heatmap(titanic.corr(), cmap='coolwarm')
#  plt.title('titanic.corr()')

g = sns.FacetGrid(data=titanic, col='sex')
g.map(plt.hist, 'age')


plt.show()
