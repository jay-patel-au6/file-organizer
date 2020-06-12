# File organizer

This is a python project to organize scattered files and/or directories.

## Installation

The repo contains an executable file in dist folder which should be placed in the system such that it can be called globally.

If you need to make a new executable file, go to the directory where this repo is located and type folloing command in terminal. A new executable file will be created in dist directory.

```bash
pyinstaller main.py --onefile
```

Copy the executable file to bin to run it from anywhere.

```bash
cp ./dist/main /bin/organize_files
```

## Usage

```bash
organize_files --help
```

### Positional argument: organize_by

```bash
organize_files <organize_by>
```

Used to set the type by which files/folders are supposed to be organized.
Choices: `by_extension` `by_size` `by_last_modified`

Example:
```bash
organize_files by_size
```

### Optional argument: --src | -S

```bash
organize_files <organize_by> [--src SRC]
```

Used to set the source directory where unorganized files/folders exist. Can take absolute/relative path as value.
Default is set to desktop.

Example:
```bash
organize_files by_size --src ./organize_this_directory
```

### Optional argument: --dist | -D

```bash
organize_files <organize_by> [--dist DIST]
```

Used to make a an existent/non-existent directory as destination where files/folders are organized. Can take absolute/relative path as value.
Default is set to a new(non-existent) directory in desktop.

Example:
```bash
organize_files by_size --dist /home/user_name/work_directory/organized_files
```

### Optional argument: --include_sub_directories | -SUBDIR

```bash
organize_files <organize_by> [--include_sub_directories]
```

Used to state whether or not to include files within sub-directories while organizing the source directories.
Default is false. If it is desired to be made true, it should be included in command without any value.

Example:
```bash
organize_files by_size -SUBDIR
```

### Optional argument: --ignore

```bash
organize_files <organize_by> [--ignore [IGNORE ...]]
```

Used to ignore files/directories from the source directory.
Add space-separated names.

Example:
```bash
organize_files by_size --src ~/work_directory -SUBDIR --ignore imp_file.txt ignore_this_directory
```







