"""Módulo para interactuar con navegador web"""
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
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
        self.buttons: list = []

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

    def get_elements_by_xpath(self, xpath_id: str) -> list[webelement]:
        """Función para encontrar elementos HTML por XPATH"""

        # COnsiderar usar un decorador para el try except
        # y asi poder usarlo con cualquier otra funcion
        try:
            ele = self.driver.find_elements(By.XPATH, xpath_id)
            return ele
        except Exception as err:
            print("No obtuvo web elements. Revisa el error")
            print(err)
            print("!!"*40)
            return []
        
    def get_element(self, css_selector: str ="") -> webelement:
        """Funcion que retorna el elemento web encontrado de acuerdo
        al selector"""

        try:
            ele = self.driver.find_element(By.CSS_SELECTOR, css_selector)
            return ele
        except Exception as err:
            print("No obtuvo web element usando css selector. Revisa el error")
            print(err)
            print("!!"*40)
            return None

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

    def go_to_page(self, url: str = "") -> None:
        """Funcion para ir a una determinada pagina"""

        self.driver.get(url)
    
    def get_contact_button(self) -> bool:
        """Funcion para obtener el boton de conectar"""

        self.buttons = self.get_page_profile_buttons()
        self.connect_btn = self.get_button(ButtonName.CONNECT.value, self.buttons)

        return True if self.connect_btn else False
    
    def press_connect_button(self, contact_message: str) -> None:
        """Función flujo para agregar nota y presionar botón de enío de nota a contacto"""

        self.connect_btn.click()
        self.press_add_note_button()
        self.add_note(contact_message)
        time_to_sleep(3, 6)
        self.press_send_note_button()

    def press_add_note_button(self) -> None:
        """Función que buscar y presionar botón para agregar nota al contacto"""

        selector = self.CONNECT_MODAL + self.CONNECT_MODAL_ADD_NOTE_BUTTON
        button,  = self.get_elements_by_xpath(selector)
        button.click()

    def add_note(self, message: str) -> None:
        """Función que agregar el mensaje en el campo de texto"""

        text_area,  = self.get_elements_by_xpath(self.CONNECT_MODAL_TEXT_AREA)
        text_area.send_keys(message)

    def press_send_note_button(self) -> None:
        """Función que buscar y presionar botón para enviar la nota al contacto"""

        selector = self.SEND_MESSAGE_BUTTON_CONTAINER + self.SEND_MESSAGE_BUTTON
        btn,  = self.get_elements_by_xpath(selector)
        btn.click()

    def get_follow_button(self) -> bool:
        """Funcion para obtener el boton de seguir"""

        if not self.buttons:
            self.buttons = self.get_page_profile_buttons()

        self.follow_btn = self.get_button(ButtonName.FOLLOW.value, self.buttons)

        return True if self.follow_btn else False

    def press_follow_button(self) -> None:
        """Función para presionar botón Seguir contacto"""

        try:
            self.follow_btn.click()
        except:
            self.driver.execute_script("arguments[0].click();", self.follow_btn)

    def get_more_button(self) -> bool:
        """Funcion para obtener boton MAS"""

        if not self.buttons:
            self.buttons = self.get_page_profile_buttons()
        print("self.buttons")
        print(self.buttons)
        self.more_btn = self.get_button(ButtonName.MAS.value, self.buttons)

        return True if self.more_btn else False
    
    def press_more_button(self) -> None:
        """Funcion que presiona el boton mas para desplegar mas acciones
        y poder conectar y segui"""

        self.more_btn.click()

    def more_button_flow(self, full_name: str = "", message: str = "") -> None:
        """Funcion para hacer el flujo de presionar botones de
        Seguir y/o Conectar"""

        connect_button_selector = self.connect_more_menu_selector(full_name=full_name)
        self.connect_btn = self.get_element(css_selector=connect_button_selector)
        if self.connect_btn:
            self.press_connect_button(message)
            return True

        return False

