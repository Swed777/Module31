import os


def gen_dir_path(dir_name: str, root_path: str = os.path.abspath(os.sep)):
    for root, dirs, files in os.walk(root_path):
        if root.endswith(dir_name):
            print(root)
            return

        yield root

        for file_name in files:
            yield os.path.join(root, file_name)


for i in gen_dir_path(dir_name="01_scary_code", root_path="../../../Python_Basic"):
    print(i)

# зачтено
