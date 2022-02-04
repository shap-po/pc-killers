from shutil import copyfile

MEMORY = 1  # file size in gb
FILE_COUNT = 1


text = "1"*int(1050000*1024*MEMORY)
with open('1', "w") as f:
    f.write(text)
del text
for i in range(FILE_COUNT-1):
    copyfile('1', str(i+2))
