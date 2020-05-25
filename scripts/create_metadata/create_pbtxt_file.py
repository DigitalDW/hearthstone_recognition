import json

with open("class_text_to_int.json") as f:
    data = json.load(f)

with open('../../training/labelmap.pbtxt', 'w') as pbtxt_file:
    for key, value in data.items():
        pbtxt_file.write('item {\n')
        pbtxt_file.write('\tid: {}\n'.format(int(value)))
        pbtxt_file.write("\tname: '{0}'\n".format(str(key)))
        pbtxt_file.write('}\n\n')
