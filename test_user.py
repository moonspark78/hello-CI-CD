import pytest
from user import (
    create_user,
    calculate_age,
    is_adult,
    is_valid_email
)


def test_create_user_success():
    user = create_user(
        first_name="Matis",
        last_name="Dupond",
        birth_year=2000,
        email="matis@test.com"
    )

    assert user["first_name"] == "Matis"
    assert user["last_name"] == "Dupond"
    assert user["is_adult"] is True


def test_create_user_invalid_email():
    with pytest.raises(ValueError):
        create_user(
            first_name="Matis",
            last_name="Dupond",
            birth_year=2000,
            email="email-invalide"
        )


def test_calculate_age():
    age = calculate_age(2000)
    assert age > 20

def test_create_user_missing_name():
    with pytest.raises(ValueError):
        create_user(
            first_name="",
            last_name="Dupond",
            birth_year=2000,
            email="",
        )

def test_calculate_age_future_year():
    with pytest.raises(ValueError):
        calculate_age(3000)


def test_is_adult():
    assert is_adult(18) is True
    assert is_adult(17) is False


def test_email_validation():
    assert is_valid_email("test@mail.com") is True
    assert is_valid_email("testmail.com") is False
