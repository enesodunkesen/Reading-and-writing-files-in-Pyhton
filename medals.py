import csv

csv_file_name = "OlympicMedals_2020.csv"

with open(csv_file_name, encoding="utf-8", newline="") as csv_file:
    # when writing a CSV file, if you don't provide an empty string for the newline argument.(especially on macos)
    headers = csv_file.readline().strip("\n").split(",")
    # on line 7 readline iterates over the csv_file object for 1 time and returns data string
    print(headers)
    reader = csv.reader(csv_file)
    # csv.reader() method continues iteration and returns data as lists
    for row in reader:
        print(row)
    print(type(row))

# The numerical values have been parsed as strings, not integers. The reader function has an option that can
# help with that, but unfortunately it only works when string values are surrounded with quotes.
# check read_cereals.py for this case
