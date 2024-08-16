"""
    利用flask框架实现的简单数据接受demo
"""

from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# 设置文件大小限制 (例如：1MB)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 1MB

@app.route('/upload', methods=['POST'])
def upload_file():
    # 获取文件
    file = request.files.get('file')
    if not file:
        return jsonify({'error': '未找到文件'}), 400

    # 检查文件类型
    if not file.filename.endswith('.txt'):
        return jsonify({'error': '文件类型不正确，仅支持 .txt 文件'}), 400

    # 保存文件
    file_path = './received_output.txt'
    file.save(file_path)

    return jsonify({'message': '文件接收成功'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
