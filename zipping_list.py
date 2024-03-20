import csv

# DictWriter needs dictionaries to write to the CSV file.
# But what if your data isn't in dictionaries? You might have a list of lists, # or a list of tuples.

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

keys = ["album", "artist", "year"]

# use a writer,if you wanted to store this data in a CSV file.DictWriter is useful when the data's already in a dictionary
# If you wanted column headings in the first row, you can create a list, and use the CSV writer to write that row first:
# It would be easy to write this data using the CSV writer.

for row in albums:
    zip_object = zip(keys, row)
    print(zip_object)
    for tuple in zip_object:
        print(f"\t{tuple}")

# Python comes with very powerful commands for transforming data. One command is the zip function,
# You pass iterables to it, and it returns an iterable containing tuples.
# The zip function zips together the two iterables – a list and a tuple in this case – and creates
# tuples containing each item from each iterable.
# If you provide two lists, for example, each tuple will contain two items – one from each list, in turn.

with open("albums.csv", "w", encoding="utf-8", newline="") as output_file:
    writer = csv.DictWriter(output_file, fieldnames=keys)
    writer.writeheader()
    for row in albums:
        zip_object = zip(keys, row)
        albums_dict = dict(zip_object)
        writer.writerow(albums_dict)
# we can pass an iterable of key/value pairs to the dict function,to create a dictionary. Our zip objects are iterables,
# containing key/value pairs. That's exactly what we need, if we want to transform our data into a list of dictionaries.
