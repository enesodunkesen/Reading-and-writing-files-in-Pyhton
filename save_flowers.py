data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

file_name = "flowers_print.txt"

with open(file_name, "w") as flowers_file:
    # We want to write to this file. It's almost the same as reading a file, but we specify "w" for the mode.
    # That's "w" for write. After opening the file for writing, we iterate over the items in our data list.
    # Inside the loop, we'll send each item to the file.
    # That's easy, but there are two different ways to do it.
    for flower in data:
        print(flower, file=flowers_file)
        # The file keyword argument tells print where it should print the data to.
        # The default is to print to the screen. That's most often what you want to do, which is why it's the default.
        # But you can print to any output stream that can accept text – including to an open file.

    # other way is the using .write() method, but it's problematic in 2 ways
    # first is the print automatically adds newline char at the end of string write method doesn't
    # second is the print automatically calls __str__ method of the argument write doesn't
    # that means when we use write with non-text data types such as ints we have to explicitly

with open(file_name,"w") as flowers_file:
    for i in range(10):
        flowers_file.write(str(i)+'\n')


