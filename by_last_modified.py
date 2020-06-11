# importing in-built modules
import os
import shutil
from time import time


def by_last_modified(file_name, dirpath, dist):
    file_path = os.path.join(dirpath, file_name)
    now = time()

    # selecting a directory to move
    if os.stat(file_name).st_mtime > now - 60 * 60 * 24:    # 24 hours
        if not os.path.exists(os.path.join(dist, '24 hours')):
            os.makedirs(os.path.join(dist, '24 hours'))
        shutil.move(file_path, os.path.join(dist, '24 hours'))
    elif os.stat(file_name).st_mtime > now - 60 * 60 * 24 * 2:    # 2 days
        if not os.path.exists(os.path.join(dist, '2 days')):
            os.makedirs(os.path.join(dist, '2 days'))
        shutil.move(file_path, os.path.join(dist, '2 days'))
    elif os.stat(file_name).st_mtime > now - 60 * 60 * 24 * 7:    # 7 days
        if not os.path.exists(os.path.join(dist, '7 days')):
            os.makedirs(os.path.join(dist, '7 days'))
        shutil.move(file_path, os.path.join(dist, '7 days'))
    else:    # older
        if not os.path.exists(os.path.join(dist, 'older')):
            os.makedirs(os.path.join(dist, 'older'))
        shutil.move(file_path, os.path.join(dist, 'older'))
