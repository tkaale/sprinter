import csv
import os

DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']

def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list


def write_user_story(user_list, filename):
    count = len(get_all_user_story(filename))
    user_list.insert(0, count + 1)
    with open(filename, "a", newline='') as csvfile:
        fieldnames = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, user_list))
        writer.writerow(to_write)
    print(writer)
        
def change_user_story(filename, user_list):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == user_list[0]:
            line['title'] = user_list[1]
            line['user_story'] = user_list[2]
            line['acceptance_criteria'] = user_list[3]
            line['business_value'] = user_list[4]
            line['estimation'] = user_list[5]
            line['status'] = user_list[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})
