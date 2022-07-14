

# .py >>> Connect to >> .DBI >> Connect to >> Database
import sqlite3
# In this example: Learn to create DB Connection
conn = sqlite3.connect("mydatabase.db")
print (type(conn))

print(conn.total_changes)
conn.close()

#%%
