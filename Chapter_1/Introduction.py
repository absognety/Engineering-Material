# In[21]
import numpy as np
x = np.array([[1,2,3],[4,5,6]])
x_shape_prod = np.prod(x.shape)
y = x.reshape(3,2)
y_shape_prod = np.prod(y.shape) #reshape dimensions product must be equal to original shape product
z = x.reshape(6,1)
z_shape_prod = np.prod(z.shape)
w = x.reshape(1,6)
w_shape_prod = np.prod(w.shape)
check = (x_shape_prod == y_shape_prod == z_shape_prod == w_shape_prod)

# In[22]
from scipy import sparse
t = np.eye(5)
print (t)
sparse_matrix = sparse.csr_matrix(t)
print ("The Sparse CSR Matrix is \n{}".format(sparse_matrix))

# In[23]

from matplotlib import pyplot as plt
arr = np.arange(20)
y_arr = np.sin(arr)
plt.plot(arr,y_arr,marker = "x")

# In[24]

#creating a Dataframe from Python Dictionary
import pandas as pd
data = {'Name':['Stark','Thor','TChalla','Peter'],
        'Type':['Ironman','God of Thunder','Black Panther','Spider man'],
        'Alias':['Avengers','Avengers','Avengers','Avengers']}
table = pd.DataFrame(data)
data = table.sort(axis=1)

