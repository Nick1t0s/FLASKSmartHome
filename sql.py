import sqlite3
def createTable(ip,columns):
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

def execSQL(ip,sqlQuest):
    with sqlite3.connect(f"devices\\{ip.replace(".","_")}\\{ip.replace(".","_")}.db") as con:
        cur = con.cursor()
        cur.execute(sqlQuest)
    # print(type(cur.fetchall()))
    # print(cur.fetchall())
    ans=[list(i) for i in cur.fetchall()]
    # print(*ans,sep="\n")
    if cur.fetchall == []:return []
    else: return ans
# createTable("192.168.1.42",{"column1":"INTAGER","column2":"STRING","column3":"INTAGER","column4":"STRING","column5":"INTAGER"})
# execSQL("192.168.1.42","SELECT * FROM Data")
