import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21128733"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "13f1c613ae0775aa68f05cd3df5531c7")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://EXONTESTMONGO:EXONTESTMONGO@cluster0.bviw7ic.mongodb.net/?retryWrites=true&w=majority")
