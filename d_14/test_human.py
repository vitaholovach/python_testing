import pytest


@pytest.mark.smoke
def test_grow(create_human):
    human = create_human
    new_age = human.age + 1
    human.grow()
    assert human.age == new_age, 'Age did not change'


def test_grow_not_allowed(create_human_with_custom_params):
    human = create_human_with_custom_params('Olena', 100, 'female')
    new_age = 100
    human.grow()
    assert human.age == new_age, 'Age was changed for age 100.'


def test_is_alive_private(create_human):
    human = create_human
    with pytest.raises(AttributeError):
        human.__is_alive


@pytest.mark.smoke
def test_validate_gender(create_human):
    human = create_human
    assert human.gender in ['male', 'female'], 'Gender is not out of the following range ["male", "female"]'


def test_validate_gender_exception(create_human_with_custom_params):
    human = create_human_with_custom_params('Olena', 23, 'binary')
    with pytest.raises(Exception, match='Not correct name of gender'):
        human.change_gender('bi')


def test_is_int_age(create_human):
    human = create_human
    assert type(human.age) == int, 'Age is not int.'


def test_is_str_gender(create_human):
    human = create_human
    assert type(human.gender) == str, 'Gender is not string.'


@pytest.mark.smoke
def test_gender_change(create_human):
    human = create_human
    new_gender = 'male'
    human.change_gender('male')
    assert human.gender == new_gender, 'Gender was not changed.'


def test_gender_change_is_forbidden(create_human_with_custom_params):
    human = create_human_with_custom_params('Olena', 20, 'female')
    with pytest.raises(Exception, match=f"Olena already has gender '{human.gender}'"):
        human.change_gender('female')


def test_age_limit_is_valid(create_human):
    human = create_human
    with pytest.raises(AttributeError):
        human.__age_limit != 100
