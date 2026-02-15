import pymysql

# Connect to MySQL Server (without selecting a specific database yet)
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root'  # Using the password from your .env
)

try:
    with connection.cursor() as cursor:
        # Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS todo_list")
        print("✅ Success! Database 'todo_list' created.")
finally:
    connection.close()
    