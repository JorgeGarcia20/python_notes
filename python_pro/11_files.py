# to open a file with python an do using the best practices, we can use the using statement
# this statement help us closing the file once we don't need more or we have finsh the logic that englobe it
with open('./test.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write('\nNew line\n')
    file.write('another line\n')
    file.write('another one\n')

# if we use a file without indicate a permission, we only have the reading permission
# to have a permission to write in our file, we have to indicate with 'r+'
# if we use a 'w+' all the content in our file going to be deleted to rewrite the file.
# so, we have to be carefull indicating the permissions in our files.