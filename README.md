# EXP-10 -Record-Implementation of Erosion and Dilation

## Aim:

To implement Erosion and Dilation using Python and OpenCV.

## Software Required:

1. Anaconda - Python 3.7,

2. OpenCV.

## Algorithm:

### Step 1:

Load the necessary packages requiured for the implemtation of erosion and dilation on an image.

### Step 2:

Create the text image for the implemtation of erosion and dilation using cv2.putText function.

### Step 3:

Create the structuring image for the implemtation of erosion and dilation on the text image.

### Step 4:

Apply the erosion and dilation to the text image using cv2.erode and cv2.dilate.

### Step 5:

Display the images of the erosion and dilation applied using the plt.imshow.
 
### Step 6:

End the program.

## Program:

```python

Developed by : Rama E. K. Lekshmi
Register No : 212222240082
Program to implement Erosion and Dilation using Python and OpenCV.

```

```python

# Import the necessary packages:

import cv2
import numpy as np
import matplotlib.pyplot as plt

```

```python

# Create the Text using cv2.putText:

text_image = np.zeros((100,300),dtype = 'uint8')
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX = 7
cv2.putText(text_image,"Javith",(5,70),font,2,(255),5,cv2.LINE_AA)
plt.title("Original Text Image")
plt.imshow(text_image,'bone')
plt.axis('off')

```

```python

# Create the structuring element:

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))

```

```python

# Erode the image:

image_erode = cv2.erode(text_image,kernel)
plt.title("Eroded Text Image")
plt.imshow(image_erode,'bone')
plt.axis('off')

```

```python

# Dilate the image:

image_dilate = cv2.dilate(text_image,kernel)
plt.title("Dilated Text Image")
plt.imshow(image_dilate,'bone')
plt.axis('off')

```

## Output:

### Display the input text Image:

![1](https://github.com/Rama-Lekshmi/EROSION-AND-DILATION/assets/118541549/e107e164-597f-4e4d-b468-895ab69ad107)


### Display the Eroded text Image:


![2](https://github.com/Rama-Lekshmi/EROSION-AND-DILATION/assets/118541549/26c620c5-d67f-455a-af16-03136da66833)


### Display the Dilated text Image:

![3](https://github.com/Rama-Lekshmi/EROSION-AND-DILATION/assets/118541549/55fc336f-6c9d-4f32-bc99-71b88b1c155b)


## Result:

Thus the generated text image is eroded and dilated using python and OpenCV.

