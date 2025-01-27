# -*- coding: utf8 -*-
import csv

WELCOME = """
        ---------------------------------------------------
        |   B I E N V E N I D O   A   L A   A G E N D A   |
        ---------------------------------------------------
"""

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:

    def __init__(self):
        self.contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        self.save()
        #print('name: {}, phone: {}, email: {}'.format(name, phone, email))

    def delete(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                del self.contacts[i]
                self.save()
                break

    def search(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.print_contact(contact)
                break
        else:
            self.not_found()

    def save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))

            for contact in self.contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

    def show_all(self):
        print('#########################################################')
        print('         L I S T A   D E   C O N T A C T O S')
        print('#########################################################')
        for contact in self.contacts:
            self.print_contact(contact)
        print('#########################################################')

    def print_contact(self, contact):
        print('---*---*---*---*---*---*---*---')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('---*---*---*---*---*---*---*---')

    def not_found(self):
        print('#########################################################')
        print('El usuario no ha sido encontrado!!')
        print('#########################################################')

def run():

    contact_book = ContactBook()
    print(WELCOME)

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            contact_book.add(row[0], row[1], row[2])

    while True:
        command = str(input('''
        ¿Qué deseas hacer?

        [a]ñadir contacto
        [ac]tualizar contacto
        [b]uscar contacto
        [e]liminar contacto
        [l]istar contactos
        [s]alir

        Opcion: '''))

        if command == 'a':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el telefono del contacto: '))
            email = str(input('Escribe el email del contacto: '))
            contact_book.add(name, phone, email)
        elif command == 'ac':
            print('actualizar contacto')
        elif command == 'b':
            name = str(input('Escribe el nombre del contacto: '))
            contact_book.search(name)
        elif command == 'e':
            name = str(input('Escribe el nombre del contacto: '))
            contact_book.delete(name)
        elif command == 'l':
            contact_book.show_all()
            #print('listar contactos')
        elif command == 's':
            break
        else:
            print('Comando no encontrado')


if __name__ == '__main__':
    run()