from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
#filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert('L')
crooked = filtered_img.rotate(90)
#filtered_img.save("blur.png", 'png')
#filtered_img.save("grey.png", 'png')
#filtered_img.show()
crooked.save("grey.png", 'png')
crooked.show()