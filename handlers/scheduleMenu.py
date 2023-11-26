from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder
import shelve
from datetime import datetime, timedelta

from keyboards.menuChooseScheduleKeyboard import *
from keyboards.menuKeyboard import getMenuKeyboard
from formattingSchedule import *
import handlers.sched_handlers.professor as professor
from keyboards.configKeyboard import *

router = Router()
data = Scheduler()

@router.message(F.text == "Расписание на эту неделю")
async def cmd(message: Message):
    schedule = getScheduleOnWeek(user_id=message.from_user.id)   
    await message.answer(schedule, parse_mode=ParseMode.HTML)

@router.message(F.text == "Расписание на следующую неделю")
async def cmd(message: Message):
    schedule = getScheduleOnWeek(user_id=message.from_user.id, date=datetime.now() + timedelta(days=7))
    await message.answer(schedule, parse_mode=ParseMode.HTML)

@router.message(F.text == "Расписание преподавателя")
async def cmd(message: Message):
    await message.answer(text="Выберите расписание преподавателя", reply_markup=ReplyKeyboardRemove())
    await message.answer(text="Выберите факультет", reply_markup=DivisionKeybouard(data).as_markup())

@router.message(F.text == "Расписание аудитории")
async def cmd(message: Message):
    await message.answer(text="Выберите расписание аудитории", reply_markup=ReplyKeyboardRemove())
    await message.answer(text="Выберите корпус", reply_markup=korpusKeybouard(data).as_markup())

@router.message(F.text == "Меню")
async def backToMenu(message: Message):
    await message.answer(text="Возвращение в меню", reply_markup=getMenuKeyboard())
    
@router.message(F.text == "Меню расписания")
async def backToMenu(message: Message):
    await message.answer(text="Возвращение в меню расписания", reply_markup=getMenuChooseKeyboard())
    
###############

@router.callback_query(F.data[:2] == "d_")
async def configCallback(callback: CallbackQuery):
    data.setDivisionID(callback.data[2:])
    await callback.message.edit_text(text="Выберите кафедру", reply_markup=kafedraKeybouard(data).as_markup())
    
@router.callback_query(F.data[:2] == "k_")
async def configCallback(callback: CallbackQuery):
    data.setKafedra(callback.data[2:])
    await callback.message.edit_text(text="Выберите преподавателя", reply_markup=professorKeyboard(data).as_markup())
    
@router.callback_query(F.data[:2] == "p_")
async def configCallback(callback: CallbackQuery):
    user_id = callback.from_user.id
    data.setProfessor(callback.data[2:])
    db = shelve.open('./db/user_data', 'c')
    db[f'prof_{user_id}'] = data.getProfessorID()
    db.close()
    await callback.message.edit_text(text="Настройка завершена", reply_markup=InlineKeyboardBuilder().as_markup())
    await callback.message.answer(text="Выберите расписание", reply_markup=professorReplyKeyboard())

###############

@router.callback_query(F.data[:3] == "kp_")
async def configCallback(callback: CallbackQuery):
    data.setKorpus(callback.data[3:])
    await callback.message.edit_text(text="Выберите аудиторию", reply_markup=classroomKeybouard(data).as_markup())
    
@router.callback_query(F.data[:3] == "cl_")
async def configCallback(callback: CallbackQuery):
    data.setClassroom(callback.data[3:])
    user_id = callback.from_user.id
    db = shelve.open('./db/user_data', 'c')
    db[f'class_{user_id}'] = [data.getClassroomNumber(), data.getKorpus()]
    db.close()
    await callback.message.edit_text(text="Настройка завершена", reply_markup=InlineKeyboardBuilder().as_markup())
    await callback.message.answer(text="Выберите расписание", reply_markup=classroomReplyKeyboard())