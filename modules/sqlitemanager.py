import sqlite3
import texttable

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
        returnID = None
        for x in users:
            if (int(x['cardNo']) == int(accountString)):
                accountObject = x

        if(accountObject):
            returnID = self.incrementUsers(accountString)
        else:
            returnID = self.createUsersRow(accountString)

        # accountMatch = [x for x in users if int(x['cardNo']) == int(accountString)]
        # print(accountMatch)
        return returnID

    def createUsersRow(self, accountString):
        conn = sqlite3.connect('main.sqlite')
        c = conn.cursor()

        c.execute(f'INSERT INTO users (cardNo , uses) VALUES({accountString}, 1);')
        execution = c.execute(f'SELECT id FROM users WHERE cardNo = {accountString};').fetchone()
        conn.commit()
        conn.close()
        return execution[0]


    def incrementUsers(self, cardNo):
        conn = sqlite3.connect('main.sqlite')
        c = conn.cursor()
        execution = c.execute(f'SELECT * FROM users WHERE cardNo = {cardNo};').fetchall()[0]
        uses = int(execution[2])+1

        c.execute(f'UPDATE users SET uses = {str(uses)} WHERE cardNo = {cardNo};')
        conn.commit()
        conn.close()
        return execution[0]
    # Rack Stuff
    def getRack(self, rackId):
        conn = sqlite3.connect('main.sqlite')
        c = conn.cursor()

        returnObject = c.execute(f'SELECT * FROM racks WHERE id = {rackId};').fetchall()[0]
        conn.close()
        return returnObject
    def toggleRack(self, rackId):
        conn = sqlite3.connect('main.sqlite')
        c = conn.cursor()

        rack = c.execute(f'SELECT * FROM racks WHERE id = {rackId};').fetchall()[0]
        returnmessage = rack[0]
        locked = ""
        if (int(rack[1]) == 1):
            locked = "0"
        elif (int(rack[1]) == 0):
            locked = "1"
        c.execute(f'UPDATE racks SET locked = {locked} WHERE id = {rackId};')
        conn.commit()
        
        conn.close()
        return returnmessage
    def rackTable(self):
        conn = sqlite3.connect('main.sqlite')
        c = conn.cursor()
        racks = c.execute(f'SELECT * FROM racks;').fetchall()
        conn.close()
        print(racks)
        table = texttable.Texttable()
        table.add_row(["Rack Number", "Locked"]) 
        for rack in racks:
            table.add_row([rack[0], rack[1]])
        return table.draw()
        
    # Active Stuff
    def createActiveRow(self, userID, rackID):
        conn = sqlite3.connect('main.sqlite')
        c = conn.cursor()

        c.execute(f'INSERT INTO active (userID , rackID) VALUES({userID}, {rackID});')
        conn.commit()
        conn.close()
    def findActiveRow(self, userID):
        conn = sqlite3.connect('main.sqlite')
        c = conn.cursor()

        print(f'SELECT * FROM active WHERE userID = {userID};')

        returnObject = c.execute(f'SELECT * FROM active WHERE userID = {userID};').fetchall()
        conn.commit()
        conn.close()
        return returnObject
    def deleteActiveRow(self, userID):
        conn = sqlite3.connect('main.sqlite')
        c = conn.cursor()

        returnObject = c.execute(f'DELETE FROM active WHERE userID = {userID};').fetchall()
        conn.commit()
        conn.close()
        return returnObject

