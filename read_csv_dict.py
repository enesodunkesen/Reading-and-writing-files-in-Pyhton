# The CSV module provides another couple of classes that can be useful, when parsing or writing CSV files.
# The DictReader works like the reader that we've already used, but produces rows of dictionaries.
#  We can pass the same format options – the delimiter, and so on – to a DictReader as we can for a reader.
# We can also provide a Dialect, to specify all the options in a single object.

import csv

input_file_name = "cereal_grains.csv"

with open(input_file_name, encoding="utf-8", newline="") as cereals_file:
    reader = csv.DictReader(cereals_file)
    for row in reader:
        # print(row)
        pass
    # The keys are the column headings(first row in file), and the values are the corresponding values for each row.


# The DictReader automatically reads the column names from the CSV file it's reading,
# and uses those names for the individual dictionary keys.But what happens if the file doesn't contain column headings?
# There must be some way to provide the keys, if they're not in a header row in the file.
# And we also need to provide the keys when using a DictWriter to create a CSV file.
# We can pass a list, containing the keys, to these objects, in the fieldnames argument.

dialect = csv.excel
dialect.delimiter = "|"
# Dialect objects can't be created in the usual way. The documentation says that the class "must be subclassed"
# What we can do, is use one of the dialects that's included in the CSV module, and modify it.

with open("country_info.txt", encoding="utf-8", newline="") as country_data_file:

    countries = dict()
    headings = country_data_file.readline().strip("\n").split(dialect.delimiter)
    for index in range(len(headings)):
        headings[index] = headings[index].casefold()

    reader = csv.DictReader(country_data_file, dialect=dialect, fieldnames=headings)
    # DictReader and DictWriter objects accept a fieldnames argument.
    # That's optional with a DictReader, if the first line of the file contains the column headings.
    # If it doesn't, you'd have to provide a list containing the column headings – or field names.

    for row in reader:
        countries[row["country"].casefold()] = row
        countries[row["cc"].casefold()] = row


while True:
    try:
        answer = input("Please enter a country name\n--> ").casefold()
        if answer == 'quit':
            break
        country_name = countries[answer]["country"]
        country_capital = countries[answer]["capital"]
        print(f"{country_name}'s capital is {country_capital}")
    except KeyError:
        print("That's not a valid country name")
