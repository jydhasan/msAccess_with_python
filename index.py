import pyodbc

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\patsa\Desktop\msAccess\customer.accdb;')
cursor = conn.cursor()
cursor.execute('select * from user')

for row in cursor.fetchall():
    print(row)
