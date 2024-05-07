from PIL import Image

# 打开图像文件
image = Image.open('linux.png')

# 将图像转换为灰度图像
gray_image = image.convert('L')

# 获取图像的宽度和高度
width, height = gray_image.size

# 打印每个像素的灰度值
for y in range(height):
    for x in range(width):
        pixel_value = 8 - round(gray_image.getpixel((x, y)) / 32)
        print(f'{pixel_value},', end='')
    print('')

# 关闭图像文件
image.close()
