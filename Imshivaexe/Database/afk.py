from Imshivaexe.Database import db

afkdb = db.afk

async def is_afk():
    self_afk = await afkdb.find_one({"_": "_"})
    if not self_afk:
        return False
    return True

async def add_afk(details):
    return await afkdb.update_one({"_": "_"}, {"$set": {"details": details}}, upsert=True)

async def remove_afk():
    return await afkdb.delete_one({"_": "_"})

async def get_afk_details():
    get = await afkdb.find_one({"_": "_"})
    det = get["details"]
    AFK_DETAILS = [det["afk_time"], det["afk_reason"]]
    return AFK_DETAILS
