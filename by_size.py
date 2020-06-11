# importing in-built modules
import os
import shutil


def by_size(file_name, dirpath, dist):
    size = os.stat(file_name).st_size
    file_path = os.path.join(dirpath, file_name)

    # selecting a directory to move
    if size <= 1024:    # <= 1 KiB
        if not os.path.exists(os.path.join(dist, '1 KiB')):
            os.makedirs(os.path.join(dist, '1 KiB'))
        shutil.move(file_path, os.path.join(dist, '1 KiB'))
    elif size <= 1024 * 100:    # <= 100 KiB
        if not os.path.exists(os.path.join(dist, '100 KiB')):
            os.makedirs(os.path.join(dist, '100 KiB'))
        shutil.move(file_path, os.path.join(dist, '100 KiB'))
    elif size <= 1024 ** 2:    # <= 1 MiB
        if not os.path.exists(os.path.join(dist, '1 MiB')):
            os.makedirs(os.path.join(dist, '1 MiB'))
        shutil.move(file_path, os.path.join(dist, '1 MiB'))
    elif size <= 1024 ** 2 * 10:     # <= 10 MiB
        if not os.path.exists(os.path.join(dist, '10 MiB')):
            os.makedirs(os.path.join(dist, '10 MiB'))
        shutil.move(file_path, os.path.join(dist, '10 MiB'))
    elif size <= 1024 ** 2 * 100:     # <= 100 MiB
        if not os.path.exists(os.path.join(dist, '100 MiB')):
            os.makedirs(os.path.join(dist, '100 MiB'))
        shutil.move(file_path, os.path.join(dist, '100 MiB'))
    elif size <= 1024 ** 3:     # <= 1 GiB
        if not os.path.exists(os.path.join(dist, '1 GiB')):
            os.makedirs(os.path.join(dist, '1 GiB'))
        shutil.move(file_path, os.path.join(dist, '1 GiB'))
    else:
        if not os.path.exists(os.path.join(dist, 'larger')):
            os.makedirs(os.path.join(dist, 'larger'))
        shutil.move(file_path, os.path.join(dist, 'larger'))
