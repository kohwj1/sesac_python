# https://docs.python.org/ko/3.10/library/zipfile.html
import os, zipfile #빌트인 모듈 중 압축 시 사용하는 모듈


my_dir = 'sesac1234'

for filename in os.listdir(my_dir):
    file_path = os.path.join(my_dir,filename)
    if os.path.isfile(file_path):
        #print(filename)
        zip_filename = f'{filename}.zip'

        with zipfile.ZipFile(zip_filename, 'w') as zipfile:
            zipfile.write(file_path, arcname=filename)
            print(f'{filename}을 {zip_filename}으로 압축함')
        
        os.remove(file_path)
        print(f'원본 파일 삭제')