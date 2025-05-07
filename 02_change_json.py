import os
import json


def convert_json_to_txt(input_folder, output_folder):
    """
    将文件夹中的 JSON 文件转换为 TXT 文件并保存到另一个文件夹中。

    参数：
        input_folder (str): 包含 JSON 文件的文件夹路径。
        output_folder (str): 保存 TXT 文件的目标文件夹路径。
    """
    # 确保目标文件夹存在，如果不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            input_file_path = os.path.join(input_folder, filename)

            # 读取 JSON 文件
            with open(input_file_path, 'r', encoding='utf-8') as json_file:
                try:
                    data = json.load(json_file)  # 尝试解析 JSON 数据
                except json.JSONDecodeError as e:
                    print(f"解析 JSON 文件 {filename} 时出错: {e}")
                    continue

            # 将 JSON 数据转换为字符串
            txt_content = json.dumps(data, indent=4, ensure_ascii=False)

            # 定义输出文件的路径
            txt_filename = f"{os.path.splitext(filename)[0]}.txt"
            output_file_path = os.path.join(output_folder, txt_filename)

            # 将内容写入 TXT 文件
            with open(output_file_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(txt_content)

            print(f"已转换: {filename} -> {txt_filename}")


# 示例用法
input_folder = r"C:\Users\Administrator\Desktop\shujv_json"  # 将此处替换为你的输入文件夹路径
output_folder = r"C:\Users\Administrator\Desktop\shujv_txt"  # 将此处替换为你的目标文件夹路径
convert_json_to_txt(input_folder, output_folder)
