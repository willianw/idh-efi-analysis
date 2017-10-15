
# coding: utf-8

# In[146]:


import matplotlib.pyplot as plt
import pandas as pd
import pdb


# In[147]:


idh = pd.read_csv("~/crawlers/output/idh.csv")
efi = pd.read_csv("~/crawlers/output/economic_freedom.csv")


# In[176]:


scat = [[],[], []]
for i in range(idh.count()[0]):
    name = idh['name'][i]
    if efi.name.str.contains(name).any():
        try:
            scat[1].append(efi[efi.name.str.match(name)].efi.values[0])
            scat[0].append(idh.idh[i])
            scat[2].append(name)
        except:
            pass

plt.plot(scat[1], scat[0], '.')
plt.show()
