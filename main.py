from os import listdir, makedirs, getcwd
from random import randint, choice, sample


from file_operations import render_template


from fake_data import faker_male, faker_city, faker_job
from char_skills import SKILLS, beautiful_letters


def fill_char_form():
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
        "skill_1": choice(sampled_skills),
        "skill_2": choice(sampled_skills),
        "skill_3": choice(sampled_skills),
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


def dir_for_char() -> str:
    folder_name = "chars"

    if folder_name in listdir(getcwd()):
        return folder_name
    else:
        makedirs(folder_name)
        return folder_name


if __name__ == "__main__":
    for numb in range(1, 11):
        render_template(template_path=r'cart_template\charsheet.svg',
                        output_path=fr"{dir_for_char()}\charsheet{numb}.svg",
                        context=fill_char_form())
