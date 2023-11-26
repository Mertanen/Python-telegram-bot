from aiogram import Bot
from formattingSchedule import getScheduleOnDate
from aiogram.enums import ParseMode
from datetime import datetime, timedelta


async def sendScheduleOnTime(bot: Bot, user_id ):
    schedule = getScheduleOnDate(user_id=user_id, date=datetime.now())
    await bot.send_message(user_id, text=schedule, parse_mode=ParseMode.HTML)
    