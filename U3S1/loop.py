import random 

from person import Person

names = ['Anika', 'Nick', 'William', 'Dakota', 'Bobby', 'Taylor', 'James']
professions = ['Engineer', 'Nurse', 'Comedian', 'Clown', 'Lawyer', 'Voice Actor', 'Data Scientist']

def loop(count=10):

    people = []

    while count > 0:
        name = random.choice(names)
        age = random.randrange(0, 120, 1)
        height = random.randrange(0, 625, 1)
        profession = random.choice(professions)

        person = Person(name, age, height, profession)
        people.append(person)

        count -= 1

    return people


if __name__ == '__main__':
    people_list = loop()

    ages = []

    for people in people_list:
        ages.append(people.age)

    oldest_age = max(ages)

    oldest_idx = ages.index(oldest_age)

    print(people_list[oldest_idx].name)




    


