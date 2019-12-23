import re
import ftplib
import socket
from ftplib import FTP
from log_manager import logger
import os

ftp = FTP()


def clean_ftp(address, user=None, pwd=None):
    ret = re.match(r'ftp://(((2[0-4]\d|25[0-5]|\d?\d|1\d{2})\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)):(\d{0,5})(/.*)?$',
                   address)
    if not ret:
        logger.error("Wrong address")
        return
    host = ret.group(1)
    port = int(ret.group(5))
    path = ret.group(6)

    if path:
        path = path[1:]
        if path[-1] == '/':
            path = path[:-1]

    try:
        ftp.connect(host=host, port=port, timeout=10)
        logger.info("login successful: {}".format(ftp.welcome))
    except (socket.error or socket.gaierror) as e:
        logger.error("con't access {} ftp server!!! {}".format(host, e))

    try:
        ftp.login(user, pwd)
    except ftplib.error_perm as e:
        logger.error("Wrong account or password, code: {}".format(e))
        return

    ftp_rm_tree(path)
    # dir_list = ftp.nlst(path)
    # remove_file(dir_list)


# def remove_file(files):
#     for file in files:
#         try:
#             ftp.delete(file)
#             logger.info("delete %s successful" % file)
#         except Exception as e:
#             logger.error("delete {} failed wrong info: {}".format(file, e))


def ftp_rm_tree(path):
    """Recursively delete a directory tree on a remote server."""
    wd = ftp.pwd()

    try:
        names = ftp.nlst(path)
    except ftplib.all_errors:
        return

    for name in names:
        if os.path.split(name)[1] in ('.', '..'): continue

        logger.debug('FtpRmTree: Checking {0}'.format(name))
        try:
            ftp.cwd(name)  # if we can cwd to it, it's a folder
            ftp.cwd(wd)  # don't try a nuke a folder we're in
            ftp_rm_tree(name)
        except ftplib.all_errors:
            ftp.delete(name)

    try:
        ftp.rmd(path)
    except ftplib.all_errors as e:
        logger.debug('FtpRmTree: Could not remove {0}: {1}'.format(path, e))


if __name__ == '__main__':
    clean_ftp("ftp://192.168.1.8:21/opt_pic/", 'ELUpload', 'jink0s0l@rel')
