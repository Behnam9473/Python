"""
The Builder pattern is used when:

The construction process of an object is complex and involves multiple steps.
The object to be created can have various representations or configurations.
You need to separate the construction of a complex object from its representation.


All properties of the builder pattern must be configured step-by-step
"""
# Below is a 1D Builder class which literily use ONE bulder to create an object
#===================BUT==============What if the objct is too complex to be created in one bulider?

# class Person:
#     def __init__(self):
#         self.name = None
#         self.position = None
#         self.date_of_birth = None

#     def __str__(self):
#         return f'{self.name} born on {self.date_of_birth} works as a {self.position}'

#     @staticmethod
#     def new():
#         return PersonDateBuilder()

# class PersonBuilder:
#     def __init__(self):
#         self.person = Person()

#     def build(self):
#         return self.person


# class PersonInfoBuilder(PersonBuilder):
#     def called(self, name):
#         self.person.name = name
#         return self


# class PersonJobBuilder(PersonInfoBuilder):
#     def works_as_a(self, position):
#         self.person.position = position
#         return self


# class PersonDateBuilder(PersonJobBuilder):
#     def born(self, date_of_birth):
#         self.person.date_of_birth = date_of_birth
#         return self


# if __name__ == '__main__':
#     pb = Person.new()
#     me = pb\
#         .called('Dmitri')\
#         .works_as_a('quant')\
#         .born('1/1/1980')\
#         .build()  
#     print(me)


# Thats how Two builders are created

class TwoBuilderPerson:
    def __init__(self):
        print('Creating an instance of Person')

        # ID 
        self.name = None
        self.surname = None
        self.id_number = None
        
        # address
        
        self.street = None
        self.city = None
        self.country = None
        
    def __str__(self):

        return f'Name: {self.name}, lastname: {self.surname} ID number: {self.id_number}\n' +\
                f'Street: {self.street}, City: {self.city}, country: {self.country}'
                     
class PersonBuilder:
    def __init__(self, person = TwoBuilderPerson()):
        self.person = person
        
    @property
    def creat_person(self):
        return PersonIdBuilder(self.person)
    
    @property
    def lives(self):
        return PersonAdrressbuiler(self.person)
        
    def bulid(self):
        return self.person
    
    
class PersonIdBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)
        
    def name(self, name):
        self.person.name = name
        return self
    def surname(self, surname):
        self.person.surname = surname
        return self
    
    def id_number(self, id_number):
        self.person.id_number = id_number
        return self
        
        
class PersonAdrressbuiler(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)
        
    def street(self, street):
        self.person.street = street
        return self
    def city(self, city):
        self.person.city = city
        return self
    def country(self, country):
        self.person.country = country
        return self
        
        
if __name__ == '__main__':
   
    pb = PersonBuilder()
    person_lives = pb\
            .lives\
                .street("street")\
                .city("city")\
                .country("country")\
            .creat_person\
                .name("person")\
                .surname("lastname")\
                .id_number(111)\
            .bulid()
        
print(person_lives)
