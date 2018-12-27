import os

def rename_file(filename):
    new_filename = ''
    for letter in filename:
        if not letter.isdigit():
            new_filename += letter
    return new_filename
def rename_files():
    dir_path = '/Users/nsabbour/REDI/udacity_projects/mini_project2/prank'
    file_list = os.listdir(dir_path)
    for filename in file_list:
        new_filename = rename_file(filename)
        os.rename(os.path.join(dir_path, filename ), os.path.join(dir_path, new_filename ))
        print('renamed file', filename, new_filename)


rename_files()