#!/usr/bin/env python
# coding: utf-8

# # 13.1.2: Lập trình đọc tất cả tập tin và thư mục con trực tiếp của thư mục gốc ổ đĩa C và in kết quả ra màn hình.
# 

# In[1]:


import os
for (root,dist,files) in os.walk('C:\\', topdown=True):
    print(root)
    print(dist)
    print(files)


# In[ ]:




