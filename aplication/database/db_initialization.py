import mysql.connector
from products_information import *


# as it is not a real project, I will leave it here,
# in another case I would remove it to a special file

host = '127.0.0.1'
user = 'admin'
password = 'your_mysql_password'
database = 'products'

# Establish a connection to the MySQL server
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

try:
    # Create a database (if it doesn't exist)
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")

    # Switch to the specified database
    cursor.execute(f"USE {database}")

    # Create a table (if it doesn't exist)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            description TEXT,
            price DECIMAL(10, 2),
            image_url VARCHAR(255)
        )
    """)

    # Insert a record into the table
    product_data = {
        'name': HpLaptop.label,
        'description': HpLaptop.detail_info(),
        'price': HpLaptop.price(),
        'image_url': HpLaptop.hp_image_link()
    }

    cursor.execute("""
        INSERT INTO products (name, description, price, image_url)
        VALUES (%(name)s, %(description)s, %(price)s, %(image_url)s)
    """, product_data)

    # Commit the changes
    conn.commit()

    print("Record inserted successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
