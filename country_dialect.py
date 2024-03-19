import csv

file_name = "country_info.txt"

with open(file_name, encoding="utf-8", newline="") as countries_data:
    reader = csv.reader(countries_data, delimiter="|")
    # If we want the reader to parse this data, we have to tell it how the fields are separated.
    # A quick way to do that is to provide a value for the `delimiter` parameter(in this case `|` char is our seperator)
    for row in reader:
        # print(row)
        pass

    # That works and is often a quick way to read a CSV file that uses a different separator.
    # But let's imagine that you've written a program that fetches files from different sources, automatically.
    # You can't examine each file yourself, to check things like the separators being used.
    # We need an automated solution. The CSV module's Sniffer class can help here.
    # It examines a sample of the file, and works out things like the separators, the character
    # used to delimit strings, and so on. It uses that sample to create a Dialect.
    # A Dialect is just all of the various options, grouped together into a single object.

with open(file_name, encoding="utf-8", newline="") as countries_data2:
    sample = countries_data2.read()
    dialect = csv.Sniffer().sniff(sample)
    # Line 22 creates a new Sniffer object, and calls its sniff method. We pass our sample as an argument.
    # we can use read method to create a single string containing all the chars in file
    # We obtained the sample by reading the entire countries_data2 file. (That's not the most efficient way)

    # Because we've read the entire file, there's nothing left for the reader to read. We've reached the end of the file
    # The seek method is used to position the file pointer to another place in the file.
    # Passing zero to seek starts reading from the beginning of the file again.
    countries_data2.seek(0)
    reader = csv.reader(countries_data2, dialect=dialect)
    # we can pass our dialect to the reader as kwarg

    for row in reader:
        # print(row)
        pass

# That's obviously not very efficient, especially with very large files.
# The sniffer only needs a sample of the data. Generally, two or three lines should be sufficient
# When you checked out the documentation for the read and readline methods, you'll have seen the size parameter.
# You can tell both methods how many characters to read (to create a sample for passing as an argument to sniff method)

with open(file_name, encoding="utf-8", newline="") as countries_data2:
    sample = ""
    for i in range(3):
        sample += countries_data2.read()

    dialect = csv.Sniffer().sniff(sample)
    dialect.skipinitialspace = True
    countries_data2.seek(0)
    reader = csv.reader(countries_data2, dialect=dialect)
    for row in reader:
        print(row)

    # dialect :They're basically just a way to group the various CSV settings together, into a single object.
    # We could specify things like the delimiter, escapechar, quotechar, and so on, when we call the reader function.
    # The Dialect lets us set all the values inside a single object, and pass that to the reader– it keeps things tidier

    print('*'*50)

    attributes = ["delimiter",
                  "doublequote",
                  "escapechar",
                  "lineterminator",
                  "quotechar",
                  "quoting",
                  "skipinitialspace",]
    # An attribute is just another name for a value, that's stored inside an object.

    for attribute in attributes:
        print(f"{attribute} : {getattr(dialect, attribute)}")
        # The getattr function is one way to get the value of an attribute.