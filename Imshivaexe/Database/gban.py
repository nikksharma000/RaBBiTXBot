from Imshivaexe.Database import db

db = db.gban

async def gban(user_id: int):
    x = await db.find_one({"user_id": user_id})
    if not x:
        await db.insert_one({"user_id": user_id})

async def ungban(user_id: int):
    x = await db.find_one({"user_id": user_id})
    if x:
        await db.delete_one({"user_id": user_id})

async def is_gbanned(user_id: int):
    x = await db.find_one({"user_id": user_id})
    if x:
        return True
    return False
