import os
API_ID = int(os.getenv("5962135"))
API_HASH = os.getenv("61c06ec69048612b49788f41bbdeb61f")
BOT_TOKEN = os.getenv("1862900591:AAHdOgND0ojzVl2tWBsJu6GKzDcA78oOvCU")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
