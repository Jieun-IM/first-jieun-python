import numpy as np

img_path = 'elephant.jpg'
img = image.load_img(img_path, target_size=(224, 224))
print(type(img))

#Temporarily Check
tmp = np.asarray(img)
print(tmp.shape)