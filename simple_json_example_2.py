import json
languages = [
    ('ABC', 1987),
    ('Algol 68', 1968),
    ('APL', 1962),
    ('C', 1973),
    ('Haskell', 1990),
    ('Lisp', 1958),
    ('Modula-2', 1977),
    ('Perl', 1987),
]
# this time we'll be serializing a list of tuples.

with open("test.json", 'w', encoding='utf-8') as serialization:
    json.dump(languages, serialization)

with open("test.json", 'r', encoding='utf-8') as deserialization:
    data = json.load(deserialization)

print(type(languages))
print(type(data))
# And we get back a list of lists. The JSON format doesn't support tuples.
# That's not surprising; many languages don't even have tuples, so they'd be unable to parse them out of the JSON text.
#  Remember that JSON is a format for exchanging data. As long as you can get the data in a form that you can work with,
# in your code,then it's serving its purpose. JSON has to be language independent,
# otherwise it wouldn't be an open standard that can be used with any language.
# That means it can only support objects that are common in all languages.

# for details check https://docs.python.org/3/library/json.html#encoders-and-decoders
