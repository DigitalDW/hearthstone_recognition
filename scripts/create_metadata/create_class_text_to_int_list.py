import os
import json

labels = os.listdir("../../images/test/")
labels_list = list()
for label in labels:
    if os.path.splitext(label)[1] == ".png":
        label_info = label.split("_")
        image_id = label_info[0] + "_" + label_info[1]
        if image_id not in labels_list:
            labels_list.append(image_id)

labels_dict = dict()
for i in range(len(labels_list)):
    labels_dict[labels_list[i]] = i + 1

with open("./class_text_to_int.json", "w") as f:
    json.dump(labels_dict, f)
