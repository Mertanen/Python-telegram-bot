from Scheduler import Scheduler
from datetime import datetime
import shelve
from aiogram.types import Message

data = Scheduler()
TimeTableMain = ['8:30 – 10:00', '10:10 – 11:40', '12:00 – 13:30', '13:40 – 15:10', '15:20 – 16:50', '17:00 – 18:30', '18:40 – 20:10', '20:15 – 21:45']
day = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
db = shelve.open('./db/user_data')

def formatDate(date: datetime):
    return date.strftime("%d.%m.%Y")

########################################### Day Schedule ################################################ 

def getScheduleOnDate(user_id, date):
    try:
        data.setGroupID(groupID=db[f'{user_id}'])
        schedule = data.getSchedule(date=date)
        date = formatDate(date)
        text = "<b>" + f'📅{date} ({day[schedule[0]["DayWeek"]-1]})' + "</b>"
        for item in schedule:
            text += "\n\n" + "🕮" + "<b>" + f"{item['TitleSubject']}({item['TypeLesson']})" + "</b>" + "\n" \
                + "🕰" + "<b>" + f"{TimeTableMain[item['NumberLesson']-1]}" + "</b>" + "\n" \
                    + "👤" + f"{item['Family']} {item['Name']} {item['SecondName']}" + "\n" \
                        + '🚪' + "<b>" + f"{item['Korpus']}-{item['NumberRoom']}" + "</b>"
        return text
    except:
        return "Расписание не найдено"

########################################### Week Schedule ################################################ 

def getScheduleOnWeek(user_id, date=datetime.now()):
    
    try:
        data.setGroupID(groupID=db[f'{user_id}'])
        schedule = data.getSchedule(date=date, week=True)
        dateDict = {}
        for item in schedule:
            if item['DateLesson'] not in dateDict:
                dateDict[f"{item['DateLesson']}"] = []
        for item in schedule:
            (dateDict[f'{item["DateLesson"]}']).append(item)
        dateDict = dict(sorted(dateDict.items()))
        text = ""
        for item in dateDict.keys():
            date = formatDate(datetime.strptime(dateDict[f'{item}'][0]['DateLesson'], '%Y-%m-%d'))
            text += "--------------------------------------------------------------------------------------------------"
            text += "\n\n<b>" + f"📅{date} ({day[dateDict[f'{item}'][0]['DayWeek']-1]})" + "</b>" + "\n"
            for lesson in dateDict[item]:
                text += "\n" + "🕮" + "<b>" + f"{lesson['TitleSubject']}({lesson['TypeLesson']})" + "</b>" + "\n" \
                + "🕰" + "<b>" + f"{TimeTableMain[lesson['NumberLesson']-1]}" + "</b>" + "\n" \
                    + "👤" + f"{lesson['Family']} {lesson['Name']} {lesson['SecondName']}" + "\n" \
                        + '🚪' + "<b>" + f"{lesson['Korpus']}-{lesson['NumberRoom']}" + "</b>" + "\n\n" 
        text += "--------------------------------------------------------------------------------------------------"
        return text
    except:
        return "Расписание не найдено" 
            
########################################### Exams Schedule ################################################ 

def getScheduleExams(user_id):
    try:
        data.setGroupID(groupID=db[f'{user_id}'])
        data.examSchedule()
        schedule = data.getExamSchedule()
        text = str()
        for item in schedule:
            text += "<b>" + f'📅{item["DateLesson"]} ({day[item["DayWeek"]-1]})' + "</b>" + "\n" \
                + "🕮" + "<b>" + f"{item['TitleSubject']}({item['TypeLesson']})" + "</b>" + "\n" \
                    + "🕰" + "<b>" + f"{TimeTableMain[item['NumberLesson']-1]}" + "</b>" + "\n" \
                        + "👤" + f"{item['Family']} {item['Name']} {item['SecondName']}" + "\n" \
                            + '🚪' + "<b>" + f"{item['NumberRoom']}" + "</b>" + "\n\n"
        return text          
    except:
        return "Расписание не найдено"

########################################### Professor Day Schedule ################################################ 

def getProfessorDaySchedule(user_id, date):
    try:
        data.setProfessor(prof_id=db[f'prof_{user_id}'])
        schedule = data.getProfessorSchedule(date=date)
        date = formatDate(date)
        text = "<b>" + f'📅{date} ({day[schedule[0]["DayWeek"]-1]})' + "</b>"
        for item in schedule:
            text += "\n\n" + "🕮" + "<b>" + f"{item['TitleSubject']}({item['TypeLesson']})" + "</b>" + "\n" \
                + "🕰" + "<b>" + f"{TimeTableMain[item['NumberLesson']-1]}" + "</b>" + "\n" \
                    + "👤" + f"{item['Family']} {item['Name']} {item['SecondName']}" + "\n" \
                        + '🚪' + "<b>" + f"{item['Korpus']}-{item['NumberRoom']}" + "</b>"
        return text
    except:
        return "Расписание не найдено"

########################################### Professor Week Schedule ################################################ 

def getProfessorWeekSchedule(user_id, date):
    try:
        data.setProfessor(prof_id=db[f'prof_{user_id}'])
        schedule = data.getProfessorSchedule(date=date, week=True)
        dateDict = {}
        for item in schedule:
            if item['DateLesson'] not in dateDict:
                dateDict[f"{item['DateLesson']}"] = []
        for item in schedule:
            (dateDict[f'{item["DateLesson"]}']).append(item)
        dateDict = dict(sorted(dateDict.items()))
        text = ""
        for item in dateDict.keys():
            date = formatDate(datetime.strptime(dateDict[f'{item}'][0]['DateLesson'], '%Y-%m-%d'))
            text += "--------------------------------------------------------------------------------------------------"
            text += "\n\n<b>" + f"📅{date} ({day[dateDict[f'{item}'][0]['DayWeek']-1]})" + "</b>" + "\n"
            for lesson in dateDict[item]:
                text += "\n" + "🕮" + "<b>" + f"{lesson['TitleSubject']}({lesson['TypeLesson']})" + "</b>" + "\n" \
                + "🕰" + "<b>" + f"{TimeTableMain[lesson['NumberLesson']-1]}" + "</b>" + "\n" \
                    + "👤" + f"{lesson['Family']} {lesson['Name']} {lesson['SecondName']}" + "\n" \
                        + '🚪' + "<b>" + f"{lesson['Korpus']}-{lesson['NumberRoom']}" + "</b>" + "\n\n" 
        text += "--------------------------------------------------------------------------------------------------"
        return text
    except:
        return "Расписание не найдено"
    
########################################### Classroom Day Schedule ################################################ 

def getClassroomOnDate(user_id, date):
    try:   
        data.setKorpus((db[f'class_{user_id}'])[1])
        data.setClassroom(classroomNumber=(db[f'class_{user_id}'])[0])
        schedule = data.getClassroomSchedule(date=date)
        date = formatDate(date)
        text = "<b>" + f'📅{date} ({day[schedule[0]["DayWeek"]-1]})' + "</b>"
        for item in schedule:
            text += "\n\n" + "🕮" + "<b>" + f"{item['TitleSubject']}({item['TypeLesson']})" + "</b>" + "\n" \
                + "🕰" + "<b>" + f"{TimeTableMain[item['NumberLesson']-1]}" + "</b>" + "\n" \
                    + "👤" + f"{item['Family']} {item['Name']} {item['SecondName']}" + "\n" \
                        + '🚪' + "<b>" + f"{item['Korpus']}-{item['NumberRoom']}" + "</b>"
        return text
    except:
        return "Расписание не найдено"