# importing in-built modules
import os
import shutil


def by_extension(file_name, dirpath, dist):
    extension = file_name.split('.')[-1]
    file_path = os.path.join(dirpath, file_name)
    if not os.path.exists(os.path.join(dist, extension)):
        os.makedirs(os.path.join(dist, extension))
    shutil.move(file_path, os.path.join(dist, extension))
