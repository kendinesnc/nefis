import os
API_ID = int(os.getenv("4748268"))
API_HASH = os.getenv("3bb985dd19588c90aaad6179dfaa9803")
BOT_TOKEN = os.getenv("1862900591:AAHdOgND0ojzVl2tWBsJu6GKzDcA78oOvCU")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
