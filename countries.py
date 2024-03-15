import sys

countries = dict()

with open("country_info.txt","r") as country_file:
    country_file.readline()
# Our country_file object is iterable. Each time you use the readline method to read a line,
# the iterator automatically moves on to the next item. That's the next line, in this case.
# So our for loop, on line 9, starts with the second line of the file – because we've already read the
# first line, on line 4
    for row in country_file:
        data = row.rstrip('\n').split(sep="|")
        country, capital, code, code3, dialing, timezone, currency = data # another example of unpacking
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        countries[country.casefold()] = country_dict  # remember how to add key value pairs in a dict
        countries[code.casefold()] = country_dict

# There's no reason why values, in a dictionary, can't have more than one key. We can add another
# key to the countries dictionary, and give it the same value as the country name.
# The countries dictionary now contains two references to the dictionaries for each country.
# One with the country name as the key, and another with the country code as the key.
# Note that the individual country dictionaries are not duplicated.
# As we saw in the last section, countries is storing references to the individual dictionaries.

while True:
    try:
        answer = input("Please enter the name of country\n--> ").casefold()
        if answer == 'quit':
            sys.exit()

        name = countries[answer]['name']
        capital = countries[answer]['capital']
        print(f"{name}'s capital is {capital}")
    except KeyError:
        print("Sorry that's not a valid country")
