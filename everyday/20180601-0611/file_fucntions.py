file_name = 'words_ex1~' # <= Error file name
try:
    content = open(file_name, 'r', encoding='utf-8')
    for line in content:
        print(line)

except IOError as io_err:
    print(io_err) # Output the exception message
    # [Errno 2] No such file or directory: 'words_ex1~'

# You can use 'with' statement
with open(file_name, 'r', encoding='utf-8') as content:
    for line in content:
        print(line)
# [Errno 2] No such file or directory: 'words_ex1~'

