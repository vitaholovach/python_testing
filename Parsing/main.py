import json
import xmltodict


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        return json.dumps(self.__dict__)

    def convert_to_xml(self):
        return xmltodict.unparse({"Human": self.__dict__})


human = Human('Vita', 28, 'female', 1994)
result = human.convert_to_json()
with open("human.json", "w") as json_file:
    json_file.write(result)
