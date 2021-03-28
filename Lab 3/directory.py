import os.path
import json
from json import JSONEncoder
from types import SimpleNamespace
import collections
import re


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class Contact():
    def set_name(self, name):
        if str.isalpha(name):
            self._name = name
        else:
            raise ValueError

    def set_email(self, email):
        if re.match(r"\S+@\S+", email):
            self._email = email
        else:
            raise ValueError

    def set_age(self, age):
        if str.isdigit(age):
            self._age = age
        else:
            raise ValueError

    def set_country(self, country):
        if str.isalpha(country):
            self._country = country
        else:
            raise ValueError

    def __init__(self, name, email, age, country):
        self.set_name(name)
        self.set_email(email)
        self.set_age(age)
        self.set_country(country)

    def __eq__(self, other):
        if self._name == other._name and self._email == other._email and self._age == other._age and self._country == other._country:
            return True
        else:
            return False


class Directory():
    def add_contact(self, name, email, age, country):
        self._directory[email] = Contact(name, email, age, country)

    def __init__(self, file):
        self._directory = {}
        self._file = file
        if not os.path.isfile(file):
            return

        self.load()

    def save(self):
        with open(self._file, "w+") as f:
            json.dump(self._directory, f, cls=MyEncoder)

    def load(self):
        with open(self._file, "r+") as f:
            self._dict_to_dir(json.loads(f.read()))

    def _dict_to_dir(self, dict):
        for _, elem in dict.items():
            self.add_contact(elem["_name"], elem["_email"], elem["_age"], elem["_country"])

    def parse_dir(self):
        fmt = "|{:^15}|{:^15}|{:^15}|{:^15}|\n"
        plist = fmt.format("NAME", "MAIL", "AGE", "COUNTRY")
        for _, elem in self._directory.items():
            plist = plist + fmt.format(elem._name, elem._email, elem._age, elem._country)
        return plist

    def print_directory(self):
        print(self.parse_dir())

    def search_by_age(self, age):
        age = str(age)
        results = []
        for _, elem in self._directory.items():
            if elem._age == age:
                results.append(elem)
        return results

    def search_by_email(self, email):
        return self._directory[email]
