import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="1499",
    port="5433"
)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS person(
id int primary key,
age int,
name varchar(100),
gender char
);
""")

cur.execute("""INSERT INTO person(id, age, name, gender) 
VALUES
(1, 30, 'mike', 'm'),
(2, 28, 'john', 'm'),
(3, 25, 'lisa', 'f'),
(4, 33, 'bob', 'm')

""")


cur.execute("""Select * from person where age < 30""")
print(cur.fetchone())

cur.execute("""SELECT * FROM person""")
print(cur.fetchall())

cur.execute("""SELECT * FROM person""")
for row in cur.fetchall():
    print(row)

conn.commit()
cur.close()
conn.close()