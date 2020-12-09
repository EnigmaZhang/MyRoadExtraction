import os
import cv2
import numpy as np

path = 'submits/Atlanta/'
if os.path.exists(path + "Atlanta_mask.png"):
    os.remove(path + "Atlanta_mask.png")
example_image = cv2.imread(path + os.listdir(path)[0])
each_size = example_image.shape[0]
final_size = each_size * 8

final_image = np.zeros((final_size, final_size, 3))
names = os.listdir(path)
names.sort(key=lambda x: int(x[:x.find(".")]))
for num, name in enumerate(names):
    now_image = cv2.imread(path + name)
    col_index, row_index = int(num % 8), int(num / 8)
    print(each_size * col_index, each_size * (col_index + 1))
    final_image[each_size * row_index:each_size * (row_index + 1),
                each_size * col_index:each_size * (col_index + 1)] = now_image


cv2.imwrite(path + "Atlanta_mask.png", final_image)
