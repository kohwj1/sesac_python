from PIL import Image
from PIL import ImageFilter

image = Image.open('cat1.jpg')
# resized_image = image.resize((80,60))
# resized_image.save('small_cat.jpg')

blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save('blurred_cat.jpg')