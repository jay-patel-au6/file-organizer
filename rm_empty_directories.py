# importing in-built modules
import os


def rm_empty_directories(src, ignore, include_sub_directories):
    for dirpath, dirnames, _ in os.walk(src, topdown=True):
        # removing unwanted dirnames
        if include_sub_directories is True:
            dirnames[:] = [d for d in dirnames if d not in ignore]
        else:
            dirnames[:] = []

        if not os.listdir(dirpath):
            os.rmdir(dirpath)
            rm_empty_directories(src, ignore, include_sub_directories)
