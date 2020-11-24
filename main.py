from peewee import *
from datetime import date

db = PostgresqlDatabase('contacts', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Contacts(BaseModel):
    first_name = CharField()
    last_name = CharField()
    number = CharField()
    birthday = DateField()

db.drop_tables([Contacts])
db.create_tables([Contacts])


mother = Contacts(first_name='MaDukes', last_name='Mcdermott', number='336-555-0123' ,birthday=date(1974, 7, 28))
mother.save()
# print("Working")

aunty = Contacts(first_name='Redd', last_name='Little', number='757-999-4562', birthday=date(1974, 7, 28))
aunty.save()

wifey = Contacts(first_name='Wifey', last_name='Rowe', number='757-876-1876', birthday=date(1998, 6, 10))
wifey.save()

pops = Contacts(first_name='Pops', last_name='Salley', number= '704-746-3031', birthday=date(1969, 3, 16))
pops.save()

josh = Contacts(first_name = 'Josh', last_name='Salley', number='336-831-0327', birthday=date(1994, 10,24))
josh.save()

print("Howdy we working")


def black_book():
    print('Welcome To your personal Black Book \n 1: Contacts \n 2: Add New Contact \n 3: Find Contact \n 4: Exit')
    pick = int(input('Enter Number: '))
    if pick == 1:
        show_contacts()
    elif pick == 2: 
        create_contact()
    elif pick == 3:
        find_contact()
    else:
        exit()

# Show all Contact
def show_contacts():
    contacts = Contacts.select()
    for contact in contacts:
        print(f'Full Name: {contact.first_name} {contact.last_name} \n Birthday: {contact.birthday} \n Number: {contact.number}')
    
    quit = input('To return press q: ')
    if quit == 'q':
        black_book()



# find_mother = Contacts.get(Contacts.first_name == 'MaDukes')
# print(find_mother.last_name)

# Create a Contact
def create_contact():
    new_first_name = input('Enter first name: ')
    new_last_name = input('Enter Last name: ')
    new_birthday = input('Enter Birthday Year,Month,Day (2020,11,24): ')
    new_number = input('Enter number: ')

    new_contact = Contacts(
        first_name = new_first_name,
        last_name = new_last_name,
        birthday = new_birthday,
        number = new_number
    )
    new_contact.save()
    black_book()

# find contact by first name 
def find_contact():
    search = input("Enter Name: ")
    search_result = Contacts.select().where(Contacts.first_name == search)
    for contact in search_result:
        print(f'Full Name: {contact.first_name} {contact.last_name} \n Birthday: {contact.birthday} \n Number: {contact.number}')
    
    black_book()
        


black_book()





      
