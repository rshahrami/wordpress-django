import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="database", user='user', password='password', host='host', port= 'port'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

#Closing the connection
conn.close()
