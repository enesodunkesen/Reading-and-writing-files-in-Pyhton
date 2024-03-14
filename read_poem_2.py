# Python provides 3 other methods for reading from a file

with open("Jabberwocky.txt","r") as jabber:
    lines = jabber.readlines()

print(type(lines))

# The .readlines() method returns a list, containing strings for each line from the file.
# So we now have the entire file stored in a list. We've read the entire file,
# and can come out of the with block – allowing Python to close the file

# now we can index through new list and acquire data(for example we could get the last line of the file, using a slice)

print(lines[-1:])

# There is a serious disadvantage to processing a file like this, that you need to consider.
# We've read every single line into a list. That works fine for this short "Jabberwocky" file,
# but what if you're trying to process a file that contains millions of lines?
# The file might be too big to fit into memory.
# As the documentation says, "it's your problem if the file is twice as large as your machine's memory".


with open("Jabberwocky.txt","r") as jabber:
    lines = jabber.read()

print(type(lines))
# Unlike .readlines() method, .read() method doesn't split the lines up.
# Instead, it returns a single string containing all the characters in the file.


with open("Jabberwocky.txt","r") as jabber:
    while True:
        jubjub = jabber.readline()
        print(jubjub)
        if "jubjub" in jubjub.casefold():
            break
# Here, we read the file line-by-line, and break out of the loop when we find something we're looking for.
# and the program terminates when it finds the line containing "Jubjub"
# That's one use for readline. It reads one line of the file at a time.
# The reason you might not use it very often, is that we can get the same result by just iterating
# over the file object – which is what we did when we first looked at reading from a text file.