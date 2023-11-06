#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


text_image = np.zeros((100,300),dtype = 'uint8')
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX = 7
cv2.putText(text_image,"Javith",(5,70),font,2,(255),5,cv2.LINE_AA)
plt.title("Original Text Image")
plt.imshow(text_image,'bone')
plt.axis('off')


# In[3]:


kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))


# In[4]:


image_erode = cv2.erode(text_image,kernel)
plt.title("Eroded Text Image")
plt.imshow(image_erode,'bone')
plt.axis('off')


# In[5]:


image_dilate = cv2.dilate(text_image,kernel)
plt.title("Dilated Text Image")
plt.imshow(image_dilate,'bone')
plt.axis('off')


# In[ ]:




