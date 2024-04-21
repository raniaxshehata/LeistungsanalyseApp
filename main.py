import json
from my_classes import Person, Experiment #für die Aufgabe 6.1 importieren, um die Klassen hier zu verwenden.

# Definition der Funktionen estimate_max_hr und build_person aus deinem vorhandenen Code

def estimate_max_hr(age_years: int, sex: str) -> int:
    if sex == "male":
        max_hr_bpm = 223 - 0.9 * age_years
    elif sex == "female":
        max_hr_bpm = 226 - 1.0 * age_years
    else:
        max_hr_bpm = int(input("Enter maximum heart rate:"))
    return int(max_hr_bpm)

def build_person(first_name, last_name, sex, age) -> dict:
    person_dict = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "estimate_max_hr": estimate_max_hr(age, sex)
    }
    return person_dict

def build_experiment(experiment_name, date, supervisor, subject) -> dict:
    experiment_dict = {
        "experiment_name": experiment_name,
        "date": date,
        "supervisor": supervisor,
        "subject": subject
    }
    return experiment_dict

# Funktion, um Benutzereingaben für ein Experiment zu erhalten
def get_experiment_details():
    experiment_name = input("Enter experiment name: ")
    date = input("Enter date of experiment (YYYY-MM-DD): ")
    supervisor_first_name = input("Enter supervisor's first name: ")
    supervisor_last_name = input("Enter supervisor's last name: ")
    supervisor_sex = input("Enter supervisor's sex (male/female): ")
    supervisor_age = int(input("Enter supervisor's age: "))
    supervisor = Person(supervisor_first_name, supervisor_last_name, supervisor_sex, supervisor_age)
    subject_first_name = input("Enter subject's first name: ")
    subject_last_name = input("Enter subject's last name: ")
    subject_sex = input("Enter subject's sex (male/female): ")
    subject_age = int(input("Enter subject's age: "))
    subject = Person(subject_first_name, subject_last_name, subject_sex, subject_age)
    return Experiment(experiment_name, date, supervisor, subject)
#build_person/build_experiment (um ein Wörterbuch zu erstellen, dass die Attribute einer Person/Experiment enthält), haben wir mit den Klassen 'Person' 'Experiment', die deren Attribute direkt als Eigenschaften haben, ersetzt.
#Experiment erstellen, als Datei speichern
def main():
    experiment = get_experiment_details()
    #JSON-Datei
    with open("experiment.json", "w") as outfile:
        json.dump(experiment.__dict__, outfile)

if __name__ == "__main__":
    main()

