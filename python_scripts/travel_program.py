import csv, sys
import a_config
import mysql.connector
from mysql.connector import errorcode

# imported int_departures_output.csv into database, in 10,000 increments

print('everything was found')

try:
    cnx = mysql.connector.connect(user=a_config.DB_USER,
                                  password=a_config.DB_PASSWORD,
                                  host=a_config.DB_HOST,
                                  database=a_config.DB_DATABASE)
    cursor = cnx.cursor()
    print('Connection to', a_config.DB_DATABASE, 'successful')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("ERROR: Something wrong with your user name or password")
    sys.exit(0)
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("ERROR: Database does not exist")
    sys.exit(0)
  else:
    print(err)
    sys.exit(0)

departures = []

add_departures = ("INSERT INTO Departure "
                  "(id, flight_year, month, charter, "
                  "scheduled, usg_apt, fg_apt, airline_id) "
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

with open('int_departures_output.csv', newline='') as csv_input:
    reader = csv.DictReader(csv_input)
    print("Creating airports Dictionary")
    for row in reader:
        current_row = int(row["id"])
        departures.append((current_row,
                           row["year"],
                           int(row["month"]),
                           int(row["charter"]),
                           int(row["scheduled"]),
                           row["usg_apt"],
                           row["fg_apt"],
                           int(row["airline_id"])))
        # print(current_row, end=' ')
        # i = i + 1
        if current_row % 10000 == 0:
            print(current_row, 'total rows in database')
            print('Adding departures...')
            cursor.executemany(add_departures, departures)
            print("Committing departures...")
            cnx.commit()
            departures.clear()
            # if current_row >= 100000: <-- used to test a subset of departures
                # break

print(current_row, 'total rows in database')
print('Adding departures...')
cursor.executemany(add_departures, departures)
print("Committing departures...")
cnx.commit()
departures.clear()
print("Closing...")
cursor.close()
cnx.close()
print('Database closed. closing program...')
sys.exit(0)
