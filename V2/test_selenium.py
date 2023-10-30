
import os
from Class.Selenium import Selenium
from dotenv import load_dotenv

load_dotenv()

ACTION_CONNECT = os.getenv("ACTION_CONNECT")
ACTION_FOLLOW = os.getenv("ACTION_FOLLOW")
ACTION_PENDING = os.getenv("ACTION_PENDING")
ACTION_NOT_POSSIBLE = os.getenv("ACTION_NOT_POSSIBLE")

URL_HOME = 'https://www.linkedin.com'
LOGIN_INPUT_EMAIL = '//input[@id="session_key"]'
LOGIN_INPUT_PASS = '//input[@id="session_password"]'
LOGIN_BUTTON = '//button[@data-id="sign-in-form__submit-btn"]'

LINKEDIN_CONTACT_PENDING = "https://www.linkedin.com/in/kelly-rosa-laura-guevara-02516425/"
LINKEDIN_CONTACT_CONECT = "https://www.linkedin.com/in/david-rojas-bautista-586317aa/"
LINKEDIN_CONTACT_FOLLOW = "https://www.linkedin.com/in/hyder-mamani-83769617/"
LINKEDIN_CONTACT_NOT_POSSIBLE = "https://www.linkedin.com/in/juanreymundo%C3%B1ahui/"


def test_linkedin_login_form_input_email():
    sel = Selenium()
    sel.init()
    sel.driver.get(URL_HOME)
    input_el, *_ = sel.get_element_by_xpath(LOGIN_INPUT_EMAIL)
    expected = "session_key"

    assert isinstance(LOGIN_INPUT_EMAIL, str)
    assert input_el.get_attribute("id") == expected
    sel.quit()


def test_linkedin_login_form_input_pass():
    sel = Selenium()
    sel.init()
    sel.driver.get(URL_HOME)
    input_el, *_ = sel.get_element_by_xpath(LOGIN_INPUT_PASS)
    expected = "session_password"

    assert isinstance(LOGIN_INPUT_EMAIL, str)
    assert input_el.get_attribute("id") == expected
    sel.quit()


def test_linkedin_login_form_btn():
    sel = Selenium()
    sel.init()
    sel.driver.get(URL_HOME)
    input_el, *_ = sel.get_element_by_xpath(LOGIN_BUTTON)
    expected = "sign-in-form__submit-btn"

    assert isinstance(LOGIN_INPUT_EMAIL, str)
    assert input_el.get_attribute("data-id") == expected
    sel.quit()


def test_manage_contact_page():
    sel = Selenium()
    sel.init()
    sel.login()

    print("detectar boton para Conectar")
    actions = sel.manage_contact_page(LINKEDIN_CONTACT_CONECT)
    assert ACTION_CONNECT in actions, "ERROR en: Boton para conectar"
    print("Conectar: OK")

    print("detectar boton para Pendiente")
    actions = sel.manage_contact_page(LINKEDIN_CONTACT_PENDING)
    assert ACTION_PENDING in actions, "ERROR en: Bot�n Pendiente"
    print("Pendiente: OK")

    print("detectar boton para Seguir")
    actions = sel.manage_contact_page(LINKEDIN_CONTACT_FOLLOW)
    assert ACTION_FOLLOW in actions, "ERROR: No se encuentra bot�n Seguir"
    print("Seguir: OK")

    print("detectar boton para Sin Boton")
    actions = sel.manage_contact_page(LINKEDIN_CONTACT_NOT_POSSIBLE)
    assert actions == [], "ERROR en: Sin Boton"
    print("Sin Boton: OK")
    sel.quit()
