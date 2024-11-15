import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24267726"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "7500ba8248548cc3864bd033668f9a9a")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://EXONTESTMONGO:EXONTESTMONGO@cluster0.bviw7ic.mongodb.net/?retryWrites=true&w=majority")
