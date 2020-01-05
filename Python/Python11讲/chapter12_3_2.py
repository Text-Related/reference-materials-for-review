import matplotlib.pyplot as plt
from PIL import Image
  
def show_image(img):
    fig = plt.figure() 
    out = img
    w,h = out.size 
    for i in range(1,5):
    	ax = fig.add_subplot(2,3,i)
    	ax.imshow(out)
    	ax.set_title('size: {0}*{1}'.format(w,h))
    	w = w//2
    	h = h//2
    	out = out.resize((w, h))

    rot = 45
    for i in range(5,7):
    	im = img
    	ax = fig.add_subplot(2,3,i)
    	im = im.rotate(rot) 
    	ax.imshow(im)
    	ax.set_title('rotate: {0}'.format(rot))
    	rot += 45
    plt.show()

im = Image.open(r'Tulips.jpg')
show_image(im)
 