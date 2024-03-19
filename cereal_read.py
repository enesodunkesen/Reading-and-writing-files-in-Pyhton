# CSV files are much easier to work with, if all strings are quoted.
# Unfortunately, they often aren't.
import csv

csv_filename = 'cereal_grains.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    # We provide a value for the quoting argument, instructing the reader function how the data has been quoted.
    # QUOTE_NONNUMERIC tells it that all non-numeric values have been quoted – which is the case, with this dataset
    for row in reader:
        print(row)
# But it does have some limitations. The main limitation is that it only works with
# data that has all string values quoted. The other problem is that the numerical
# values are all floats. That's probably fine, most of the time, but is something to be aware of.
# If you need integer values to be converted to ints (not floats), then you can't use this approach.

# check https://docs.python.org/3/library/csv.html for more
