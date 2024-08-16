"""
    此代码用于在vps上执行对应的命令
    当文件上传覆盖更新时自动执行(显然这里ebpf是个更好的选择)
    希望执行后你能看到对应的shell
"""
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == file_path and event.is_directory is False:
            print(f"文件 {event.src_path} 已修改")
            self.execute_commands_from_file(event.src_path)

    def execute_commands_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                command = line.strip()
                if command:
                    # 检查命令是否以 /bin/bash 开头
                    if command.startswith('/bin/bash'):
                        try:
                            result = subprocess.run(command, shell=True, check=True)
                            print(f"命令执行成功: {command}")
                        except subprocess.CalledProcessError as e:
                            print(f"命令执行失败: {command}\n错误信息: {e}")
                    else:
                        print(f"跳过非 /bin/bash 命令: {command}")

file_path = './received_output.txt'

if __name__ == "__main__":
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
