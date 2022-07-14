# In this example: Learn to create DB
import sqlite3
conn = sqlite3.connect("mydatabase.db")
# Execute any SQL Statement: USE "Curser" to run the queries>> Similar to File Pointer
cursor =conn.cursor()
# Create Table
SQL = """ CREATE TABLE books(
bookid integer,
title varchar(255)
)
"""
# Run the SQL Command
cursor.execute(SQL)
# Close the DB Connection
conn.close()

#%%
