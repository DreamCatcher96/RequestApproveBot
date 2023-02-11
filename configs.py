from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "25640503"))
    API_HASH = getenv("API_HASH", "2f70ec120918a722b671b3e96a2aefa7")
    BOT_TOKEN = getenv("BOT_TOKEN", "5900213880:AAEGV6XbBcACuNU3owOMvZ_uEpM5iRWp1Lc")
    FSUB = getenv("FSUB", "Galexycinemas")
    CHID = int(getenv("CHID", "-1001702258788"))
    SUDO = list(map(int, getenv("SUDO", "5002985537 5292845540").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Autoaccept1:Autoaccept1@cluster0.n9s38ir.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
