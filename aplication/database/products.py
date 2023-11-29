import mysql.connector

# Replace these values with your MySQL server credentials
host = 'your_mysql_host'
user = 'your_mysql_user'
password = 'your_mysql_password'
database = 'your_database_name'
def get_products():
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return products