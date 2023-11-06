"""Módulo para definir Clase LinkedInMessage"""
import os
import pandas as pd

from dotenv import load_dotenv
from helper.time import time_to_sleep
from Class.Contacts import Contacts as Cts
from Class.Selenium import Scraper
from Class.NotionBase import Notion
from Class.enums.LinkedIn import Action, ConectionStatus

from helper.files import read_file_content, get_message_dir_path
from helper.df import save_to_csv
from helper.time import time_to_sleep

load_dotenv()

SALES = "compras"
MAINTENANCE = "mantenimiento"

# contacts = Cts()

class LinkedInMessage:
    """Clase para gestionar contactos y enviar mensajes a cada uno por LinkedIm"""

    def __init__(self, database_id: str = "", key: str = "") -> None:
        self.executor: str = ""
        self.contacts: list = []
        self.notion: Notion = Notion(database_id=database_id, key=key)
        self.scraper: Scraper = Scraper()

    def start(self) -> None:
        """Funcion para iniciar proceso de scraping"""

        self.browser_start()
        self.get_contacts()

    def set_user(self, user: str = "") -> None:
        """Funcion para establecer el usuario que esta ejecutando el scrping"""

        self.executor = user

    def browser_start(self) -> None:
        """Iniciar el navegador e iniciar sesión en LinkedIn"""

        self.scraper.init()
        self.scraper.login()
        time_to_sleep(1, 3)

    def get_contacts(self) -> None:
        """Funcion para obtener contactos de Notion"""

        self.contacts = self.notion.get_contacts()

    def send(self) -> None:
        """Enviar mensajes a los contactos"""

        counter = 1
        for contact in self.contacts:

            contact.set_status(ConectionStatus.IMPOSSIBLE.value)

            print(".."*50)
            print(f"Contador: {counter}/{len(self.contacts)}")
            print(f"Pág. de {contact.get_name()}")

            actions = self.scraper.manage_contact_page(contact.get_page_profile())
            self.manage_actions(actions=actions, contact=contact)

            saved = self.notion.update_contact(contact=contact)

            print(f'Estado del contacto: {contact.get_status()}')
            print("Guardado en Notion")
            print(saved)
            print("HECHO!!!")
            print("✔︎"*50)

            #self.people_contacted.append(contact)
            #save_to_csv(self.company_name, self.people_contacted)
            counter += 1

            time_to_sleep(2, 7) if counter % 5 == 0 else time_to_sleep(1, 3)

    def select_message(self, contact_name: str = "") -> str:
        """Seleccionar mensaje en función del cargo"""

        message_dir_path = get_message_dir_path(self.executor)

        if message_dir_path:
            file, *_ = [f for f in message_dir_path.iterdir() if f.suffix == ".txt"]
            content_file = read_file_content(file)
            txt = content_file.format(name = contact_name)
        else:
            print("!!"*50)
            print("No existe carpeta para empresa ejecutora especificada o no se ha especificado.")
            print("Revisa la carpeta 'messages' para determinar mensaje de la empresa ejecutora")
            print("!!"*50)

        return txt

    def manage_actions(self, actions: list = [], contact: dict = {}) -> None:
        """Funcion que ejecuta acciones en funcion del valor de 'actions'"""

        if Action.PENDING.value in actions:
            contact.set_status(ConectionStatus.PENDING.value)

        if Action.FOLLOW.value in actions:
            contact.set_status(ConectionStatus.FOLLOW.value)
            time_to_sleep(1, 3)
            self.scraper.press_follow_button()

        if Action.CONNECT.value in actions:
            contact.set_status(ConectionStatus.CONNECT.value)
            time_to_sleep(1, 4)
            message = self.select_message(contact_name=contact.get_first_name())
            self.scraper.press_connect_button(message)

        if Action.MAS.value in actions:
            contact.set_status(ConectionStatus.CONNECT.value)
            time_to_sleep(1, 4)
            message = self.select_message(contact_name=contact.get_first_name())
            self.scraper.press_more_button(message)


    def end(self) -> None:
        """Funcion para indicar a usuario que termino el proceso de scraping"""

        print("="*50)
        print("FIN")
        print("="*50)