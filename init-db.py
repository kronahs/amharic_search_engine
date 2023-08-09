import pymysql

# Connect to MySQL (replace with your database connection details)
db_connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
)
cursor = db_connection.cursor()

# Create the database
try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS amharic_documents")
    print("Database 'amharic_documents' created successfully.")
except pymysql.Error as e:
    print(f"Error creating database: {e}")

# Switch to the created database
cursor.execute("USE amharic_documents")

# Create the 'amharic_documents' table
create_amharic_documents_table = """
CREATE TABLE IF NOT EXISTS amharic_documents (
    id INT PRIMARY KEY,
    headline VARCHAR(255),
    category VARCHAR(255),
    date DATE,
    views INT,
    article TEXT,
    link VARCHAR(255)
)
"""
try:
    cursor.execute(create_amharic_documents_table)
    print("'amharic_documents' table created successfully.")
except pymysql.Error as e:
    print(f"Error creating 'amharic_documents' table: {e}")

# Create the 'inverted_index' table
create_inverted_index_table = """
CREATE TABLE IF NOT EXISTS inverted_index (
    word VARCHAR(255),
    document_id INT,
    tf FLOAT,
    idf FLOAT,
    frequency INT,
    composite FLOAT,
    PRIMARY KEY (word, document_id)
)
"""
try:
    cursor.execute(create_inverted_index_table)
    print("'inverted_index' table created successfully.")
except pymysql.Error as e:
    print(f"Error creating 'inverted_index' table: {e}")

# Close the database connection
cursor.close()
db_connection.close()
