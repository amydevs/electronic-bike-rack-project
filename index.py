from modules.sqlitemanager import SqliteManager
from modules.barcodemanager import BarcodeManager
from modules.ocrmanager import OcrManager
import numpy as np

cardNo = 213321
userID = SqliteManager().cardNoProcess(cardNo)

rackId = input('Enter your desired rack number: ')
print (SqliteManager().toggleRack(rackId))

SqliteManager().createActiveRow(userID, rackId)




# def run():
#     returnedArr = OcrManager.camera()
#     accountString = None
#     for x in returnedArr:
#         if (len(x) == 9 and ' ' not in str(accountString)):
#             accountString = x
#     if (accountString):
#         SqliteManager().cardNoProcess(accountString)
#     else:
#         run()
#         return

# run()



