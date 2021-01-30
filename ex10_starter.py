import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames

# TODO: use os.path.getsize to find each file's size

# TODO: Add a test to only display files that are not zero length

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()

file_list = glob.glob(pattern)
print('file_list {}'.format(file_list))

file_size = os.path.getsize(hdir)
print("The size of the directory is:",file_size,"bytes")

file_removebn = os.path.basename(hdir)
print(file_removebn)


# print('file_size {}'.format(file_size))

# if os.stat(hdir).st_size != 0:
#     print('notzero {}'.format(file_size))

os.path.basename(pattern)