from skimage.transform import resize
from skimage.io import imread,imsave

def resizeImage(filepath,filename,fileextension):
    image = imread(f"{filepath}{filename}{fileextension}")
    image_downscaled = resize(image, (256, 256,3))
    imsave(f"{filepath}{filename}resized{fileextension}",image_downscaled)

# exemplo
# resizeImage("","lefishe",".jpg")