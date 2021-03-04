import sqlite3

class SqliteManager:
    def __init__(self):
        self.self = self

    def convertSqlite(self, tableName):
        conn = sqlite3.connect('main.sqlite')
        c = conn.cursor()
        
        RowsArray=[]

        RowsDescription=[]
        
        execution=c.execute(f"SELECT * FROM {tableName};")

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
    # User Stuff
    def cardNoProcess(self, accountString):
        users=self.convertSqlite('users')

        accountObject = None
        for x in users:
            print(int(x['cardNo']), int(accountString))
            if (int(x['cardNo']) == int(accountString)):
                accountObject = x

        if(accountObject):
            self.incrementUsers(accountObject)
        else:
            self.createUsersRow(accountString)

        # accountMatch = [x for x in users if int(x['cardNo']) == int(accountString)]
        # print(accountMatch)
        return 

    def createUsersRow(self, accountString):
        conn = sqlite3.connect('main.sqlite')
        c = conn.cursor()

        c.execute(f'INSERT INTO users (cardNo , uses) VALUES({accountString}, 1);')
        conn.commit()
        conn.close()

    def incrementUsers(self, user):
        conn = sqlite3.connect('main.sqlite')
        c = conn.cursor()



        uses = int(user['uses']) + 1
        cardNo = user['cardNo']
        usesthing = c.execute(f'SELECT * FROM users WHERE cardNo = {cardNo};').fetchall()[0]
        
        c.execute(f'UPDATE users SET uses = {str(uses)} WHERE cardNo = {cardNo};')
        conn.commit()
        conn.close()
        return
    # Rack Stuff
    def toggleRack(self, rackId):
        conn = sqlite3.connect('main.sqlite')
        c = conn.cursor()

        rack = c.execute(f'SELECT * FROM racks WHERE id = {rackId};').fetchall()[0]
        returnmessage = rack[0]
        locked = "1"
        if (int(rack[1]) != 1):
            locked = "0"

        c.execute(f'UPDATE users SET locked = {locked} WHERE id = {rackId};')
        conn.commit()
        
        conn.close()
        return returnmessage
    


