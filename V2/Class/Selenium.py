"""Módulo para interactuar con navegador web"""
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

from Class.HtmlSelector import HtmlSelector
from Class.enums.LinkedIn import PageProfileButtons as ButtonName, Action

from helper.time import time_to_sleep

load_dotenv()

URL_HOME = 'https://www.linkedin.com'

USER_EMAIL = os.getenv("USER_EMAIL")
USER_PASS = os.getenv("USER_PASS")

class Scraper(HtmlSelector):
    def __init__(self) -> None:
        self.driver = None
        self.connect_btn = None
        self.follow_btn = None
        self.more_btn = None

    def init(self) -> None:
        """Función para iniciar navegador web"""

        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1400, 780)
        self.driver.implicitly_wait(10)
        return self.driver

    def login(self) -> None:
        """Función para inicar sesión en LinkedIn"""

        self.go_to_page(url=URL_HOME)
        self.driver.implicitly_wait(6)

        input_user, *_ = self.get_elements_by_xpath(self.LOGIN_INPUT_EMAIL)
        input_pass, *_ = self.get_elements_by_xpath(self.LOGIN_INPUT_PASS)

        input_user.send_keys(USER_EMAIL)
        input_pass.send_keys(USER_PASS)

        btn, *_ = self.get_elements_by_xpath(self.LOGIN_BUTTON)
        btn.click()
        input("Agrega el codigo de verificacion si es necesario y presiona enter\n")

    def get_elements_by_xpath(self, xpath_id: str) -> str:
        """Función para encontrar elementos HTML por XPATH"""

        ele = self.driver.find_elements(By.XPATH, xpath_id)
        return ele

    def get_page_profile_buttons(self) -> None:
        """Función para obtener los botones de contacto en la página de la persona"""

        #time_to_sleep(3, 5)
        buttons = self.get_elements_by_xpath(self.LINKEDIN_CONTACT_BUTTONS)
        return buttons

    def get_button(self, btn_name: str, buttons: list) -> object or False:
        """Función que consigue el botón en función de la btn_name pasada como argumento"""

        target_btn = False

        for btn in buttons:
            att_val = btn.get_attribute("aria-label")
            if att_val and btn_name.lower() in att_val.lower():
                target_btn = btn

        return target_btn

    def manage_contact_page(self, url: str) -> str:
        """Función que determina qué botones tiene el contacto disponible
        y retorna sus nombres como acciones"""

        self.go_to_page(url=url)
        time_to_sleep(1, 4)

        buttons = self.get_page_profile_buttons()
        actions = []

        # para que no haya error cuando la page_profile es una estado
        time_to_sleep(1, 2)
        self.follow_btn = self.get_button(ButtonName.FOLLOW.value, buttons)
        if self.follow_btn:
            actions.append(Action.FOLLOW.value)

        pending_btn = self.get_button(ButtonName.PENDING.value, buttons)
        if pending_btn:
            actions.append(Action.PENDING.value)

        self.connect_btn = self.get_button(ButtonName.CONNECT.value, buttons)
        if self.connect_btn:
            actions.append(Action.CONNECT.value)

        self.more_btn = self.get_button(ButtonName.MAS.value, buttons)
        if self.more_btn:
            actions.append(Action.MAS.value)

        return actions

    def go_to_page(self, url: str = "") -> None:
        """Funcion para ir a una determinada pagina"""

        self.driver.get(url)

    def press_add_note_button(self) -> None:
        """Función que buscar y presionar botón para agregar nota al contacto"""

        button,  = self.get_elements_by_xpath(
            self.CONNECT_MODAL + self.CONNECT_MODAL_ADD_NOTE_BUTTON
        )
        button.click()

    def add_note(self, message: str) -> None:
        """Función que agregar el mensaje en el campo de texto"""

        text_area,  = self.get_elements_by_xpath(self.CONNECT_MODAL_TEXT_AREA)
        text_area.send_keys(message)

    def press_send_note_button(self) -> None:
        """Función que buscar y presionar botón para enviar la nota al contacto"""

        btn,  = self.get_elements_by_xpath(
            self.SEND_MESSAGE_BUTTON_CONTAINER + self.SEND_MESSAGE_BUTTON
        )
        btn.click()

    def press_connect_button(self, contact_message: str) -> None:
        """Función flujo para agregar nota y presionar botón de enío de nota a contacto"""

        self.connect_btn.click()
        self.press_add_note_button()
        self.add_note(contact_message)
        time_to_sleep(3, 7)
        self.press_send_note_button()

    def press_follow_button(self) -> None:
        """Función para presionar botón Seguir contacto"""

        try:
            self.follow_btn.click()
        except:
            self.driver.execute_script("arguments[0].click();", self.follow_btn)

    def press_more_button(self, contact_message: str) -> None:
        """Funcion que presiona el boton mas para desplegar mas acciones
        y poder conectar y segui"""

        self.more_btn.click()
        # se despliega el menu y debo presionar Seguir y Conectar