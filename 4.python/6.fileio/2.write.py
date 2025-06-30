# https://docs.python.org/3.10/library/functions.html#open
file_path = 'text.txt'

with open(file_path,'w', encoding='UTF-8') as file:
    file.write('Hello!\n\n') #\n: new line
    file.write('안녕!')
    file.write('\n바이')