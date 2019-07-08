from PIL import Image
'''
На сколько пикселей смещать канал выберите сами. Самое хорошее решение — создать переменную и записать в неё выбранное число. Если вы передумаете достаточно будет заменить всего одну переменную.
'''
number = 86

#  открыть картинку
image = Image.open("monro.jpg")

#  конвертировать ее в RGB
image = image.convert("RGB")


# В переменные запишутся 3 чёрно-белые картинки.
red, green, blue = image.split()

#  создаем кортеж и кладем в него 3 переменные с 3мя черно-белыми картинками
images = (red, green, blue)

#  сохраняем в отдельную переменную каждую черно-белую картинку
image_color_red = images[0].save("image_color_red.jpg")

#  обрезать картинку на 60 слева, сохранив миниатюру в переменную
image_color_red = Image.open("image_color_red.jpg")
coordinates = (number, 0, image_color_red.width, image_color_red.height)
cropped = image_color_red.crop(coordinates)
cropped_1 = cropped.save("image_color_red_duble_1.jpg")

#  обрезать накладываемую картинку с двух сторон по 30, сохранив миниатюру в переменную
image_color_red = Image.open("image_color_red.jpg")
coordinates = (number / 2, 0, image_color_red.width - number / 2, image_color_red.height)
cropped = image_color_red.crop(coordinates)
cropped_2 = cropped.save("image_color_red_duble_2.jpg")

# накладываем картинку на картинку с прозрачностью 0.5
cropped_1 = Image.open("image_color_red_duble_1.jpg")
cropped_2 = Image.open("image_color_red_duble_2.jpg")
new_image = Image.blend(cropped_1, cropped_2, 0.5)


#  сохраняем собранную картинку
new_image = new_image.save("result_img.jpg")
#  собираем из 3х картинок одну обратно
# new_image = Image.merge("RGB", (red, green, blue))

