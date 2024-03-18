import json
import urllib.request
# Python includes a basic library for opening URLs. That is urllib.request module. When you check out the documentation
# for this module, you'll see a recommendation to use a third-party library called requests, instead.

json_data_source = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/10/1880-2024.json'


# with open(json_data_source, 'r', encoding='utf-8') as data:
with urllib.request.urlopen(json_data_source) as json_stream:
    # The urlopen function can be used in a with statement,
    # so our internet connection will be automatically closed for us.
    data = json_stream.read().decode('utf-8')
    # The next step is to read the data from the stream that we've opened, and decode it from UTF-8:
    # Our original line 6, which is now commented out, specified the encoding when we opened the file.
    # The urlopen function doesn't let us specify an encoding, so we decode the data after reading that's on line 9.
    anomalies = json.loads(data)
    # There is one other change we need to make. On line 9, the JSON load function takes care
    # of reading the data from a file. We've read the data on line 9,and now have a string containing the JSON.
    # json.load gets data from a file – as we've seen.Similarly, json.dump sends data to a file.
    # There are 2 other functions, corresponding to these,that take or return a string. The names are almost the same, they just end in "s".


print(anomalies["description"]["title"])

for key,value in anomalies["data"].items():
    print(f"{key} : {value}")

# print(anomalies["citation"])
