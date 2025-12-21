from datetime import datetime


def create_user(first_name, last_name, birth_year, email):
    if not first_name or not last_name:
        raise ValueError("Le prénom et le nom sont obligatoires")

    if not is_valid_email(email):
        raise ValueError("Email invalide")

    age = calculate_age(birth_year)

    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "email": email,
        "is_adult": is_adult(age)
    }


def calculate_age(birth_year):
    current_year = datetime.now().year

    if birth_year > current_year:
        raise ValueError("Année de naissance invalide")

    return current_year - birth_year


def is_adult(age):
    return age >= 18


def is_valid_email(email):
    return "@" in email and "." in email
