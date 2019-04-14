import csv

with open('verbaalpina-classifications.csv', newline='') as csv_read:
	with open('csv_data.csv', 'w', newline='') as csv_writer:

		zooniverse_reader = csv.reader(csv_read, delimiter=',', quotechar='|')
		csv_writer = csv.writer(csv_writer, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		
		for row in zooniverse_reader:
			print(', '.join(row))

