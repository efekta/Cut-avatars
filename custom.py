from PIL import Image

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

#  сохраняем в отдельную переменную каждую черно-белую картинку зеленого канала
image_color_green = green.save("image_color_green.jpg")

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

#  обрезать накладываемую картинку зеленого канала с двух сторон, сохранив миниатюру в переменную
image_color_green = Image.open("image_color_green.jpg")
coordinates = (number / 2, 0, image_color_green.width - number / 2, image_color_green.height)
cropped = image_color_green.crop(coordinates)
cropped_green = cropped.save("image_color_green_duble_2.jpg")

# накладываем картинку на картинку с прозрачностью 0.5
cropped_red_1 = Image.open("image_color_red_duble_1.jpg")
cropped_red_2 = Image.open("image_color_red_duble_2.jpg")
cropped_blue_1 = Image.open("image_color_blue_duble_1.jpg")
cropped_blue_2 = Image.open("image_color_blue_duble_2.jpg")
cropped_green = Image.open("image_color_green_duble_2.jpg")

new_image_red = Image.blend(cropped_red_1, cropped_red_2, 0.5)
new_image_blue = Image.blend(cropped_blue_1, cropped_blue_2, 0.5)

#  сохраняем собранные картинки
new_image_red = new_image_red.save("result_img_red.jpg")
new_image_blue = new_image_blue.save("result_img_blue.jpg")
cropped_green = cropped_green.save("result_img_green.jpg")

#  собираем из 3х картинок одну обратно
new_image_red = Image.open("result_img_red.jpg")
new_image_blue = Image.open("result_img_blue.jpg")
cropped_green = Image.open("result_img_green.jpg")
new_image = Image.merge("RGB", (new_image_red, cropped_green, new_image_blue))

#  сохраняем собранную аватарку
avatar_image = new_image.save("avatar_image.jpg")

# изменить размер картинки
avatar_image = Image.open("avatar_image.jpg")
avatar_image.thumbnail((80, 80))

# сохранить картинку в файл
avatar_image_min = avatar_image.save("avatar_image_min.jpg")
