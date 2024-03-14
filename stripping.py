file = "Jabberwocky.txt"

with open(file, "r") as poem:
    line = poem.readline()

line = line.strip()
# note that strip methods has a default values, they are whitespaces(space, tab, newline char)
# also note that we have to assign a variable to operations on strings since they're immutable
print(line)
print(line.strip("'"))
print(line.strip("'Twasoeb "))

# These strip methods don't remove the string that you pass as an argument.
# They take each of the characters in the string, and keep removing them,
# until a non-matching character is found.

print(line.rstrip("eosv"))
# .rstrip() method works just like .strip() but only strips end of the string

print(line.lstrip("'twas "))
# and there is also .lstrip() method

# if we want to remove one string from the start, or end of another we should use .prefix() and .suffix() methods

print(line.casefold().removeprefix("'twas "))
print(line.removesuffix("toves"))


# these methods are present Python 3.9 or later but they're easy to implement

def remove_prefix(first: str, prefix: str) -> str:
    if first.startswith(prefix):
        return first[len(prefix):]
    else:
        return first


def remove_suffix(first: str, prefix: str) -> str:
    if first.endswith(prefix):
        return first[:-len(prefix)]
    else:
        return first
