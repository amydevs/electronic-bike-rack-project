from modules.sqlitemanager import SqliteManager
from modules.barcodemanager import BarcodeManager


racks=SqliteManager.convertSqlite('racks')
users=SqliteManager.convertSqlite('users')
active=SqliteManager.convertSqlite('active')
image = BarcodeManager.camera()
print(BarcodeManager.decode(image))

