# Deep-Learning-Final
## Dataset:
with_mask: image of a person wearing a mask.\\
without_mask: image of a person without a mask.\\
de-mask: image of a person whose mask is transformed to blank.
mask: image of a mask corresponding to the original masked face.
generated_fig: generated images from de-mask.

## Files:
Data_preparation_&_facenet_baseline.ipynb is how we generated input data for GAN from the kaggle dataset.
facenet file contains facenet.py which is the facenet model.
facenet_result.ipynb can get the face recognition result through facenet. The density plots of both original mask images and generated images are also included.
GAN.ipynb is our main model. Through it we generate face under the mask of the images.
