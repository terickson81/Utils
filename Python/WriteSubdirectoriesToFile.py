import os

'''
This will write the absolute path of all subdirectories of the current directory to the file subdirectories.txt. You can replace '.' with the path of the directory you want to scan.
'''

def write_subdirectories_to_file(directory_path, file_path):
    with open(file_path, 'w') as file:
        for subdir in os.listdir(directory_path):
            subdir_path = os.path.join(directory_path, subdir)
            if os.path.isdir(subdir_path):
                file.write(os.path.abspath(subdir_path) + '\n')

write_subdirectories_to_file('.', 'subdirectories.txt')

'''
This code uses the os.walk() function to recursively traverse the directory tree and find all subdirectories. The os.walk() function returns a tuple of three values for each directory it visits: the root directory, a list of subdirectories, and a list of files. We only need the subdirectories, so we loop over the dirs list and write the absolute path of each subdirectory to the file.

You can call this function with the directory path and the file path as arguments. For example, if you want to write the subdirectories of the current directory to a file named subdirectories.txt, you can call the function like this:

write_subdirectories_to_file('.', 'subdirectories.txt')
This will write the absolute path of all subdirectories of the current directory to the file subdirectories.txt. You can replace '.' with the path of the directory you want to scan.
'''
def write_subdirectories_to_file_recursive(directory_path, file_path):
    with open(file_path, 'w') as file:
        for root, dirs, files in os.walk(directory_path):
            for subdir in dirs:
                subdir_path = os.path.join(root, subdir)
                file.write(os.path.abspath(subdir_path) + '\n')

write_subdirectories_to_file_recursive('.', 'subdirectoriesrecur.txt')