# import pandas as pd
# import numPy

from csv import reader

open_file = open('covid_19_data.csv')
read_file = reader(open_file)
file_data = list(read_file)

print(file_data[:5][0])
print(file_data[:5][1])
print(file_data[:5][2])
