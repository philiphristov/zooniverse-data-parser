import csv
import re
import json
from ast import literal_eval

with open('verbaalpina-classifications.csv', newline='') as csv_read:
	with open('csv_data.csv', 'w', newline='') as csv_writer:

		zooniverse_reader = csv.reader(csv_read, delimiter=',', quotechar='"')
		csv_writer = csv.writer(csv_writer, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		
		for row in zooniverse_reader:
			#parsed_row = [ item.strip('\"') for item in row  ]
			print(', '.join(row))
			print("\n")

			parsed_data = "'" + row[11].replace("'", "\"")[1:-1] + "'"

			print(parsed_data)

			# dict_obj = json.loads(parsed_data)
			dict_obj = literal_eval(parsed_data)

			print(dict_obj)
			print("\n")

