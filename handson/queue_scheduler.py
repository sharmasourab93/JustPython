import os
import csv


if __name__ == '__main__':
    content = []
    file_location, file_name = r"file_location", "file_name.csv"

    for file in os.listdir(file_location):
        if file.endswith(".html"):
            print(file)
            content.append(file)

    f = open(file_location+file_name)

    for i in range(0, (len(content)-1), 1):
        writer = csv.writer(file_location+'Book1.csv', 'wb')
        writer.writerows(content[i])

    f.close()
