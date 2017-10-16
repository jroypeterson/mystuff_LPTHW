import csv
import requests

with open('../data/vertebral_column_2_categories.dat', 'r') as f:
    vertebral_data = [row for row in csv.reader(f)]

#print the first five elements in vertebral_data
for line in vertebral_data[:5]:
    print(line)
