# Script to add/use data in the SQL server (AZURE) - Will be used after the API request runs to commit 
# that information to the database
#Server variables were deleted before uploading for security reasons

import pyodbc

SERVER = 'PLACEHOLDER'
DATABASE = 'PLACEHOLDER'
USERNAME = 'PLACEHOLDER'
PASSWORD = 'PLACEHOLDER'

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString) 

SQL_STATEMENT = """

INSERT INTO dbo.tb_noa (dia_semana, dia_mes, mes, ano, clima, feriado, temperatura, umidade, velocidade)
VALUES ('Sábado', 30, 'março', 2024, 'ameno', 1, 24.0, 82.5, 15.0);

"""

SQL_QUERY = """

SELECT * FROM tb_noa

"""

cursor = conn.cursor()

cursor.execute(SQL_STATEMENT)

cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
    print(r)

conn.commit()
cursor.close()
conn.close()
