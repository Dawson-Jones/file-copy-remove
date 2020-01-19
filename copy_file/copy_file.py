import yaml
import os
import shutil
from log_manager import logger


def main():
    try:
        with open('config.yaml') as f:
            dct = yaml.load(f, Loader=yaml.Loader)
    except Exception as e:
        print(e)
    copy_li = dct.get('copy')
    copy_to = dct.get('copy_to')
    if not all([copy_li, copy_to]):
        return print('配置文件出错')
    if not isinstance(copy_li, list):
        return print('配置文件出错')

    for i in copy_li:
        file_name = i.replace('/', '-')
        target_path = os.path.join(dct.get('copy_to'), file_name)
        copy_file(i, target_path, 50)


def copy_file(file: str, target_path, num):
    if num == 0:
        return print(f'复制{file}失败')
    try:
        shutil.copy(file, target_path)
    except FileNotFoundError as e:
        logger.error(e)
        return print(f'{file}文件路径有错')
    except PermissionError:
        return copy_file(file, target_path, num-1)
    except Exception as e:
        logger.error(e)
        return print(f'复制{file}失败')
    print('成功')


if __name__ == '__main__':
    main()
