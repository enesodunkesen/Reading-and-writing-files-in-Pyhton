import csv

ordering = ['Country', 'Gold', 'Silver', 'Bronze', 'Rank']
# Note the lack of 'Total' in `ordering`

with open('OlympicMedals_2020.csv', encoding='utf-8', newline='') as data,\
        open('medals_dict.py', 'w', encoding='utf-8') as output_file:
    # Write the first part of the code (excluding the actual data)
    print('import csv', file=output_file)
    print(file=output_file)
    print('medals_table = [', file=output_file)

    reader = csv.DictReader(data)
    for row in reader:
        new_dict = {}
        for key in ordering:
            value = row[key]
            if value.isnumeric():
                value = int(value)
            new_dict[key.casefold()] = value
        print(f'    {new_dict},', file=output_file)

    print("]", file=output_file)
