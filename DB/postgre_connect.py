import psycopg2 as pg2
print('Opened successfully')
conn = pg2.connect(database='dvdrental', user='postgres', password='password')

cur = conn.cursor()
cur.execute("select * from actor")
value=cur.fetchone()
print(value)


    