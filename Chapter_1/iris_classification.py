# %% Classical Dataset for Machine Learning

from sklearn import datasets
from matplotlib import pyplot as plt
dt = datasets.load_iris()
keys = dt.keys()
print (dt['data'])
print (dt['DESCR'])
data = dt['data']
print(dt['DESCR'][:193] + "\n...")
print (type (dt['feature_names']))
print (type(dt['target_names']))
print (dt['data'].shape)
print (dt['target'].shape)

#Classes : 0-Setosa, 1-Versicolor, 2-Virginica
# %% Train and Test Set split of Development Dataset of Iris.

from sklearn.model_selection import train_test_split
train_X,test_X,train_y,test_y = train_test_split(dt['data'],dt['target'],
                                                 random_state=0)
print (train_X.shape)
print (test_X.shape)
print (train_y.shape)
print (test_y.shape)
fig,ax = plt.subplots(3,3,figsize = (15,15))

for i in range(3):
    for j in range(3):
        ax[i, j].scatter(train_X[:, j], train_X[:, i + 1], c=train_y, s=60)
        ax[i, j].set_xticks(())
        ax[i, j].set_yticks(())
        if i == 2:
            ax[i, j].set_xlabel(dt['feature_names'][j])
        if j == 0:
            ax[i, j].set_ylabel(dt['feature_names'][i + 1])
        if j > i:
            ax[i, j].set_visible(False)
