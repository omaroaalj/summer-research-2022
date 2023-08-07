import csv

countryDict = {}
categoryDict = {}
time_spent_rows = []

with open('Country.csv', newline='') as country_csvfile:
    reader = csv.DictReader(country_csvfile)
    for row in reader:
        countryDict[row["country_name"]] = row["country_id"]

with open('Category.csv', newline='') as category_csvfile:
    reader = csv.DictReader(category_csvfile)
    for row in reader:
        categoryDict[row["category_name"]] = row["category_id"]

with open('TimeSpentByCountry.csv', newline='') as time_spent_csvfile:
    reader = csv.DictReader(time_spent_csvfile)
    for row in reader:
        time_spent_rows.append([row["Country"], row["Category"], row["Time (minutes)"]])

with open('CountryOnCategory.csv', 'w', newline='') as ctc_csvfile:
    fieldnames = ['country_id','category_id','minutes']
    writer = csv.DictWriter(ctc_csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in time_spent_rows:
        print(row[1])
        print('Country', row[0], '-', countryDict[row[0]])
        print('Category', row[1], '-', categoryDict[row[1]])
        print('Minutes', row[2])
        writer.writerow({'country': countryDict[row[0]],
                         'category': categoryDict[row[1]],
                         'minutes': row[2]})

