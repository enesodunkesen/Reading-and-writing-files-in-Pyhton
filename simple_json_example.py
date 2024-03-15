# Serialization is the process of converting an object or data structure into a format that can be easily stored,
# transmitted, or reconstructed at a later time. The serialized form is typically a stream of bytes or a string
# that can be written to a file, sent over a network, or stored in a database.
# json(javascript object notation) is such a format, plus it's a standard for serialization

import json

languages = [
    ['ABC', 1987],
    ['Algol 68', 1968],
    ['APL', 1962],
    ['C', 1973],
    ['Haskell', 1990],
    ['Lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]

with open("test.json", 'w', encoding='utf-8') as serialization:
    json.dump(languages, serialization)
    # To serialize Python values to a file,
    # we open a text file for writing, then use the json.dump function.
    # The dump function serializes the data we give it(arg1), and write the result to the file(arg2).
    # We've also specified the encoding to be UTF-8 – the JSON standard specifies UTF-8 for JSON documents.

with open("test.json", 'r', encoding='utf-8') as deserialization:
    data = json.load(deserialization)
    # For it to be useful, we also need to be able to read it back in again.
    # To do that, we use the json.load function.
    # The json module handles it well, and we retain our original structure.

print(type(languages))
print(type(data))

