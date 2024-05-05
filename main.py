import requests
import json

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    def put(self):
        url = 'http://example.com/api/person'
        data = {'first_name': self.first_name}
        response = requests.post(url, json=data)
        return response

class Subject(Person):
    def __init__(self, first_name, email=None):
        super().__init__(first_name)
        self.email = email

    def update_email(self, new_email):
        self.email = new_email
        url = f'http://example.com/api/person/{self.first_name}/update_email'
        data = {'email': self.email}
        response = requests.post(url, json=data)
        return response

# Weil Supervisor und Experiment vom Ursprungsskript abhängen, ändern wir diese nicht.
