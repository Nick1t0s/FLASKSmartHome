import sqlite3
def createTable(columns,ip):
    command="CREATE TABLE IF NOT EXISTS Data ("
    for column in columns:
        command+=f"{column} {columns[column]},\n"
    command=command[:-2]
    command+="\n)"
    print(command)
    with sqlite3.connect(f"devices\\{ip.replace(".","_")}\\{ip.replace(".","_")}.db") as con:
        cur=con.cursor()
        cur.execute(command)
        con.commit()

def deleteTable(ip):
    command="DROP TABLE IF EXISTS Data"
    with sqlite3.connect(f"devices\\{ip.replace(".","_")}\\{ip.replace(".","_")}.db") as con:
        cur=con.cursor()
        cur.execute(command)
        con.commit()