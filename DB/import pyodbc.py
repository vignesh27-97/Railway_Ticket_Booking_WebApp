import pyodbc 

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=localhost;"
                      "Database=sampledb;"
                      "Trusted_Connection=yes;")
                    
cursor = connection.cursor()

cursor.execute('SELECT * FROM sampledb.dbo.Person')# select * from Databasename.Tablename

for row in cursor:
    print(row)
