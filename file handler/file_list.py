# 디렉터리의 현재 파일과 디렉터리 리스트 보여주기
import os

# data = os.listdir('c:\\')
# \는 특별하게 쓰이기 때문에 /를 사용하거나 \\를 사용한다.
data = os.listdir('.')
data = os.listdir('..')
data = os.listdir('my_directory')

for d in data:
    print(d)
    print('is directory? : ' + str(os.path.isdir(d)))
    print('is file? : ' + str(os.path.isfile(d)))