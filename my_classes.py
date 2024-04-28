import json
from datetime import datetime

class Person:
  def __init__(self, first_name, last_name, sex, birthday):
      self.first_name = first_name
      self.last_name = last_name
      self.sex = sex
     # self.age = age
      self.__birthday = birthday #verstecktes Attribut: Geburtsdatum

  def estimate_max_hr(self):
      if self.sex == "male":
        max_hr_bpm = 223 - 0.9 * self._get_age()
      elif self.sex == "female":
        max_hr_bpm = 226 - 1.0 * self._get_age()
      else:
        max_hr_bpm = int(input("Enter maximum heart rate:"))
      return max_hr_bpm

  def _get_age(self): #Berechnung: Alter der Person basierend auf dem GBdat.
    current_date = datetime.today()
    birthday = datetime.strptime(self._birthday, "%Y-%m-%d") #strptime, um String in ein Datum zu konvertieren mit dem Format y-m-d
    age = current_date.year - birthday.year ((current_date.month, current_date.day) < (birthday.month, birthday.day)) #nachdem jahr gbd vom akt. jahr subtrahiert wird, wird überprüft, ob der akt. monat und day vor dem gbd und day liegt. ja: wird ein zusätzliches jahr subtr., da die person gbd in diesem jahr noch nicht erreicht hat
    return age

  def save(self):
      with open('person.json', 'w') as f:
          json.dump(self.__dict__, f)
        
class Subject(Person):
  def __init__(self, first_name, last_name, sex, age, birthday):
      super().__init__(first_name, last_name, sex, age, birthday) #super() habe ich hier verwendet, um die __init__ Methode von der Elternklasse 'Person' von den Unterklassen 'Subject' und Sup. aufzurufen, ohne den Code zu dupliziern

class Supervisor(Person):
  def __init__(self, first_name, last_name, sex, age, birthday):
      super().__init__(first_name, last_name, sex, age, birthday)

class Experiment:
  def __init__(self, eperiment_name, date, supervisor, subject):
    self.experiment_name = experiment_name
    self.date = date
    self.supervisor = supervisor
    self.subject = subject
      
    def save(self):
        with open('experiment.json', 'w') as f:
          json.dump(self.__dict__, f)



  
