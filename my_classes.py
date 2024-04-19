import jason

class Person:
  def __init__(self, first_name, last_name, sex, age):
      self.first_name = first_name
      self.last_name = last_name
      self.sex = sex
      self.age = age

  def estimate_max_hr(self):
    if self.sex == "male":
        max_hr_bpm = 223 - 0.9 * self.age
    elif self.sex == "female":
        max_hr_bpm = 226 - 1.0 * self.age
    else:
        max_hr_bpm = int(input("Enter maximum heart rate:"))
    return max_hr_bpm

  def save(self):
      with open('person.json', 'w') as f:
          json.dump(self.__dict__, f)


class Experiment:
    def __init__(self, eperiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject
      
    def save(self):
        with open('experiment.json', 'w') as f:
          json.dump(self.__dict__, f)



  
