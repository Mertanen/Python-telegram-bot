import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
import locale

import bot_config
from handlers import onStartHandler, scheduleMenuHandler, startMenuHandler
import handlers.sched_handlers.professorMenuHandler as professorMenuHandler
import handlers.sched_handlers.classroomMenuHandler as classroomMenuHandler
from clearDataBase import clearDataBase

logging.basicConfig(filename='bot.log', level=logging.INFO)
 
bot = Bot(token=bot_config.bot_token)
dp = Dispatcher()   

async def main():
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(
        clearDataBase, 
        trigger='interval', 
        start_date=datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour=0),
        seconds=int(timedelta(days=4).total_seconds()),
    )
    scheduler.start()
    dp.include_router(onStartHandler.router)
    dp.include_routers(startMenuHandler.router, scheduleMenuHandler.router, professorMenuHandler.router, classroomMenuHandler.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
    
if __name__ == '__main__':  
    asyncio.run(main()) 
    