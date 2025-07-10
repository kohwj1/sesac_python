import csv

def get_all_list():
    with open('todo.csv', 'r', encoding='UTF-8') as file:
        csv_reader = csv.reader(file)
        my_todolist = [{'idx':int(row[0]), 'status':row[1], 'content':row[2]} for row in csv_reader]
        my_todolist.sort(key=lambda x: x['idx'])
    return my_todolist

def delete_todo(idx):
    before_list = get_all_list()
    after_list = [item for item in before_list if item['idx'] != int(idx)]
    # print(after_list) 
    
    with open('todo.csv', 'w', encoding='UTF-8', newline='\n') as file:
        csv_writer = csv.writer(file)
        for item in after_list:
            csv_writer.writerow([item['idx'], item['status'], item['content']])
    return True

def add_todo(content):
    new_idx = int(get_all_list()[-1]['idx']) + 1
    with open('todo.csv', 'a', encoding='UTF-8', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([new_idx, '', content])
    return True

def switch_todo(idx):
    for item in get_all_list():
        if item['idx'] == int(idx):
            target = item
            break
    
    content = target['content']
    before_status = target['status']

    delete_todo(idx)

    if before_status  == 'checked':
        new_status = ''
    else:
        new_status = 'checked'

    with open('todo.csv', 'a', encoding='UTF-8', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([idx, new_status, content])
    return True