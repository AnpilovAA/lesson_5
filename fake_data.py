from faker import Faker


FAKE = Faker("ru_RU")

faker_male = FAKE.name_male()
faker_city = FAKE.address()
faker_job = FAKE.job()
