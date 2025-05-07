import os
import shutil

def extract_masks_to_new_folder(root_dir, target_dir, mask_name="_Original_Degree.bmp"):
    """
    从指定根目录下的所有子文件夹中提取 _mask.png 文件，并将它们复制到一个新的文件夹。

    :param root_dir: 根目录，所有子文件夹中的 _mask.png 文件将提取到此目录。
    :param target_dir: 新的目标文件夹，所有提取的 _mask.png 文件将存放在此文件夹。
    :param mask_name: 要查找的文件名，默认为 "_mask.png"。
    """
    # 如果目标文件夹不存在，则创建它
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 遍历根目录下的所有子目录及其文件
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(mask_name):
                # 构造文件的完整路径
                source_path = os.path.join(root, file)
                # 目标路径是目标文件夹下，保持文件名不变
                dest_path = os.path.join(target_dir, file)

                # 如果目标路径已经存在，则给文件加个编号防止覆盖
                if os.path.exists(dest_path):
                    base_name, ext = os.path.splitext(file)
                    counter = 1
                    # 防止目标文件名重复
                    while os.path.exists(dest_path):
                        dest_path = os.path.join(target_dir, f"{base_name}_{counter}{ext}")
                        counter += 1

                print(f"复制文件 {source_path} 到 {dest_path}")
                # 复制文件到目标文件夹
                shutil.copy(source_path, dest_path)

# 示例用法
root_dir = r"C:\Users\Administrator\Desktop\shuju1"  # 替换为你的源文件夹路径
target_dir = r"C:\Users\Administrator\Desktop\shujv2024_12_25"  # 替换为你希望存放文件的目标文件夹路径

extract_masks_to_new_folder(root_dir, target_dir)
