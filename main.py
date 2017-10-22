
# coding: utf-8

# In[105]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pdb


# In[106]:


idh_o = pd.read_csv("~/crawlers/output/idh.csv")
efi_o = pd.read_csv("~/crawlers/output/economic_freedom.csv")


# In[349]:


valid_names = set(efi_o.name.values) & set(idh_o.name.values)
valid_columns = np.concatenate((efi_o.columns.values, idh_o.columns.values), axis=0)
m = np.zeros(shape =(len(valid_columns), len(valid_names)))
for i, name in enumerate(valid_names):
    myval  = list(efi_o.loc[:, efi_o.columns != 'name'][efi_o.name.str.match(name)].values[0])
    myval += list(idh_o.loc[:, idh_o.columns != 'name'][idh_o.name.str.match(name)].values[0])
    for j, value in enumerate(myval):
        if np.isfinite(value):
            m[j, i] = value


# In[355]:


M = pd.DataFrame(np.corrcoef(m, rowvar=True), index=valid_columns, columns = valid_columns)


# In[360]:


plt.plot(m[70], m[7], '.')
plt.show()

