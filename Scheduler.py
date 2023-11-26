
from fake_useragent import UserAgent
import requests
from datetime import datetime, timedelta
import time

class Scheduler():
    def __init__(self):
        self.facultyDictionary()
        
    ua = UserAgent()
    
    #################################### Settings ######################################
    
    def facultyDictionary(self):
        data = requests.get(
            url= f'https://oreluniver.ru/schedule/divisionlistforstuds', 
            headers={
                'User-Agent': self.ua.random
            }
        ).json()
        self.__faculty = {item['shortTitle']: item['idDivision'] for item in data} 
    
    def getfacultyDictionary(self):
        return self.__faculty
    
    def setDivisionID(self, facultyTitle):
        self.__divisionID = self.__faculty[facultyTitle]
        
    def getDivisionID(self):
        return self.__divisionID
    
    ###############
    
    def courseList(self):
        data = requests.get(
            url= f'https://oreluniver.ru/schedule/{self.__divisionID}/kurslist', 
            headers={
                'User-Agent': self.ua.random
            }
        ).json()
        self.__course = [course['kurs'] for course in data]  
        
    def getCourseList(self):
        return self.__course
        
    def setCourse(self, course):
        self.__course = course
        
    ###############
    
    def groupDict(self):
        data = requests.get(
            url= f'https://oreluniver.ru/schedule/{self.__divisionID}/{self.__course}/grouplist', 
            headers={
                'User-Agent': self.ua.random
            }
        ).json()
        self.__group = {item['title']: item['idgruop'] for item in data}
        
    def getGroup(self) -> dict["title": "groupID"]:
        return self.__group
    
    def setGroupID(self, title=None, groupID=None):
        self.__groupID = self.__group[f'{title}'] if title else groupID
        
    def getGroupID(self) -> int: 
        return self.__groupID
    
    ###############
    
    def getTime(self, date: datetime):
        now = date
        weekStart = now - timedelta(days=date.weekday())
        weekStart = weekStart.replace(hour=0, minute=0, second=0, microsecond=0)
        weekStartMillis = int(time.mktime(weekStart.timetuple())) * 1000
        return weekStartMillis
    
    #################################### Schedule ######################################
    def schedule(self, date: datetime):
        data = requests.get(
            url= f'https://oreluniver.ru/schedule//{self.__groupID}///{self.getTime(date)}/printschedule', 
            headers={
                'User-Agent': self.ua.random
            }
        ).json()
        self.__schedule = [item for item in data.values()][:-2]
        
    def getSchedule(self, date=datetime.now(), week=False) -> list[dict]:
        self.schedule(date)
        if week == True:
            return self.__schedule
        else:
            schedule = []
            date = f'{date.strftime("%Y-%m-%d")}'
            for item in self.__schedule:
                if item['DateLesson'] == date:
                    schedule.append(item)
            return schedule
        
    #################################### Exam Schedule ######################################
        
    def examSchedule(self):
        data = requests.get(
            url= f'https://oreluniver.ru/schedule/{self.getGroupID()}////printexamschedule', 
            headers={
                'User-Agent': self.ua.random
            }
        ).json()
        self.__exam = [item for item in data]
        
    def getExamSchedule(self):
        return self.__exam 
    
    
    #################################### Professor ######################################
    
    def kafedra(self):
        data = requests.get(
            url= f'https://oreluniver.ru/schedule/{self.__divisionID}/kaflist', 
            headers={
                'User-Agent': self.ua.random
            }
        ).json()
        self.__kafedra = {item['shortTitle']: item['idDivision'] for item in data}
        
    def getKafedra(self) -> dict:
        return self.__kafedra
    
    def setKafedra(self, title):
        self.__kafedraID = self.__kafedra[f'{title}']
        
    def getKafedraID(self):
        return self.__kafedraID
    
    ###############

    def professor(self) -> dict:
        data = requests.get(
            url= f'https://oreluniver.ru/schedule/{self.getKafedraID()}/preplist', 
            headers={
                'User-Agent': self.ua.random
            }
        ).json()
        self.__professor = {item['fio']: item['employee_id'] for item in data}
        
    def getProfessorList(self):
        return self.__professor
        
    def setProfessor(self, fullName=None, prof_id=None):
        self.__professorID = self.__professor[f'{fullName}'] if fullName != None else prof_id
        
    def getProfessorID(self):
        return self.__professorID
    
    ###############
    
    def professorSchedule(self, date: datetime):
        data = requests.get(
            url= f'https://oreluniver.ru/schedule/{self.__professorID}////{self.getTime(date)}/printschedule', 
            headers={
                'User-Agent': self.ua.random
            }
        ).json()
        self.__professorSchedule = [item for item in data.values()][:-2]
        
    def getProfessorSchedule(self, date=datetime.now(), week=False):
        self.professorSchedule(date)
        if week == True:
            return self.__professorSchedule
        else:
            schedule = []
            date = str(date.strftime("%Y-%m-%d"))
            for item in self.__professorSchedule:
                if item['DateLesson'] == date:
                    schedule.append(item)
            return schedule
    
    #################################### Сlassrooms ######################################
    def getKorpusList(self):
        return ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '11', '12', '13', '15', '16', '17']
    
    def setKorpus(self, korpusNumber):
        self.__korpus = str(korpusNumber)
        
    def getKorpus(self):
        return self.__korpus
    
    ###############
    
    def classromList(self):
        data = requests.get(
            url=f'https://oreluniver.ru/schedule/{self.getKorpus()}/auditlist',
            headers={
                'User-Agent': self.ua.random
            }
        ).json()
        self.__classrooms = [item['NumberRoom'] for item in data]
        
    def getClassromList(self):
        return self.__classrooms
        
    def setClassroom(self, classroomNumber):
        self.__classroomNumber = str(classroomNumber)
        
    def getClassroomNumber(self):
        return self.__classroomNumber
    
    ###############
    
    def classroomSchedule(self, date):
        data = requests.get(
            url= f'https://oreluniver.ru/schedule///{self.getKorpus()}/{str(self.getClassroomNumber())}/{self.getTime(date)}/printschedule',
            headers={
                'User-Agent': self.ua.random
            }
        ).json()
        self.__classroomSchedule = ([item for item in data.values()])[:-2]
        
    def getClassroomSchedule(self, date=datetime.now()) -> list[dict]:
        self.classroomSchedule(date)
        schedule = []
        date = f'{date.strftime("%Y-%m-%d")}'
        for item in self.__classroomSchedule:
            if item['DateLesson'] == date:
                schedule.append(item)
        return schedule
    
if __name__ == '__main__':
    pass