#!/usr/bin/env python3

'''A simple Python application to import rows of departures from US DOT flight data '''

import mysql.connector
import os.path
from db_tunnel import DatabaseTunnel
import csv

# DB INFORMATION NOT INCLUDED


DB_HOST = ""
DB_SSH_PORT = 0
DB_SSH_USER = ""
DB_PORT = 0

# Default connection information (can be overridden with command-line arguments)
DB_SSH_KEYFILE = ""
DB_NAME = "int_flights"
DB_USER = ""
DB_PASSWORD = ""

# The query that will be executed

departures = []

add_departures = ("INSERT INTO Departure "
                  "(id, flight_year, month, charter, "
                  "scheduled, usg_apt, fg_apt, airline_id) "
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")


class Departures:
    '''A simple Python application to import rows of departures from US DOT flight data'''

    def __init__(self, dbHost, dbPort, dbName, dbUser, dbPassword):
        '''Creates an IMDbEpisodeQuery with the specified connection information'''
        self.dbHost, self.dbPort = dbHost, dbPort
        self.dbName = dbName
        self.dbUser, self.dbPassword = dbUser, dbPassword

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, *args):
        self.close()

    def connect(self):
        self.connection = mysql.connector.connect(
                host=self.dbHost, port=self.dbPort, database=self.dbName,
                user=self.dbUser, password=self.dbPassword,
                use_pure=True
        )
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def runApp(self):
        # 10,000 rows of data are taken at a time
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
                    self.cursor.executemany(add_departures, departures)
                    print("Committing departures...")
                    self.connection.commit()
                    departures.clear()
                    # if current_row >= 100000: <-- used to test a subset of departures
                        # break

        print(current_row, 'total rows in database')
        print('Adding departures...')
        self.cursor.executemany(add_departures, departures)
        print("Committing departures...")
        self.connection.commit()
        departures.clear()
        print('Done')


def main():
    import sys
    '''Entry point of the application. Uses command-line parameters to override database connection settings, then invokes runApp().'''
    # Default connection parameters (can be overridden on command line)
    params = {
        'dbname':       DB_NAME,
        'user':         DB_USER,
        'password':     DB_PASSWORD
    }

    needToPrintHelp = False

    # Parse command-line arguments, overriding values in params
    i = 1
    while i < len(sys.argv) and not needToPrintHelp:
        arg = sys.argv[i]
        isLast = (i + 1 == len(sys.argv))

        if arg in ("-h", "-help"):
            needToPrintHelp = True
            break

        elif arg in ("-dbname", "-user", "-password"):
            if isLast:
                needToPrintHelp = True
            else:
                params[arg[1:]] = sys.argv[i + 1]
                i += 1

        else:
            print("Unrecognized option: " + arg, file=sys.stderr)
            needToPrintHelp = True

        i += 1

    # If help was requested, print it and exit
    if needToPrintHelp:
        printHelp()
        return

    try:
        with \
            DatabaseTunnel() as tunnel, \
            Departures(
                dbHost='localhost', dbPort=tunnel.getForwardedPort(),
                dbName=params['dbname'],
                dbUser=params['user'], dbPassword=params['password']
            ) as app:
            app.runApp()
    except mysql.connector.Error as err:
        print("Error communicating with the database (see full message below).", file=sys.stderr)
        print(err, file=sys.stderr)
        print("\nParameters used to connect to the database:", file=sys.stderr)
        print(f"\tDatabase name: {params['dbname']}\n\tUser: {params['user']}\n\tPassword: {params['password']}", file=sys.stderr)
        print("""
(Did you install mysql-connector-python and sshtunnel with pip3/pip?)
(Are the username and password correct?)""", file=sys.stderr)


def printHelp():
    print(f'''
Accepted command-line arguments:
    -help, -h          display this help text
    -dbname <text>     override name of database to connect to
                       (default: {DB_NAME})
    -user <text>       override database user
                       (default: {DB_USER})
    -password <text>   override database password
    ''')


if __name__ == "__main__":
    main()

