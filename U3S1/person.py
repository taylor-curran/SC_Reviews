class Person:
    def __init__(self, name, age, height, profession, ages=[], promotion_level=1):
        self.name = str(name)
        self.age = float(age)
        self.height = float(height)
        self.profession = str(profession)
        self.ages = ages
        self.promotion_level = promotion_level

        if self.age < 0 or self.age > 120:
            self.age = 21
    
    def greets(self, other_name):
        return f'Hello, {other_name}! My name is {self.name}, nice to meet you!'

    def had_birthday(self):
        # self.age = self.age + 1
        self.ages.append(self.age)
        self.age += 1
    
    def all_ages(self):
        return self.ages

    def got_promotion(self):
        if "Senior" not in self.profession:
            self.profession = f'Senior {self.profession}'
        elif "Senior" in self.profession and "Super" not in self.profession:
            self.profession = f'Super {self.profession}'
        else:
            self.promotion_level += 1
            # self.profession = f'{self.profession}'
        
        return f'{self.profession} ^{self.promotion_level}'

class Worker(Person):
    def __init__(self, name, age, height, profession, 
                 company, job_title, personal_title, 
                 years_worked, salary, ages=[], 
                 promotion_level=1):
        super().__init__(name, age, height, profession, ages=[], 
                         promotion_level=1)
        self.company = company 
        self.job_title = job_title
        self.personal_title = personal_title
        self.years_worked = years_worked
        self.salary = salary

    def greets(self, personal_title, name):
        return f'Hello, {personal_title} {name}! My name is {self.name}, I work for {self.company}.'

    def salary_increase(self, percentage):
        increase = percentage * self.salary 
        self.salary += increase
        return f"Congratulations! You are now making {self.salary}"




    
    

