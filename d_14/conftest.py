import pytest

from d_14.human import Human


@pytest.fixture(scope='function')
def create_human():
    human = Human('Anna', 20, 'female')
    yield human
    print('Pass')


@pytest.fixture
def create_human_with_custom_params():
    def __create_human(name, age, gender):
        human = Human(name=name, age=age, gender=gender)
        return human

    return __create_human
