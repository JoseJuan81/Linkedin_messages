import unittest
from helper.df import save_to_csv
from Class.LinkedIn import LinkedInMessage
from pathlib import Path


class TestLinkedIn(unittest.TestCase):

    def test_contacts(self):
        linkedin = LinkedInMessage("antamina")
        contacts = linkedin.contacts

        expected = {
            "name": "Jaime Hugo Gonzales Cordero",
            "position": "Administrador de Compras e Inventario en Compañía Minera Antamina",
            "link": "https://www.linkedin.com/in/jaime-hugo-gonzales-cordero-7884298a?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABLtsxgBHw-1c61qm_sR5KiIZddBLwjaIDk",
            "page": "56",
            "key_position": "compras"
        }
        self.assertEqual(contacts[0], expected)

    def test_select_message(self):
        linkedin = LinkedInMessage("antamina")

        msg = linkedin.select_message("compras")
        expected = "Represento a la empresa canadiense Int-elle Corporation y suministramos materiales y productos especiales contra el desgaste para el sector minero - industrial. Quisiera hacerte llegar nuestra presentación para que visualices nuestro trabajo. Saludos"
        self.assertEqual(msg, expected)

        msg = linkedin.select_message("mantenimiento")
        expected = "Represento a Int-elle Corporation de canadá quien es especialista en gestionar el desgaste para el sector minero industrial. Diseñamos y fabricamos productos y recubrimientos de alta resistencia contra el desgaste. Me gustaría que conozcas nuestros productos y clientes. Saludos"
        self.assertEqual(msg, expected)

    def test_save_contacts_to_csv_file(self):
        data = [
            {"name": "Noah", "cargo": "Gerente", "status": "contactado"},
            {"name": "José Juan", "cargo": "Ingeniero", "status": "pendiente"}
        ]
        save_to_csv("test_data", data)

        jupyter_path = Path().absolute()
        expected_dir_path = Path(
            jupyter_path, "LinkedIn_messages", "V2", "result")
        test_file = "test_data.csv"
        full_test_file = Path(expected_dir_path, test_file)

        self.assertTrue(full_test_file.exists())


if __name__ == "__main__":
    unittest.main()
