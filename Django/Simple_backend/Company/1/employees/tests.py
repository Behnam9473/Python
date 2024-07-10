# person/tests.py
from django.test import TestCase
from .models import Person
from companies.models import Companies

class PersonModelTest(TestCase):

    def setUp(self):
        self.company = Companies.objects.create(name="Test Company", address="123 Test Street", website="http://test.com")
        self.person = Person.objects.create(
            first_name='John',
            last_name='Doe',
            contact_number='1234567890',
            email='john.doe@example.com',
            photo='photos/john_doe.jpg',
            company=self.company
        )
    
    def test_person_creation(self):
        self.assertEqual(self.person.first_name, 'John')
        self.assertEqual(self.person.last_name, 'Doe')
        self.assertEqual(self.person.contact_number, '1234567890')
        self.assertEqual(self.person.email, 'john.doe@example.com')
        self.assertEqual(self.person.photo, 'photos/john_doe.jpg')
        self.assertEqual(self.person.company.name, 'Test Company')
        self.assertEqual(str(self.person), 'John Doe')

    def test_person_str_method(self):
        self.assertEqual(str(self.person), 'John Doe')

    def test_person_company_relationship(self):
        self.assertEqual(self.person.company, self.company)
        self.assertEqual(self.company.employees.count(), 1)
        self.assertEqual(self.company.employees.first(), self.person)
