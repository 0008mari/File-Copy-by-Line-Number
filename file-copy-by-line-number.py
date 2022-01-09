from itertools import islice
from os import getcwd, chdir

currentPath = getcwd()
chdir(currentPath)

# file copy by lines

print("원본 파일명: ", end='')
filename = input().rstrip()
# print("새로운 파일명: ")
# newfilename = filename[:-4] + "-edit" + ".txt"
print("start line no.: ", end='')
startline = int(input())
print("end line no.: ", end='')
endline = int(input())


file = open(filename, mode = 'rt', encoding="utf-8")


file.seek(0)    # 파일 포인터 초기화
for ignore_line in islice(file, startline-1):
    pass


newfilename = file.readline().rstrip()
newfile = open(newfilename + ".txt", mode = 'wt', encoding="utf-8")

newfile.write(newfilename + "\n")

copylines = endline - startline + 1

for line in file:
    if copylines == 0:
        break
    newfile.write(line)
    copylines -= 1


file.close()
newfile.close()