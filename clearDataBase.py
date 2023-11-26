import shelve

async def clearDataBase():
    db = shelve.open('./db/user_data', 'c')    
    db.clear()
    db.close()  