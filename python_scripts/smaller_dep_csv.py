import csv

# converted 'International_Report_Departures.csv' down to the necessary
# parts (id, year, month, charter, scheduled, usg_apt, fg_apt, airline_id),
# resulting in 'int_departures_output.csv'

with open('International_Report_Departures.csv', newline='') as csv_input:
    reader = csv.DictReader(csv_input)
    i = 1
    print("Creating airports Dictionary")
    with open('int_departures_output.csv', 'w', newline='') as csv_output:
        fieldnames = ['id','year', 'month', 'charter', 'scheduled',
                      'usg_apt', 'fg_apt', 'airline_id']
        writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
        writer.writeheader()
        for input_row in reader:
            try: 
                writer.writerow({'id': i,
                                 'year': input_row["Year"],
                                 'month': int(input_row["Month"]),
                                 'charter': int(input_row["Charter"]),
                                 'scheduled': int(input_row["Scheduled"]),
                                 'usg_apt': input_row["usg_apt"],
                                 'fg_apt': input_row["fg_apt"],
                                 'airline_id': int(input_row["airlineid"])})
                i = i + 1
                # if i > 1:
                    # break
            except csv.Error as e:
                sys.exit('System exit - ', e)

print('Done')s
