import json

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
    supervisor = build_person(supervisor_first_name, supervisor_last_name, supervisor_sex, supervisor_age)
    subject_first_name = input("Enter subject's first name: ")
    subject_last_name = input("Enter subject's last name: ")
    subject_sex = input("Enter subject's sex (male/female): ")
    subject_age = int(input("Enter subject's age: "))
    subject = build_person(subject_first_name, subject_last_name, subject_sex, subject_age)
    return build_experiment(experiment_name, date, supervisor, subject)

# Hauptfunktion, um das Experiment zu erstellen und in einer Datei zu speichern
def main():
    experiment = get_experiment_details()
    # Schreibe das Experiment in eine JSON-Datei
    with open("experiment.json", "w") as outfile:
        json.dump(experiment, outfile)

if __name__ == "__main__":
    main()
