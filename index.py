from modules.sqlitemanager import SqliteManager
from modules.barcodemanager import BarcodeManager
from modules.ocrmanager import OcrManager
import numpy as np

def run():
    returnedArr = OcrManager.camera()
    accountString = None
    for x in returnedArr:
        if (len(x) == 9 and ' ' not in str(accountString)):
            accountString = x
    if (accountString):
        return SqliteManager().cardNoProcess(accountString)
    else:
        run()
        return

# cardNo = 213123
# userID = SqliteManager().cardNoProcess(cardNo)
userID = run()
racksActivebyUser = SqliteManager().findActiveRow(userID)
if (len(racksActivebyUser) != 0):
    SqliteManager().toggleRack(racksActivebyUser[0][2])

    SqliteManager().deleteActiveRow(userID)
    exit()



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










