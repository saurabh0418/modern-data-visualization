#!/usr/bin/env python
# coding: utf-8

# In[2]:


## project on matplotlib by me in python
from mpl_toolkits import mplot3d  
import sys
from matplotlib import pyplot as plt
import numpy as np
print(">>>>>>>>>>>>>>>>>>>>>>>>>> šš“š»š²š¾š¼š“ šš¾ ššš°ššøšššøš²š š¼š°š½š°š¶š“š¼š“š½š ššššš“š¼ >>>>>>>>>>>>>>>>>>>\n\n")
print("ššššš šššššš šš šššš šš šš ššššššš šš š šššš:")
n=int(input())
print("šššššš ššššš šššššš ššš š-šššš ")
l1=[]
l2=[]
for i in range(n):
    x1=input()
    l1.append(x1)
    
print("ššššš šššššš šš šššš šš šš ššššššš šš š-šššš")

m=int(input())
print("ššššš šššššš ššš š-šššš")
for i in range(m):
    x2=input()
    l2.append(x2)
    #title
print("ššššš ššššš ššššš ")
tit=input()
print("ššššš ššššš ššš š-šššš: ")
labelx=input()
print("ššššš ššššš ššš š-šššš : ")
labely=input()
print("\nšššššš šššš ššššššššššššš :")
print("š­. ššš„-šš„šš£š")
print("š®. š¦ššš§š§šš„ šš„šš£š")
print("šÆ. ššš¦š§š¢-šš„šš£š")
print("š°. ššš”š šš„šš£š")
print("5. 3-D Scatter Plot")
print("š“š½šš“š š²š·š¾šøš²š“ šµšš¾š¼ š°š±š¾šš“ : ")
CHOICE=int(input())
try :
    def plot(CHOICE):
        if(CHOICE==1): 
         plt.bar(l1, l2)
         plt.title(tit)
         plt.ylabel(labelx)
         plt.xlabel(labely)
         plt.show()
        if(CHOICE==2): 
         plt.scatter(l1, l2)
         plt.title(tit)
         plt.ylabel(labelx)
         plt.xlabel(labely)
         plt.show()
        if(CHOICE==3): 
         plt.hist(l1,l2)
         plt.title(tit)
         plt.ylabel(labelx)
         plt.xlabel(labely)
         plt.show()
        if(CHOICE==4): 
         plt.plot(l1,l2)
         plt.title(tit)
         plt.ylabel(labelx)
         plt.xlabel(labely)
         plt.show()
        if (CHOICE==5):
         height = np.array(l1)  
         weight = np.array(l2)  
         #scatter(height,weight)  
         fig = plt.figure()  
         ax=plt.axes(projection='3d')  
# This is used to plot 3D scatter  
         ax.scatter3D(height,weight)  
         plt.title(tit)  
         plt.ylabel(labelx)
         plt.xlabel(labely)
         plt.show()  
    print(plot(CHOICE))
except:
     print("\nerror occured")
    


# ### 

# ### 

# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




