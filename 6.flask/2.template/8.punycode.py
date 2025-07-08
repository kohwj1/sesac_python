url = '한글도메인.com'
puny_string = 'https://xn--ob0b5sm6z90a59ugwiskcm3ejviyny.com/'

print(url.encode('puny').decode())
print(puny_string.encode('utf-8'))