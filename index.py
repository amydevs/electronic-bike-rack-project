from modules.sqlitemanager import SqliteManager
from modules.barcodemanager import BarcodeManager
from modules.ocrmanager import OcrManager
import numpy as np

SqliteManager().cardNoProcess('9012391')

input = input('Enter your desired rack number: ')
print (SqliteManager().toggleRack(input))


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



