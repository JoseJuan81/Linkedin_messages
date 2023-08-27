import unittest
from Class.Contacts import Contacts
from pathlib import Path

COMPANY_NAME = "test_company"


class TestContacts(unittest.TestCase):

    def test_contacts_path(self):
        """Probar la ruta en la que se encuentran los datos"""
        contact = Contacts()
        contact.get_source_path()

        jupyter_path = Path().absolute()
        expected_dir_path = Path(jupyter_path, "Scraping-linkedin", "data")

        self.assertEqual(expected_dir_path, contact.contacts_source)

    def test_select_company_data(self):
        contact = Contacts()
        contact.set_company_name(COMPANY_NAME)

        expected = COMPANY_NAME
        self.assertEqual(expected, contact.company_name)
        self.assertEqual(expected, contact.company_dir_path.stem)

    def test_get_contacts_files(self):
        contact = Contacts()
        contact.set_company_name(COMPANY_NAME)
        contact.get_contacts_files()
        self.assertEqual(len(contact.files), 10)

    def test_build_contact_obj(self):
        contact = Contacts()
        contact.set_company_name(COMPANY_NAME)
        contacts = contact.build_contact()

        expected = {
            "name": "Jaime Hugo Gonzales Cordero",
            "position": "Administrador de Compras e Inventario en Compañía Minera Antamina",
            "link": "https://www.linkedin.com/in/jaime-hugo-gonzales-cordero-7884298a?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABLtsxgBHw-1c61qm_sR5KiIZddBLwjaIDk",
            "page": "56",
            "key_position": "compras"
        }
        self.assertEqual(contacts[0], expected)

    def test_get_contacts_from(self):
        contact = Contacts()
        contacts = contact.get_contacts_from(COMPANY_NAME)
        first_contact = contacts[0]
        expected = {
            "name": "Jaime Hugo Gonzales Cordero",
            "position": "Administrador de Compras e Inventario en Compañía Minera Antamina",
            "link": "https://www.linkedin.com/in/jaime-hugo-gonzales-cordero-7884298a?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABLtsxgBHw-1c61qm_sR5KiIZddBLwjaIDk",
            "page": "56",
            "key_position": "compras"
        }
        self.assertEqual(first_contact, expected)

    def test_first_15_contacts(self):
        contact = Contacts()
        contacts = contact.get_contacts_from(COMPANY_NAME)
        first_15_contacts = contacts[:15]
        self.assertEqual(len(first_15_contacts), 15)

    def test_all_128_contacts(self):
        contact = Contacts()
        contacts = contact.get_contacts_from(COMPANY_NAME)
        self.assertEqual(len(contacts), 128)


if __name__ == "__main__":
    unittest.main()
