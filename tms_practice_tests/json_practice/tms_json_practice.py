# 1. Прочитать файлик HW_Files.txt
# 2. Преобразовать его в json, где имя ключ, значение - фамилия
# 3. Записать в файлик json с сортировкой по ключ


import json

new_dict = {}

with open('HW_Files.txt', 'r', encoding='utf-8') as f:
    value = f.read().replace('\n', ' ')
    for v in value.split():
        value_for_dict = v.split(',')
        new_dict[value_for_dict[0]] = value_for_dict[1]
    print(new_dict)

with open('test_file.json', 'w',encoding='utf-8') as new_file:
    json.dump(new_dict, new_file,ensure_ascii=False,indent=4,sort_keys=True=)
