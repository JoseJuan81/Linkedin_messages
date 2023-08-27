"""Módulo para definir Clase LinkedInMessage"""
import os
import pandas as pd

from dotenv import load_dotenv
from helper.time import time_to_sleep
from Class.Contacts import Contacts as Cts
from Class.Selenium import Selenium
from helper.files import match_file_and_get_content, get_message_dir_path
from helper.df import save_to_csv
from pathlib import Path

load_dotenv()

SALES = "compras"
MAINTENANCE = "mantenimiento"

ACTION_CONNECT = os.getenv("ACTION_CONNECT")
ACTION_FOLLOW = os.getenv("ACTION_FOLLOW")
ACTION_PENDING = os.getenv("ACTION_PENDING")
ACTION_NOT_POSSIBLE = os.getenv("ACTION_NOT_POSSIBLE")

contacts = Cts()


class LinkedInMessage:
    """Clase para gestionar contactos y enviar mensajes a cada uno por LinkedIm"""

    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.contacts = []
        self.contacts_to_save = []
        self.people_contacted = []
        self.selenium = Selenium()

        self.get_contacts()

    def get_contacts(self) -> None:
        """Administrar contactos"""

        self.contacts = contacts.get_contacts_from(self.company_name)
        print("="*50)
        print(f"Fueron encontrados: {len(self.contacts)} contactos")
        print(f"en la empresa {self.company_name}")
        print("="*50)

    def browser_start(self) -> None:
        """Iniciar el navegador e iniciar sesión en LinkedIn"""

        self.selenium.init()
        self.selenium.login()

    def select_message(self, position) -> str:
        """Seleccionar mensaje en función del cargo"""

        message_path = get_message_dir_path()
        files = [f for f in message_path.iterdir() if f.suffix == ".txt"]
        txt = match_file_and_get_content(position, files)

        return txt

    def manage_contact(self, url: str) -> str:
        """Función que gestiona acciones en la página del contacto"""
        actions = self.selenium.manage_contact_page(url)
        return actions

    def send(self) -> None:
        """Enviar mensajes a los contactos"""

        counter = 1
        for contact in self.contacts:
            name, _, contact_url, _, key_position = contact.values()
            contact["status"] = ACTION_NOT_POSSIBLE

            print("="*50)
            print(f"Contador: {counter}/{len(self.contacts)}")
            print(f"Pág. de {name}")

            actions = self.manage_contact(contact_url)

            if ACTION_PENDING in actions:
                contact["status"] = ACTION_PENDING

            if ACTION_FOLLOW in actions:
                self.selenium.press_follow_button()
                contact["status"] = ACTION_FOLLOW
                time_to_sleep(1, 5)

            if ACTION_CONNECT in actions:
                message = self.select_message(key_position)
                self.selenium.press_connect_button(name, message)
                contact["status"] = ACTION_CONNECT
                time_to_sleep(3, 8)

            print(f'Estado del contacto: {contact["status"]}')
            print("HECHO!!!")
            print("="*50)

            self.people_contacted.append(contact)
            save_to_csv(self.company_name, self.people_contacted)
            counter += 1

            time_to_sleep(5, 15)

        print("="*50)
        print(
            f"Creado archivo {self.company_name}.csv dentro del directorio '/result'")
        print(
            f"con los {len(self.contacts)} contactos clasificados por 'status'")
        print("="*50)
        print("FIN")
