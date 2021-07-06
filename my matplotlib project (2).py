#!/usr/bin/env python
# coding: utf-8

# In[2]:


## project on matplotlib by me in python
from mpl_toolkits import mplot3d  
import sys
from matplotlib import pyplot as plt
import numpy as np
print(">>>>>>>>>>>>>>>>>>>>>>>>>> 🆆🅴🅻🅲🅾🅼🅴 🆃🅾 🆂🆃🅰🆃🅸🆂🆃🅸🅲🆂 🅼🅰🅽🅰🅶🅴🅼🅴🅽🆃 🆂🆈🆂🆃🅴🅼 >>>>>>>>>>>>>>>>>>>\n\n")
print("𝐄𝐍𝐓𝐄𝐑 𝐍𝐔𝐌𝐁𝐄𝐑 𝐎𝐅 𝐃𝐀𝐓𝐀 𝐓𝐎 𝐁𝐄 𝐏𝐋𝐎𝐓𝐓𝐄𝐃 𝐎𝐍 𝐗 𝐀𝐗𝐈𝐒:")
n=int(input())
print("𝐊𝐈𝐍𝐃𝐋𝐘 𝐄𝐍𝐓𝐄𝐑 𝐕𝐀𝐋𝐔𝐄𝐒 𝐅𝐎𝐑 𝐗-𝐀𝐗𝐈𝐒 ")
l1=[]
l2=[]
for i in range(n):
    x1=input()
    l1.append(x1)
    
print("𝐄𝐍𝐓𝐄𝐑 𝐍𝐔𝐌𝐁𝐄𝐑 𝐎𝐅 𝐃𝐀𝐓𝐀 𝐓𝐎 𝐁𝐄 𝐏𝐋𝐎𝐓𝐓𝐄𝐃 𝐎𝐍 𝐘-𝐀𝐗𝐈𝐒")

m=int(input())
print("𝐄𝐍𝐓𝐄𝐑 𝐕𝐀𝐋𝐔𝐄𝐒 𝐅𝐎𝐑 𝐘-𝐀𝐗𝐈𝐒")
for i in range(m):
    x2=input()
    l2.append(x2)
    #title
print("𝐄𝐍𝐓𝐄𝐑 𝐆𝐑𝐀𝐏𝐇 𝐓𝐈𝐓𝐋𝐄 ")
tit=input()
print("𝐄𝐍𝐓𝐄𝐑 𝐋𝐀𝐁𝐄𝐋 𝐅𝐎𝐑 𝐗-𝐀𝐗𝐈𝐒: ")
labelx=input()
print("𝐄𝐍𝐓𝐄𝐑 𝐋𝐀𝐁𝐄𝐋 𝐅𝐎𝐑 𝐘-𝐀𝐗𝐈𝐒 : ")
labely=input()
print("\n𝐒𝐄𝐋𝐄𝐂𝐓 𝐓𝐘𝐏𝐄 𝐕𝐈𝐒𝐔𝐀𝐋𝐈𝐙𝐀𝐓𝐈𝐎𝐍 :")
print("𝟭. 𝗕𝗔𝗥-𝗚𝗥𝗔𝗣𝗛")
print("𝟮. 𝗦𝗖𝗔𝗧𝗧𝗘𝗥 𝗚𝗥𝗔𝗣𝗛")
print("𝟯. 𝗛𝗜𝗦𝗧𝗢-𝗚𝗥𝗔𝗣𝗛")
print("𝟰. 𝗟𝗜𝗡𝗘 𝗚𝗥𝗔𝗣𝗛")
print("5. 3-D Scatter Plot")
print("🅴🅽🆃🅴🆁 🅲🅷🅾🅸🅲🅴 🅵🆁🅾🅼 🅰🅱🅾🆅🅴 : ")
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




