from PIL import Image
'''
На сколько пикселей смещать канал выберите сами. Самое хорошее решение — создать переменную и записать в неё выбранное число. Если вы передумаете достаточно будет заменить всего одну переменную.
'''
number = 100

#  открыть картинку
image = Image.open("monro.jpg")

#  конвертировать ее в RGB
image = image.convert("RGB")


# В переменные запишутся 3 чёрно-белые картинки.
red, green, blue = image.split()


#  сохраняем в отдельную переменную каждую черно-белую картинку красного канала
image_color_red = red.save("image_color_red.jpg")

#  сохраняем в отдельную переменную каждую черно-белую картинку синего канала
image_color_blue = blue.save("image_color_blue.jpg")


#  обрезать картинку красного канала слева, сохранив миниатюру в переменную
image_color_red = Image.open("image_color_red.jpg")
coordinates = (number, 0, image_color_red.width, image_color_red.height)
cropped = image_color_red.crop(coordinates)
cropped_red_1 = cropped.save("image_color_red_duble_1.jpg")

#  обрезать накладываемую картинку красного канала с двух сторон, сохранив миниатюру в переменную
image_color_red = Image.open("image_color_red.jpg")
coordinates = (number / 2, 0, image_color_red.width - number / 2, image_color_red.height)
cropped = image_color_red.crop(coordinates)
cropped_red_2 = cropped.save("image_color_red_duble_2.jpg")

#  обрезать картинку синего канала слева, сохранив миниатюру в переменную
image_color_blue = Image.open("image_color_blue.jpg")
coordinates = (0, 0, image_color_blue.width - number, image_color_blue.height)
cropped = image_color_blue.crop(coordinates)
cropped_blue_1 = cropped.save("image_color_blue_duble_1.jpg")

#  обрезать накладываемую картинку синего канала с двух сторон, сохранив миниатюру в переменную
image_color_blue = Image.open("image_color_blue.jpg")
coordinates = (number / 2, 0, image_color_blue.width - number / 2, image_color_blue.height)
cropped = image_color_blue.crop(coordinates)
cropped_blue_2 = cropped.save("image_color_blue_duble_2.jpg")




# накладываем картинку на картинку с прозрачностью 0.5
cropped_red_1 = Image.open("image_color_red_duble_1.jpg")
cropped_red_2 = Image.open("image_color_red_duble_2.jpg")
cropped_blue_1 = Image.open("image_color_blue_duble_1.jpg")
cropped_blue_2 = Image.open("image_color_blue_duble_2.jpg")

new_image_red = Image.blend(cropped_red_1, cropped_red_2, 0.5)
new_image_blue = Image.blend(cropped_blue_1, cropped_blue_2, 0.5)



#  сохраняем собранную картинку
new_image_red = new_image_red.save("result_img_red.jpg")
new_image_blue = new_image_blue.save("result_img_blue.jpg")