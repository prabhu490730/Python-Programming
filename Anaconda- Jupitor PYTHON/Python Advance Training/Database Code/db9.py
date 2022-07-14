# Exception handling and use of Finally: Must use as best Programmer
                                # If nothing works, Finally has to work.
#Inserting Data with Exception handing
import sqlite3
#Create a DB Connection
conn = sqlite3.connect("mydatabase.db")
# Create Curser
cursor =conn.cursor()

SQL = """ INSERT INTO books(bookid, title)
values (203, "Casagrand Boulevard")
"""
# Run the SQL Command
try:
    cursor.execute(SQL)
except Exception:
    print("Something went wrong.. Rolling back..")
    conn.rollback()
else:
    print("All is going Good, Committing..")
    print(cursor.rowcount, "row(s) inserted")
    #Commit
    conn.commit()
finally:
    # Close the Database Connection
    print("Finally Closing the DB Connection")
    conn.close()
#%%
