import scipy.ndimage
import scipy.misc

path = '/home..../1/'
img = scipy.misc.imread(path+'1.bmp') #load the image
img_med = scipy.ndimage.median_filter(img,3) #apply median filter
img_sob = scipy.ndimage.sobel(img_med) #apply Sobel filter
scipy.misc.imsave(path+'1_sob.bmp',img_sob) #save the image
