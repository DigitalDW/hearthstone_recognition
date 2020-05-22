import csv
import os

DIRECTORY = "../images/train/"
FILES = os.listdir(DIRECTORY)

with open('./basic_train_labels.csv', newline="\n") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    data = [row for row in reader]

with open('../images/train_labels.csv', "w", newline="\n") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(data[0])
    locations = dict()
    for row in data[1:11]:
        locations[row[0].split("_")[2].replace(".png", "")] = [
            row[4],
            row[5],
            row[6],
            row[7]
        ]
    for filename in FILES:
        if os.path.splitext(filename)[1] == ".png":
            file = filename.split("_")
            number = file[2].replace(".png", "")
            location = locations[number]
            writer.writerow([
                filename,
                861,
                422,
                file[0]+"_"+file[1],
                location[0],
                location[1],
                location[2],
                location[3],
            ])
