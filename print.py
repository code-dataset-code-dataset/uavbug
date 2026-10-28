from pathlib import Path


def print_directory_tree(directory_path, prefix=""):
    """
    以树状结构打印指定目录下的所有文件夹。

    :param directory_path: 需要打印的根目录路径
    :param prefix: 用于前缀拼接，递归时内部使用
    """
    path = Path(directory_path)

    # 初次调用时打印根目录名称
    if prefix == "":
        if not path.is_dir():
            print(f"错误: 路径 '{directory_path}' 不是一个有效的文件夹。")
            return
        print(f"📁 {path.name}/")

    try:
        # 获取所有子文件夹并进行排序
        sub_dirs = sorted([p for p in path.iterdir() if p.is_dir()])
    except PermissionError:
        # 忽略没有权限访问的系统文件夹
        return

    # 遍历并打印子文件夹
    for index, sub_dir in enumerate(sub_dirs):
        # 判断是否是当前层级的最后一个文件夹
        is_last = (index == len(sub_dirs) - 1)

        # 选择相应的树枝符号
        connector = "└── " if is_last else "├── "

        # 打印当前文件夹
        print(f"{prefix}{connector} {sub_dir.name}")

        # 为下一级子文件夹准备前缀
        # 如果当前是最后一个，下一级的前缀用空格留白；否则用竖线延续
        extension = "    " if is_last else "│   "

        # 递归调用
        print_directory_tree(sub_dir, prefix + extension)


# ================= 使用示例 =================
if __name__ == "__main__":
    # 请将这里的路径替换为你想要查看的文件夹路径
    # Windows 示例: target_folder = "D:/my_project"
    # Mac/Linux 示例: target_folder = "/Users/username/my_project"

    target_folder = "./Result"  # 默认打印当前运行路径的文件夹结构

    print(f"开始生成 '{target_folder}' 的目录树:\n")
    print_directory_tree(target_folder)