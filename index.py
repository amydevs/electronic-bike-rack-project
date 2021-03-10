from modules.sqlitemanager import SqliteManager
from modules.barcodemanager import BarcodeManager
from modules.ocrmanager import OcrManager
import os

while (True):
    os.system('clear')
    print(SqliteManager().rackTable())
    def run():
        correctNumber = False
        while (not correctNumber):
            returnedArr = OcrManager().camera()
            accountString = None
            for x in returnedArr:
                if (len(x) == 9 and ' ' not in str(accountString)):
                    accountString = x
            if (accountString):
                
                if (input(f"Is {accountString} your ID number? (y/n): ").lower() == 'y'):
                    return SqliteManager().cardNoProcess(accountString)
                else:
                    x
            else:
                x

    # cardNo = 213123
    # userID = SqliteManager().cardNoProcess(cardNo)
    userID = run()
    racksActivebyUser = SqliteManager().findActiveRow(userID)
    if (len(racksActivebyUser) != 0):
        SqliteManager().toggleRack(racksActivebyUser[0][2])

        SqliteManager().deleteActiveRow(userID)
    else:
        rackId = input('Enter your desired rack number: ')
        rackIsntUnique = False
        if (int(SqliteManager().getRack(rackId)[1]) == 1):
            rackIsntUnique = True
        while (rackIsntUnique):
            rackId = input('Rack already used. Enter your desired rack number: ')
            if (int(SqliteManager().getRack(rackId)[1]) != 1):
                rackIsntUnique = False


        print (SqliteManager().toggleRack(rackId))

        SqliteManager().createActiveRow(userID, rackId)
    os.system('clear')










