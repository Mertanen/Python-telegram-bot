import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
import locale

import bot_config
from handlers import scheduleMenu, startHandler, menu
import handlers.sched_handlers.professor as professor
import handlers.sched_handlers.classroom as classroom
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
    dp.include_router(startHandler.router)
    dp.include_routers(menu.router, scheduleMenu.router, professor.router, classroom.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
    
if __name__ == '__main__':  
    asyncio.run(main()) 
    