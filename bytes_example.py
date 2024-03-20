# equation = bytes((207, 128, 114, 194, 178))
equation = b'\xcf\x80r\xc2\xb2'
# bytes and bytearray objects are often used to process Unicode data.
# Because of that, Python allows you to use a string-like syntax when creating a bytes object.
# so line 1 and line 2 do the same thing

print(equation)
print(type(equation))
print(len(equation))

# Inside the string, you can use any ASCII character.For byte values that you can't type on the keyboard,
# you can use hexadecimal values, escaped with `\x`. So our byte string contains 5 values,
# starting with the hexadecimal value CF. That's followed by 80 in hex, then a letter r
# Finally, we have the two hex values C2 and B2. That's 5 bytes in total.

for byte in equation:
    print(byte)
print("*"*40)
# It might seem strange that Python allows an array of bytes to be defined in the same way as a string, but it
# makes sense when you consider what happens when you read binary data from a Unicode text file.
# If you open a text file in binary mode, you'll read an array of bytes, rather than a string.
# You can then decode that array, to get a string. Let's decode our equation bytes object:

equation = equation.decode("utf-8")
print(equation)