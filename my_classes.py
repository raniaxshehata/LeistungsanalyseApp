import requests #aufgabe8: die Bib. wird verwendet um http-anfragen zu senden
import json
from datetime import datetime

class Person:
  def __init__(self, first_name, last_name, sex, birthday):
      self.first_name = first_name #vorname reicht...
      """self.last_name = last_name
      self.sex = sex
     # self.age = age
      self.__birthday = birthday #verstecktes Attribut: Geburtsdatum (noch von aufgabe 6.2"""

  """def estimate_max_hr(self):
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
      super().__init__(first_name, last_name, sex, age, birthday)"""

	def put(self):
  	data = {"first_name": self.first_name} #neue person auf dem server anlegen 
  	response = requests.post(f"http://edanur-aufgabe8-webserver-url/persons/", json = data) #post-requests an die angegebene url mit den daten senden
		if response.status_code == 201: #statuscode der antwort überprüfen
    	print("new person is successfully added") #wenn der statuscode == 201 dann wird gemeldet, dass die neue person erfolgreich hinzugefügt wurde
  	else:
    	print("failed to add a new person") #andernfalls wird gemeldet, dass es beim hinzufügen einer neuen person fehler gibt  
  
  
class Subject(Person):
  def __init__(self, first_name, last_name, sex, age, birthday):
      super().__init__(first_name, last_name, sex, age, birthday) #super() habe ich hier verwendet, um die __init__ Methode von der Elternklasse 'Person' von den Unterklassen 'Subject' und Sup. aufzurufen, ohne den Code zu dupliziern


	def update_email(self):
  	data = {"Email": self.email} #dict mit der email adresse erstellen
  	response = requests.post(f"http://edanur-aufgabe8-webserver-url/persons/{self.first_name}/update_email", json = data) #post-requests an die angegebene url mit den daten senden
		if response.status_code == 200: #statuscode der antwort überprüfen
   	 print("Email is updated successfully.") #wenn der statuscode == 20 dann wird gemeldet, dass die email erfolgreich aktualisiert wurde
  	else:
   	 print("failed to update email") #andernfalls wird gemeldet, dass die email nicht erfolgr. aktualisiert wurde  
  
class Experiment:
  def __init__(self, eperiment_name, date, supervisor, subject):
    self.experiment_name = experiment_name
    self.date = date
    self.supervisor = supervisor
    self.subject = subject
      
    def save(self):
        with open('experiment.json', 'w') as f:
          json.dump(self.__dict__, f)

#http-statuscode 200 bedeutet OK um zu zeigen dass der rest-anruf erfolgreich war und keine fehler aufgetreten sind
#http-statuscode 201 bedeutet created: um zu zeigen, dass ein neuer ressourcen eintrag erfolgreich erstellt wurde. --> wenn ein post anruf erfolgreich war und eine neue ressource auf dem server erstellt wurde



  
