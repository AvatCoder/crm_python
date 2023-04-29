import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Unity_8862'
)
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm_db")
print('All Done')