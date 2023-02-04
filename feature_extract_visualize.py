import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import os
import cv2

file_names = os.listdir(r"./images")
file_names = ["./images/" + name for name in file_names]
images = [cv2.imread(path) for path in file_names]
images = [cv2.cvtColor(image, cv2.COLOR_BGR2RGB) for image in images]
images = np.array(images, dtype = object)

#displaying image
plt.imshow(images[1])
plt.xticks([])
plt.yticks([])
plt.title("Image")

#image colorspace
def getColorSpace(image):
    # reshape image 
    flat_img = image.reshape(-1, image.shape[-1])
    # Obtain A color only once
    unique_colors = np.unique(flat_img, axis = 0)
    return unique_colors

image = images[2]

fig = plt.figure(figsize=(12, 5))
fig.suptitle('Color Space Visualization')

# First subplot
ax = fig.add_subplot(1, 2, 1)
ax.imshow(image)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.set_title("Image")

# Second subplot
ax = fig.add_subplot(1, 2, 2, projection='3d')
unique_colors = getColorSpace(image)
red = unique_colors[:, 0]
green = unique_colors[:, 1]
blue = unique_colors[:, 2]
c = unique_colors/255
surf = ax.scatter(red, blue, green, c = c, marker = ".")
ax.set_title("Color Space")

#image color histogram
def getColorHistSeparately(image):
    image = images[3]

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.xticks([])
plt.yticks([])
plt.title("Nature")
plt.show()

plt.subplot(1, 2, 2)

plt.hist(image.ravel(), bins = 256, color = 'orange', )
plt.hist(image[:, :, 0].ravel(), bins = 256, color = 'red', alpha = 0.5)
plt.hist(image[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)
plt.hist(image[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.5)
plt.xlabel('Intensity Value')
plt.ylabel('Count')
plt.legend(['Total', 'Red_Channel', 'Green_Channel', 'Blue_Channel'])

image = images[7]
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(gray,150,200)

#Edges
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.xticks([])
plt.yticks([])
plt.subplot(1, 3, 2)
plt.imshow(gray, cmap="gray")
plt.xticks([])
plt.yticks([])
plt.subplot(1, 3, 3)
plt.imshow(edges, cmap="gray")
plt.xticks([])
plt.yticks([])
plt.show()