import sqlite3

class SqliteManager:
    def __init__(initthing):
        self.initthing=initthing

    def convertSqlite(tableName):
        conn = sqlite3.connect('main.sqlite')
        c = conn.cursor()
        
        RowsArray=[]

        RowsDescription=[]
        
        execution=c.execute("SELECT * FROM "+tableName+";")

        for row in execution.description:
            RowsDescription.append(row[0])

        for row in execution.fetchall():
            rowDict={}
            RowsArrayIndex=0
            for name in RowsDescription:
                rowDict[RowsDescription[RowsArrayIndex]] = row[RowsArrayIndex]
                RowsArrayIndex=RowsArrayIndex+1
            RowsArray.append(rowDict)
        conn.close()
        return RowsArray