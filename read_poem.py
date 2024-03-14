# When you want to work with a file, you have to open it first.

jabber = open("Jabberwocky.txt", "r")
# The first argument we pass to open, is the name of the file that we want to open.
# That's Jabberwocky.txt, here. Because I put the text file into my project
# directory, I haven't had to specify the full path. If you're still unsure about file paths,
# keep your text files in the project directory, until you've learnt more about paths.
# The second argument is 'r', which stands for read. We can read from this file, but we can't write to it.

jabber.close()

# Importantly, we have to close the file when we're finished – that's on line 10.
# If you don't close a file when you're finished with it, you can get problems.

# To open a file, we use the open function:
# This isn't the cleanest way to open a file, in Python.
# PEP 343 introduced the `with` statement, for working with things like files.

with open("Jabberwocky.txt","r") as jabber:
    for line in jabber:
        print(line,end="")
        print(len(line))

# Because with is a statement, not a function, we don't get a file object returned.
# Instead, we use "as jabber" to give a name to the file object.
# Opening a file this way is preferred, because the file will be automatically closed when the with block terminates.
