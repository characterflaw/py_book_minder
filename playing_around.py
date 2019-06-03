#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

# # show Authors
# with open('data/authors.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'Name: {row[1].strip()}, {row[0]}')
#             line_count += 1
#     print(f'Processed {line_count} lines.')

# show Series
with open('data/series.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'ID: {row[0]} - title: {row[1]}')
            line_count += 1
    print(f'Processed {line_count} lines.')


# # show Books
# with open('data/books.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'ID: {row[0]} - title: {row[1]}')
#             line_count += 1
#     print(f'Processed {line_count} lines.')



