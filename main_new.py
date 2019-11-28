import os
import re
import shutil
import imghdr
from random import randint
from multiprocessing import Process
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from contans import PATH_A, PATH_C, PATH_B, RATE


class FileCopy(FileSystemEventHandler):
    def __init__(self):
        super().__init__()

    def on_created(self, event):
        if event.is_directory:
            return
        path = event.src_path
        print('路径: ', path)
        pic_name = os.path.split(path)[-1]  # 123579_A1H1.jpg
        ret = re.match(r'(.+)_.*\.', pic_name)
        if ret and imghdr.what(path) == 'jpeg':
            target_folder = os.path.join(PATH_C, ret.group(1))
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            shutil.copy(path, target_folder)


class FileRemove(FileSystemEventHandler):
    def __init__(self):
        super().__init__()

    # /home/ubuntu/Pictures/B/20191101/day/ok
    def on_created(self, event):
        if event.is_directory:
            return
        path = event.src_path

        ret = re.match(r'.*[Oo][Kk][/\\]([^/\\]+)\.', path)
        # ret = re.match(r'.*/[Oo][Kk][/\\]([^/]+)\.', '/home/ubuntu/Pictures/B/20191101/day/ok/12312.jpg')
        # ret = re.match(r'.*/[Oo][Kk][/\\]([^/]+)\.', '/home/ubuntu/Pictures/B/ok/day/ng/12312.jpg')
        # if 'ok' in path.lower():
        if ret and imghdr.what(path) == 'jpeg':
            num = randint(1, 100)
            if num <= RATE:
                target_folder = os.path.join(PATH_C, ret.group(1))
                if os.path.exists(target_folder):
                    shutil.rmtree(target_folder)


def watch_file(src_path, file_handler):
    observer = Observer()
    event_handler = file_handler()
    observer.schedule(event_handler, src_path, True)
    observer.start()
    observer.join()


if __name__ == '__main__':
    copy_pic = Process(target=watch_file, args=(PATH_A, FileCopy))
    del_pic = Process(target=watch_file, args=(PATH_B, FileRemove))
    copy_pic.start()
    del_pic.start()
