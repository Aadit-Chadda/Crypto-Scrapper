import sqlite3

db = sqlite3.connect('dogecoin-tracker.sqlite')

# Printing out the database
cursor = db.cursor()
cursor.execute("SELECT * FROM dogeprice")
for timer, pricer in cursor:
    print(timer, '\t', pricer)
    print()

cursor.close()
db.close()
