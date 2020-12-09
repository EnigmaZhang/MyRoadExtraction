from PIL import Image, ImageOps
import os
import cv2


def resize_to_square(path, new_size):
    for name in os.listdir(path):
        image = Image.open(path + name)
        new_size = (new_size, new_size)
        image = image.resize(new_size, Image.ANTIALIAS)

        image.save(path + name)


def cut_to_many(path, to_cut):
    name = path + os.listdir(path)[0]
    image = cv2.imread(name)
    image_count = 0
    to_cut_limit = image.shape[0] // to_cut
    print(image.shape)
    for i in range(0, image.shape[0], to_cut_limit):
        for j in range(0, image.shape[1], to_cut_limit):
            new_image = image[i:i + to_cut_limit, j:j + to_cut_limit]
            cv2.imwrite(path + str(image_count) + ".jpg", new_image)
            image_count += 1


path = 'dataset/Atlanta/'
for name in os.listdir(path):
    image = cv2.imread(path + name)
    print(name, image.shape)
if len(os.listdir(path)) == 1:
    resize_to_square(path, 1024 * 8)
    cut_to_many(path, 8)


