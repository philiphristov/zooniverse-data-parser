import csv
import re
import json
import ast

with open('verbaalpina-classifications.csv', newline='') as csv_read:
	with open('csv_data.csv', 'w', newline='') as csv_writer:

		zooniverse_reader = csv.reader(csv_read, delimiter=',', quotechar='"')
		csv_writer = csv.writer(csv_writer, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		
		for row in zooniverse_reader:

			parsed_data_values = row[11][1:-1]
			dict_obj = json.loads(parsed_data_values)

			parsed_data_map = row[12]
			map_data = json.loads(parsed_data_map)
			map_nr = 0

			for value in map_data:
				print(map_data[value])

				if 'map_id' in map_data[value]:
					print(map_data[value]["map_id"])

				if 'map_img' in map_data[value]:
					print(map_data[value]["map_img"])

			
			

			# values = dict_obj["value"]
			# print(values)
			

			print("\n")

