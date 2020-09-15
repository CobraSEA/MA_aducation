import pyodbc
constr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=caracal;DATABASE=HRB37_PRF;UID=RBADM;PWD=RBSYS'
conn = pyodbc.connect(constr)
table_name = 'RFACC'
db_code = "'PRF'"
cur = conn.execute(f'select top 10 * from {table_name} where DBCODE = {db_code}')
rec = cur.fetchone()

while rec:
    print(rec)
    rec = cur.fetchone()

cur.close()
conn.close()