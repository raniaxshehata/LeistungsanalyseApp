import json
import requests
from datetime import datetime

class Person:
    def __init__(self, first_name, last_name, sex, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self._birthdate = birthdate

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

    def put(self):
