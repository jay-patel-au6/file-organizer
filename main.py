#!/usr/bin/python3

# importing in-built modules
import argparse
import os

# importing local modules
from organizer import organizer
from timestr import timestr

print(os.getcwd())

# getting path of desktop
desktop = os.path.join(os.path.join(os.environ.get('HOME')), 'Desktop')

# setting argparse
parser = argparse.ArgumentParser(prog='organize_files', description='''
This is a small setup to organize and manage files.
''')

# adding positional arguments
parser.add_argument('organize_by', type=str, choices=['by_extension', 'by_size', 'by_last_modified'], metavar='ORGANIZE_BY', help='''
Used to set the type by which files/folders are supposed to be organized.
Enter one of the following: by_extension, by_size, by_last_modified.
''')

# adding optional arguments
parser.add_argument('--src', '-S', type=str, metavar="SRC", default=desktop, help='''
Used to set the source directory where unorganized files/folders exist.
Can take absolute/relative path as value.
Default is set to desktop.
''')

parser.add_argument('--dist', '-D', type=str, metavar='DIST', default=os.path.join(desktop, "organized at " + timestr), help='''
Used to make a new(non-existent) directory as destination
where files/folders are organized.
Can take absolute/relative path as value.
Default is set to a new(non-existent) directory in desktop.
''')

parser.add_argument('--include_sub_directories', '-SUBDIR', default=False, action='store_true', help='''
Used to state whether or not to include files within sub-directories
while organizing the source directories.
Default is false.
If it is desired to be made true,
it should be included in command without any value.
''')

parser.add_argument('--ignore', type=str, metavar='IGNORE', nargs='+', help='''
Used to ignore files/directories from the source directory.
Add space-separated names.
''')

args = parser.parse_args()

if args.src[0] == '.':
    args.src = args.src[1:]
    args.src = os.getcwd() + args.src

if args.dist[0] == '.':
    args.dist = args.dist[1:]
    args.dist = os.getcwd() + args.dist

if __name__ == "__main__":
    print(
        '\norganize_by:', args.organize_by,
        '\nsrc:', args.src,
        '\ndist:', args.dist,
        '\nignore:', args.ignore,
        '\ninclude_sub_directories:', args.include_sub_directories, '\n'
    )
    organizer(
        args.organize_by,
        args.src,
        args.dist,
        args.ignore,
        args.include_sub_directories
    )
