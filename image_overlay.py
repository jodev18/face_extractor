from PIL import Image

mico_img = Image.open("result/mico.jpeg")
mark_img = Image.open("result/mark.jpg")
target_img = Image.open("target.jpg")

target_img.paste(mico_img, (0,0))
target_img.paste(mark_img, (500,0))
#target_img.show()

target_img.save("merged.png")
