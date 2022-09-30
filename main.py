import csv
import re

import unidecode


def slugify(text):
    text = unidecode.unidecode(text).lower()
    return re.sub(r'[\W_]+', '-', text)


with open('url.csv', encoding='utf-8') as csv_file, open('seo.csv', 'w', newline='')as csv_out:
    csv_reader = csv.reader(csv_file, delimiter=';')
    csv_writer = csv.writer(csv_out)
    line_count = 0
    separator = ';'
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            csv_writer.writerow(row)
        else:
            print(slugify(row[1]))
            slug=slugify(row[1])
            if slug[-1] == '-': slug = slug[:-1]
            csv_writer.writerow([row[0], row[1], slug])
            #print(row[0])
            #csv_writer.writerow(["Redirect 301 "+row[0]+" "+row[1]])


            line_count += 1
    print(f'Processed {line_count} lines.')
