"""Módulo para interactuar con navegador web"""
import os

from selenium import webdriver
from helper.time import time_to_sleep
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()

URL_HOME = 'https://www.linkedin.com'

USER_EMAIL = os.getenv("USER_EMAIL")
USER_PASS = os.getenv("USER_PASS")
ACTION_CONNECT = os.getenv("ACTION_CONNECT")
ACTION_FOLLOW = os.getenv("ACTION_FOLLOW")
ACTION_PENDING = os.getenv("ACTION_PENDING")
ACTION_NOT_POSSIBLE = os.getenv("ACTION_NOT_POSSIBLE")
CONTACT_ACTION_CONNECT = os.getenv("CONTACT_ACTION_CONNECT")
CONTACT_ACTION_PENDING = os.getenv("CONTACT_ACTION_PENDING")
CONTACT_ACTION_FOLLOW = os.getenv("CONTACT_ACTION_FOLLOW")

LOGIN_INPUT_EMAIL = '//input[@id="session_key"]'
LOGIN_INPUT_PASS = '//input[@id="session_password"]'
LOGIN_BUTTON = '//button[@data-id="sign-in-form__submit-btn"]'
LINKEDIN_CONTACT_BUTTONS = '//section[@class="artdeco-card ember-view pv-top-card"]//button'
CONNECT_MODAL = '//div[@role="dialog"]'
CONNECT_MODAL_ADD_NOTE_BUTTON = '//button[@aria-label="Añadir una nota"]'
CONNECT_MODAL_TEXT_AREA = '//textarea'
SEND_MESSAGE_BUTTON_CONTAINER = '//div[@class="artdeco-modal__actionbar ember-view text-align-right"]'
SEND_MESSAGE_BUTTON = '//button[@aria-label="Enviar ahora"]'


class Selenium:
    def __init__(self) -> None:
        self.login_email_input = LOGIN_INPUT_EMAIL
        self.login_password_input = LOGIN_INPUT_PASS
        self.login_button = LOGIN_BUTTON
        self.driver = None
        self.connect_btn = None
        self.follow_btn = None

    def init(self) -> None:
        """Función para iniciar navegador web"""
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)
        return self.driver

    def get_elements_by_xpath(self, xpath_id: str) -> str:
        """Función para encontrar elementos HTML por XPATH"""
        ele = self.driver.find_elements(By.XPATH, xpath_id)
        return ele

    def login(self) -> None:
        """Función para inicar sesión en LinkedIn"""
        self.driver.get(URL_HOME)
        self.driver.implicitly_wait(6)

        input_user, *_ = self.get_elements_by_xpath(LOGIN_INPUT_EMAIL)
        input_pass, *_ = self.get_elements_by_xpath(LOGIN_INPUT_PASS)

        input_user.send_keys(USER_EMAIL)
        input_pass.send_keys(USER_PASS)

        btn, *_ = self.get_elements_by_xpath(LOGIN_BUTTON)
        btn.click()

    def get_contact_page_buttons(self) -> None:
        """Función para obtener los botones de contacto en la página de la persona"""
        time_to_sleep(3, 5)
        buttons = self.get_elements_by_xpath(LINKEDIN_CONTACT_BUTTONS)
        return buttons

    def get_button(self, key_word: str, buttons: list) -> object or False:
        """Función que consigue el botón en función de la Key_word pasada como argumento"""
        target_btn = False

        for btn in buttons:
            att_val = btn.get_attribute("aria-label")
            if att_val and key_word in att_val.lower():
                target_btn = btn

        return target_btn

    def manage_contact_page(self, url: str) -> str:
        """Función que determina qué boton tiene el contacto disponible y retorna una acción"""
        self.driver.get(url)
        buttons = self.get_contact_page_buttons()
        actions = []

        self.follow_btn = self.get_button(CONTACT_ACTION_FOLLOW, buttons)
        if self.follow_btn:
            actions.append(ACTION_FOLLOW)

        pending_btn = self.get_button(CONTACT_ACTION_PENDING, buttons)
        if pending_btn:
            actions.append(ACTION_PENDING)

        self.connect_btn = self.get_button(CONTACT_ACTION_CONNECT, buttons)
        if self.connect_btn:
            actions.append(ACTION_CONNECT)

        return actions

    def press_add_note_button(self) -> None:
        """Función que buscar y presionar botón para agregar nota al contacto"""
        button,  = self.get_elements_by_xpath(
            CONNECT_MODAL + CONNECT_MODAL_ADD_NOTE_BUTTON
        )
        button.click()

    def add_note(self, name: str, message: str) -> None:
        """Función que agregar el mensaje en el campo de texto"""
        full_message = f"Hola {name},\n{message}"
        text_area,  = self.get_elements_by_xpath(CONNECT_MODAL_TEXT_AREA)
        text_area.send_keys(full_message)

    def press_send_note_button(self) -> None:
        """Función que buscar y presionar botón para enviar la nota al contacto"""
        btn,  = self.get_elements_by_xpath(
            SEND_MESSAGE_BUTTON_CONTAINER + SEND_MESSAGE_BUTTON
        )
        btn.click()

    def press_connect_button(self, contact_name: str, contact_message: str) -> None:
        """Función flujo para agregar nota y presionar botón de enío de nota a contacto"""
        self.connect_btn.click()
        self.press_add_note_button()
        self.add_note(contact_name, contact_message)
        time_to_sleep(3, 7)
        self.press_send_note_button()

    def press_follow_button(self) -> None:
        """Función para presionar botón Seguir contacto"""
        self.follow_btn.click()
