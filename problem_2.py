import os


def find_files(suffix = "", path = "."):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files = []
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
    else: 
        new_paths =  os.listdir(path)
        for item in new_paths:
            files += find_files(suffix, "{}/{}".format(path, item))            
    return files


# def find_files_with_loop(suffix, path):
#     files = []
#     paths = []
#     paths.append(path)

#     while len(paths) > 0:
#         path = paths.pop()
#         if os.path.isfile(path):
#             if path.endswith(suffix):
#                 files.append(path)
#         else:
#             new_paths =  os.listdir(path)
#             for item in new_paths:
#                 paths.append("{}/{}".format(path, item))

#     return files


print(find_files('.c', '.'))
#expected output: ['./testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir1/a.c']

print('----------------------------------------')

print(find_files('', '.'))
#expected output: all files in the path
print('----------------------------------------')

print(find_files('.h', '.'))
#expected output: ['./testdir/subdir1/a.h', './testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h']

print('----------------------------------------')
print(find_files('t1.h', '.'))
#expected output: ['./testdir/t1.h']

print('----------------------------------------')
print(find_files('t1.h')) #if a path is not specified, the default is the current directory
#expected output: ['./testdir/t1.h']


print('----------------------------------------')
print(find_files( path= '.')) #if a suffix is not specified it searches for all files
#expected output: all files in the path