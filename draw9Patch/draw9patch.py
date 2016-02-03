# coding: utf-8

from PIL import Image, ImageDraw
import os
import LogUtil

generate_type = ['png', 'jpg', 'jpeg', 'bmp']


# 根据文件路径制作简易.9图
def generation(image_path):
    if not check_file_type(image_path):
        LogUtil.log_e('file format error !')
        return
    last_path = get_last_file_name(image_path)
    # print last_path
    org_image = Image.open(image_path)  # 打开原图
    # print org_image.size, org_image.format, org_image.info  # 基本信息输出
    dst_size = map(add_2, org_image.size)  # 新的图尺寸，上下左右向外扩1个像素
    dst_image = Image.new("RGBA", dst_size, (255, 255, 255, 0))  # 生成一张透明图
    dst_image.paste(org_image, (1, 1, dst_size[0] - 1, dst_size[1] - 1))  # 将原图画在透明图上面（居中）
    draw = ImageDraw.Draw(dst_image, "RGBA")  # 构建一张可以画的图
    draw.point([0, 1, 0, dst_size[1] - 2, 1, 0, dst_size[0] - 2, 0], fill=(0, 0, 0, 255))  # 在上面画1像素点
    dst_image.save(last_path)  # 保存.9图片
    LogUtil.log_d(app, last_path + ' save success !')


def add_2(x):
    return x + 2


# 检测文件类型是否是图片格式
def check_file_type(image_path):
    splits = str(image_path).split('.')
    if len(splits) < 2:
        return False
    temp_type = splits[len(splits) - 1]
    return generate_type.count(temp_type) == 1


# 生成新的文件名
def get_last_file_name(image_path):
    splits = str(image_path).split('.')
    if len(splits) >= 2:
        splits[len(splits) - 1] = '9.png'
    last_path = ''
    for j, s in enumerate(splits):
        last_path += s
        if j != len(splits) - 1:
            last_path += '.'
    return last_path


# 遍历一个文件夹下的所有图片
def batch_deal(folder_path, sub_folder=False):
    files = os.listdir(folder_path)
    last_paths = []
    # length = 0
    for file_path in files:
        true_path = os.path.join(folder_path, file_path)
        if check_file_type(true_path):
            need_path = os.path.join(folder_path, true_path)
            last_paths.append(need_path)
            # length += 1
        if os.path.isdir(true_path) and sub_folder:
            ss = batch_deal(true_path, sub_folder)
            last_paths += ss
            # length += ss
    return last_paths


# if __name__ == '__main__':
#     path = '\\Python_project\\Fast9-patch'
#     for i, paa in enumerate(batch_deal(path, True)):
#         print(i, paa)
#         generation(paa)


# 对外函数，可以传入一个文件或这个文件夹，默认不读取子文件夹，对文件或文件夹中的图片做.9操作
def draw_patch(x_app, folder_path, sub_in=False):
    global app
    app = x_app
    try:
        if not os.path.isfile(folder_path) and not os.path.isdir(folder_path):
            LogUtil.log_e('输入的既不是文件也不是文件夹')
            return
        if os.path.isdir(folder_path):
            for index, file_path in enumerate(batch_deal(folder_path, sub_in)):
                # print(index, file_path)
                generation(file_path)
        else:
            generation(folder_path)
    except BaseException, e:
        LogUtil.log_e(e.message)
