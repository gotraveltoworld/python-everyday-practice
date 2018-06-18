import os
files = []
# listdir 列出目錄下的資料，回傳一個串列
def walk(dir_path=''):
    for name in os.listdir(dir_path):
        path = os.path.join(dir_path, name)

        if os.path.exists(path) and os.path.isfile(path):
            files.append(path)
        else:
            walk(path)
