import mysql.connector

conn = mysql.connector.connect(
        host = "cp-15.webhostbox.net",
        user = "mongouhd_python",
        password =  "GVvc?zdZQS5V",
        database = "mongouhd_python"
)

if conn:
    print("Successfully Connected")
conn.close()


#%%
