import csv

ourData = []

# Read original CSV file
print("*** OLD FILE CONTENTS ***")
with open('example.csv') as csv_file:
    read_csv = csv.reader(csv_file, delimiter=',')
    for row in read_csv:
        ourData.append(row)

# New data set to be appended to CSV file
data = [['3', 'Aaron Hussain', 'Lecturer', 'Geek'],
        ['4', 'Steve Rogers', 'Avenger', 'Soldier Serum']]

# Append data to the CSV file
with open('example.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Read updated CSV file
print("*** NEW FILE CONTENTS ***")
with open('example.csv') as csv_file:
    read_csv = csv.reader(csv_file, delimiter=',')
    for row in read_csv:
        print("Full row:", row)
        print("Element 1: ", row[0])
        print("Element 2: ", row[1])
        print("Element 3: ", row[2])
        print("Element 4: ", row[3])


