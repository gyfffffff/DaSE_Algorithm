from PIL import Image
import os

## 数据预处理
# 统一图片大小

# 对图片大小不正确的图片resize
path = './lab2-图像压缩/Images/airplane/'
pics = os.listdir(path)
target_size = (256, 256)
for pic in pics:
    image = Image.open(path+pic)
    if image.size != target_size:
        resized_image = image.resize(target_size)
        resized_image.save(path+pic)