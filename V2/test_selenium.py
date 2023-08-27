import unittest
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


class TestSelenium(unittest.TestCase):

    def setUp(self):
        self.sel = Selenium()
        self.sel.init()

    def test_linkedin_login_form_input_email(self):
        self.sel.driver.get(URL_HOME)
        input_el, *_ = self.sel.get_element_by_xpath(LOGIN_INPUT_EMAIL)
        expected = "session_key"

        self.assertEqual(type(LOGIN_INPUT_EMAIL), str)
        self.assertEqual(input_el.get_attribute("id"), expected)

    def test_linkedin_login_form_input_pass(self):
        self.sel.driver.get(URL_HOME)
        input_el, *_ = self.sel.get_element_by_xpath(LOGIN_INPUT_PASS)
        expected = "session_password"

        self.assertEqual(type(LOGIN_INPUT_EMAIL), str)
        self.assertEqual(input_el.get_attribute("id"), expected)

    def test_linkedin_login_form_btn(self):
        self.sel.driver.get(URL_HOME)
        input_el, *_ = self.sel.get_element_by_xpath(LOGIN_BUTTON)
        expected = "sign-in-form__submit-btn"

        self.assertEqual(type(LOGIN_INPUT_EMAIL), str)
        self.assertEqual(input_el.get_attribute("data-id"), expected)

    def test_manage_contact_page(self):
        self.sel.login()

        print("detectar botón para Conectar")
        actions = self.sel.manage_contact_page(LINKEDIN_CONTACT_CONECT)
        self.assertIn(ACTION_CONNECT, actions,
                      "ERROR en: Botón para conectar")
        print("Conectar: OK")

        print("detectar botón para Pendiente")
        actions = self.sel.manage_contact_page(LINKEDIN_CONTACT_PENDING)
        self.assertIn(ACTION_PENDING, actions, "ERROR en: Botón Pendiente")
        print("Pendiente: OK")

        print("detectar botón para Seguir")
        actions = self.sel.manage_contact_page(LINKEDIN_CONTACT_FOLLOW)
        self.assertIn(ACTION_FOLLOW, actions,
                      "ERROR: No se encuentra botón Seguir")
        print("Seguir: OK")

        print("detectar botón para Sin Botón")
        actions = self.sel.manage_contact_page(
            LINKEDIN_CONTACT_NOT_POSSIBLE)
        self.assertEqual([], actions,
                         "ERROR en: Sin Botón")
        print("Sin Botón: OK")


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        exit=False,
        argv=[__file__, "-k", "test_manage_contact_page"]
    )
