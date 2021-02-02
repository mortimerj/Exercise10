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


# Question 1.5 - I amended the print command to make it simpler - it seems to do the same thing!

file_list = glob.glob(pattern)
# print('file_list {}'.format(file_list))
print(file_list)


#  Question 1.6 - commented out our saturday attempt so you can still see it and added my version below.

# file_size = os.path.getsize(hdir)
# print("The size of the directory is:",file_size,"bytes")

for files in file_list:
    file_size = os.path.getsize(files)
    print(file_size)


# Question 1.7 - not attempted on saturday
for files in file_list:
    file_size = os.path.getsize(files)
    if file_size != 0:
        print(file_size)


# Question 1.8 - commented out our staturday attempts and added my version below

# file_removebn = os.path.basename(hdir)
# print(file_removebn)

# print('file_size {}'.format(file_size))

# if os.stat(hdir).st_size != 0:
#     print('notzero {}'.format(file_size))

# os.path.basename(pattern)

for files in file_list:
    print(os.path.basename(files))