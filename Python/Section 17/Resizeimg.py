from PIL import Image

img = Image.open('./Pokedex/pikachu.jpg')
new_img = img.resize((400, 400))
new_img.save('thumbnail.jpg')
