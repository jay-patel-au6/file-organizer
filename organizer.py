# importing in-built modules
import os

# importing local modules
from by_size import by_size
from by_extension import by_extension
from by_last_modified import by_last_modified
from rm_empty_directories import rm_empty_directories


def organizer(organize_by, src, dist, ignore, include_sub_directories):
    os.makedirs(dist)

    if not os.path.exists(src):
        return print('source directory does not exist!')

    if ignore is None:
        ignore = list()     # making an empty list of ignore if it is None
    ignore.append(os.path.basename(dist))

    # seeing all files
    for dirpath, dirnames, filenames in os.walk(src, topdown=True):
        # removing unwanted dirnames
        if include_sub_directories is True:
            dirnames[:] = [d for d in dirnames if d not in ignore]
        else:
            dirnames[:] = []
        filenames[:] = [f for f in filenames if f not in ignore]

        os.chdir(dirpath)

        for f in filenames:
            print('Moving', f, 'from', dirpath)
            # selecting type
            if organize_by == 'by_size':
                by_size(f, dirpath, dist)
            elif organize_by == 'by_extension':
                by_extension(f, dirpath, dist)
            elif organize_by == 'by_last_modified':
                by_last_modified(f, dirpath, dist)

    rm_empty_directories(src, ignore, include_sub_directories)
