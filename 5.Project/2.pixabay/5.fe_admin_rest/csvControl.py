import os
import csv

UPLOAD_FOLDER = r'static/img'

def get_images():
    images = []
    os_list = os.listdir(UPLOAD_FOLDER)
    with open(r'static/images.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['filename'] in os_list:
                images.append(row)
    return images

def add_to_csv(filename):
    with open(r'static/images.csv', 'a', newline='\n', encoding='UTF-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([filename, 'keyword'])
    return True

def set_keywords(target, new_keyword):
    temp_list = get_images()
    for row in temp_list:
        if row['filename'] == target:
            row['keyword'] = new_keyword

    with open(r'static/images.csv', 'w', newline='', encoding='UTF-8') as file:
        csv_writer = csv.DictWriter(file, fieldnames=['filename','keyword'])
        csv_writer.writeheader()
        for row in temp_list:
            csv_writer.writerow(row)
