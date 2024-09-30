from os import makedirs, path
from random import randint, sample


from file_operations import render_template
from faker import Faker


from char_skills import SKILLS, beautiful_letters


FAKE_DATA = Faker("ru_RU")


def fill_char_form():

    faker_male = FAKE_DATA.name_male()
    faker_city = FAKE_DATA.address()
    faker_job = FAKE_DATA.job()

    fake_name = faker_male.split(" ")
    city = faker_city.split(",")
    name, last_name, _ = fake_name

    beauty_letter = decorate_letter()
    sampled_skills = sample(beauty_letter, len(beauty_letter))
    context = {
        "first_name": name,
        "last_name": last_name,
        "town": city[0],
        "job": faker_job,
        "strength": randint(1, 18),
        "agility": randint(1, 18),
        "endurance": randint(1, 18),
        "intelligence": randint(1, 18),
        "luck": randint(1, 18),
        "skill_1": sampled_skills[0],
        "skill_2": sampled_skills[1],
        "skill_3": sampled_skills[3],
    }

    return context


def decorate_letter():
    skills_with_beauty_letter = []
    for skill in SKILLS:
        new_skill = ""

        for letter in skill:
            if letter in beautiful_letters:
                new_skill += letter.replace(letter, beautiful_letters[letter])

        skills_with_beauty_letter.append(new_skill)
    return skills_with_beauty_letter


if __name__ == "__main__":
    makedirs("cards", exist_ok=True)
    for numb in range(1, 11):
        render_template(
            template_path=path.join("card_template", "charsheet.svg"),
            output_path=path.join(
                "cards", f"charsheet{numb}.svg"
                ),
            context=fill_char_form())
