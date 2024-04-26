import json
from datetime import datetime
from my_classes import Subject, Supervisor, Experiment  # Annahme: Diese Klassen wurden wie besprochen angelegt
#build_person und estimate_max_hr Funktionen entfernt( in Klassen integriert) -> nutzt _birthdate um das Alter der Person zu berechnen und daraufhin die maximale Herzrate zu schätzen

def get_experiment_details():
    experiment_name = input("Enter experiment name: ")
    date = input("Enter date of experiment (YYYY-MM-DD): ")

    supervisor_first_name = input("Enter supervisor's first name: ")
    supervisor_last_name = input("Enter supervisor's last name: ")
    supervisor_sex = input("Enter supervisor's sex (male/female): ")
    supervisor_birthdate = input("Enter supervisor's birthdate (YYYY-MM-DD): ")
    supervisor = Supervisor(supervisor_first_name, supervisor_last_name, supervisor_sex, supervisor_birthdate)

    subject_first_name = input("Enter subject's first name: ")
    subject_last_name = input("Enter subject's last name: ")
    subject_sex = input("Enter subject's sex (male/female): ")
    subject_birthdate = input("Enter subject's birthdate (YYYY-MM-DD): ")
    subject = Subject(subject_first_name, subject_last_name, subject_sex, subject_birthdate, experiment_name, date, supervisor)

    return Experiment(experiment_name, date, supervisor, subject)

# Experiment erstellen, als Datei speichern
def main():
    experiment = get_experiment_details()
    # JSON-Datei
    with open("experiment.json", "w") as outfile:
        json.dump({
            "experiment_name": experiment.experiment_name,
            "date": experiment.date,
            "supervisor": {
                "first_name": experiment.supervisor._first_name,
                "last_name": experiment.supervisor._last_name,
                "sex": experiment.supervisor._sex,
                "birthdate": experiment.supervisor._birthdate
            },
            "subject": {
                "first_name": experiment.subject._first_name,
                "last_name": experiment.subject._last_name,
                "sex": experiment.subject._sex,
                "birthdate": experiment.subject._birthdate,
                "experiment_name": experiment.subject._experiment_name,
                "date": experiment.subject._date,
                "supervisor": {
                    "first_name": experiment.subject._supervisor._first_name,
                    "last_name": experiment.subject._supervisor._last_name
                }
            }
        }, outfile, indent=4)

if __name__ == "__main__":
    main()
