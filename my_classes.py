import json
from datetime import datetime

class Person:
    def __init__(self, first_name, last_name, sex, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self._birthdate = birthdate
#verstecktes Geburtsdarum
    def estimate_max_hr(self):
        if self._sex == "male":
            max_hr_bpm = 223 - 0.9 * self._calculate_age()
        elif self._sex == "female":
            max_hr_bpm = 226 - 1.0 * self._calculate_age()
        else:
            max_hr_bpm = int(input("Enter maximum heart rate:"))
        return max_hr_bpm

    def _calculate_age(self):
        today = datetime.today()
        birthdate = datetime.strptime(self._birthdate, "%Y-%m-%d")
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

    def save(self):
        with open('person.json', 'w') as f:
            json.dump(self.__dict__, f)


class Subject(Person):
    def __init__(self, first_name, last_name, sex, birthdate, experiment_name, date, supervisor):
        super().__init__(first_name, last_name, sex, birthdate)
        self._experiment_name = experiment_name
        self._date = date
        self._supervisor = supervisor

    def save(self):
        with open('subject.json', 'w') as f:
            json.dump(self.__dict__, f)

class Supervisor(Person):
    def __init__(self, first_name, last_name, sex, birthdate, department):
        super().__init__(first_name, last_name, sex, birthdate)
        self._department = department

    def save(self):
        with open('supervisor.json', 'w') as f:
            json.dump(self.__dict__, f)

class Experiment:
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def save(self):
        with open('experiment.json', 'w') as f:
            json.dump(self.__dict__, f)
