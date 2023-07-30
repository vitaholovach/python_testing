import pytest

from hw_task_14.human import Human


def test_grow_human():
    human = Human("Nik", 29, "male")
    human.grow()
    assert human.age == 30, "Age increased by 1"


def test_change_gender_human():
    human = Human("Anna", 26, "female")
    human.change_gender("male")
    assert human.gender == "male", "Gender hasn't changed"


def test_age_human_property():
    human = Human("Ivan", 50, "male")
    assert human.age == 50, "Value is incorrect, age is not 50"
    human.grow()
    assert human.age == 51, "Human does not grow"


def test_gender_human_property():
    human = Human("Rich", 25, "female")
    assert human.gender == "female", "Incorrect value"
    human.change_gender("male")
    assert human.gender == "male", "Gender is not changed"


def test_grow_human_1():
    human = Human("Nik", 30, "male")
    human.grow()
    assert human.age == 31, "Age is not incremented by 1 after calling grow()"


def test_change_gender_human_1():
    human = Human("Anna", 25, "female")
    human.change_gender("male")
    assert human.gender == "male", "Gender is not changed to 'male' after calling change_gender()"


def test_change_gender_human_already_same():
    human = Human("Alice", 40, "female")
    with pytest.raises(Exception):
        human.change_gender("female"), "Exception is not raised when changing to the same gender"
    assert human.gender == "female", "Gender is changed even when attempting to set the same gender"


def test_change_gender_human_invalid():
    human = Human("Bob", 35, "male")
    with pytest.raises(Exception):
        human.change_gender("invalid_gender"), "Exception is not raised when changing to an invalid gender"
    assert 'invalid_gender' != 'male' or 'female', 'Not available Gender'


def test_age_property_human_1():
    human = Human("Ivan", 50, "male")
    assert human.age == 50, "Age property does not return the correct initial age"
    human.grow()
    assert human.age == 51, "Age property does not reflect the incremented age after calling grow()"


def test_dead_human():
    human = Human("Ron", 100, "male")
    human.grow()
    assert human.age == 100, "The age is increased, 100 the biggest Age for Human class"
