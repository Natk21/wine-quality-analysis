import numpy as np
import pandas as pd
from time import time
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Wine-Quality/winequality-red.csv", sep=';')


print(data.isnull().any())



n_wines = len(data)

#7 and above is good quality wines
quality_above_6 = data.loc[(data['quality']>=7)]
n_above_6 = len(quality_above_6)

#bad quality wines
quality_below_5 = data.loc[(data['quality'] < 5)]
n_below_5 = len(quality_below_5)

#between 5 and six is mid quality
quality_between_5 = data.loc[(data['quality'] >= 5) & (data['quality'] <= 6)]
n_between_5 = len(quality_between_5)

#% of wines of good quality
greater_percent = len(quality_above_6)*100/n_wines

print("Total number of wine data: {}".format(n_wines))
print("Wines with rating 7 and above: {}".format(n_above_6))
print("Wines with rating less than 5: {}".format(n_below_5))
print("Wines with rating 5 and 6: {}".format(n_between_5))
print("Percentage of wines with quality 7 and above: {:.2f}%".format(greater_percent))

print(np.round(data.describe()))

#graphing the amount of wines at each quality

sns.countplot(data, x=data['quality'])
plt.xticks(rotation=-45)
plt.xlabel('Quality')
plt.ylabel('Total Number')
plt.title('Number of each type of quality of wine')




correlation = data.corr()
# display correlation via a heatmap for all variables

plt.figure(figsize=(14, 12))
heatmap = sns.heatmap(correlation, annot=True, linewidths=0, vmin=-1, cmap="RdBu_r")




#Visualize the co-relation between pH and fixed Acidity

#Create a new dataframe containing only pH and fixed acidity columns to visualize their co-relations
fixedAcidity_pH = data[['pH', 'fixed acidity']]

#Initialize a joint-grid with the dataframe, using seaborn library
gridA = sns.JointGrid(x="fixed acidity", y="pH", data=fixedAcidity_pH)

#Draws a regression plot in the grid 
gridA = gridA.plot_joint(sns.regplot, scatter_kws={"s": 10})

#Draws a distribution plot in the same grid
gridA = gridA.plot_marginals(sns.histplot)


#Fixed Acidity vs. Citric Acid

fixedAcidity_CitricAcid = data[['fixed acidity','citric acid']]
gridB = sns.JointGrid(x='fixed acidity', y='citric acid', data=fixedAcidity_CitricAcid)

gridB = gridB.plot_joint(sns.regplot, scatter_kws = {"s":10})
gridB = gridB.plot_marginals(sns.histplot)


volatileAcidity_quality = data[['volatile acidity','quality']]
fig, axs = plt.subplots(ncols=1,figsize=(10,6))
sns.barplot(x='quality', y='volatile acidity', data=volatileAcidity_quality, ax=axs)
plt.title('quality VS volatile acidity')

#or plt.xticks(-45)
plt.tight_layout()


#alcohol vs quality
quality_alcohol = data[['quality', 'alcohol']]
fig, axs = plt.subplots(ncols=1,figsize=(10,6))
sns.barplot(x='quality', y='alcohol', data=quality_alcohol, ax=axs)
plt.title('quality VS alcohol')

plt.tight_layout()
plt.show()


# For each feature find the data points with extreme high or low values
for feature in data.keys():
    # Calculate Q1 (25th percentile of the data) for the given feature
    Q1 = np.percentile(data[feature], q=25)

    # Calculate Q3 (75th percentile of the data) for the given feature
    Q3 = np.percentile(data[feature], q=75)

    # Use the interquartile range to calculate an outlier step (1.5 times the interquartile range)
    interquartile_range = Q3 - Q1
    step = 1.5 * interquartile_range

    # Display the outliers
    print("Data points considered outliers for the feature '{}':".format(feature))
    print(data[~((data[feature] >= Q1 - step) & (data[feature] <= Q3 + step))])

    # OPTIONAL: Select the indices for data points you wish to remove
    outliers = []
    # Remove the outliers, if any were specified
    good_data = data.drop(data.index[outliers]).reset_index(drop = True)