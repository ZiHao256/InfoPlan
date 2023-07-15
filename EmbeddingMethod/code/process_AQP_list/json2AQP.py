import json
import os


if __name__ == '__main__':

    print("input the name of txt(with out .txt)")
    input_file_name = input()

    input_path = os.path.abspath('.') + '/input/'+input_file_name+'.txt'


    txt_content_str = "["

    f = open(input_path)  # 打开文件
    iter_f = iter(f)  # 创建迭代器
    for line in iter_f:  # 遍历文件，一行行遍历，读取文本
        txt_content_str += line + ','
    txt_content_str = txt_content_str[:-1]
    txt_content_str += ']'

    # 解析JSON文件的str格式为dict和list

    output_path = os.path.abspath('.') + '/output/'+input_file_name+'.json'
    w_file_AQP_json = open(output_path, 'w')
    w_file_AQP_json.write(txt_content_str)
