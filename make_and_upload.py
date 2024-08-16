"""
    此文件用于处理记录的数据，并将数据上传至vps
"""

import re
import requests

def extract_content_from_file(file_path):
    log_prefix_pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} - \w+ - \w+ - \d+ - \[.*\] - finddatadata:'

    content = ""
    matches = []

    # 使用正则表达式匹配两个美元符号之间的内容
    pattern = r'\$(.*?)\$'

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            cleaned_line = re.sub(log_prefix_pattern, '', line.strip())

            content += cleaned_line

            match = re.search(pattern, content, re.DOTALL)
            if match:
                matches.append(match.group(1))
                content = ""

    return matches
file_path = './response.log'
output_file_path = './output.txt'
extracted_contents = extract_content_from_file(file_path)

if extracted_contents:
    with open(output_file_path, 'w') as output_file:
        for index, content in enumerate(extracted_contents, start=1):
            output_file.write(f"{content}\n")  # 写入内容并换行
else:
    print("No content found.")

# def upload_file(file_path, server_url):
#     with open(file_path, 'rb') as file:
#         files = {'file': (file_path, file)}
#         response = requests.post(server_url, files=files)
#
#         if response.status_code == 200:
#             print("文件上传成功")
#         else:
#             print(f"文件上传失败，状态码: {response.status_code}")
#
# output_file_path = '/output.txt'
# server_url = '192.168.....'
# upload_file(output_file_path, server_url)