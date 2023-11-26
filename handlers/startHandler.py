from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder
import shelve
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bot import bot
from aiogram.enums import ParseMode
from datetime import datetime, timedelta

from Scheduler import Scheduler
from keyboards.configKeyboard import *
from keyboards.menuKeyboard import getMenuKeyboard
from everyDaySchedule import sendScheduleOnTime
from formattingSchedule import *

router = Router()
data = Scheduler()

@router.message(Command("restart"))
async def restart(message: Message):
    import subprocess
    subprocess.call(["sudo", "systemctl", "restart", "telegram-bot"])
    await message.answer("Ушел на перезагрузку")  

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(
        text=f"Настройка конфигурации",
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        text="Выберите факультет",
        reply_markup=facultyKeybouard(data).as_markup()
    )    

@router.callback_query(F.data[:2] == "f_")
async def configCallback(callback: CallbackQuery):
    data.setDivisionID(callback.data[2:])
    await callback.message.edit_text(text=f"Выберите курс", reply_markup=courseKeybouard(data).as_markup())
           
@router.callback_query(F.data[:2] == "c_")    
async def configCallback(callback: CallbackQuery):
    data.setCourse(callback.data[2:])
    await callback.message.edit_text(text="Выберите группу", reply_markup=groupKeyboard(data).as_markup())
    
@router.callback_query(F.data[:2] == "g_")
async def configCallback(callback: CallbackQuery):
    user_id = callback.from_user.id
    db = shelve.open('./db/user_data', 'c')
    data.setGroupID(callback.data[2:])
    db[f'{user_id}'] = data.getGroupID()
    db.close()
    await callback.message.edit_text(text="Настройка конфигурации завершена", reply_markup=InlineKeyboardBuilder().as_markup())
    await callback.message.answer("Начало работы", reply_markup=getMenuKeyboard())
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(
        sendScheduleOnTime, 
        trigger='interval', 
        start_date=datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour=6),
        seconds=int(timedelta(days=1).total_seconds()),
        kwargs={'bot': bot, 'user_id': user_id}
    )
    scheduler.start()
    