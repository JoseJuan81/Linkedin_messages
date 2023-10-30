from helper.df import save_to_csv
from Class.LinkedIn import LinkedInMessage
from pathlib import Path

COMPANY_NAME = "antamina"
EXECUTOR = "int-elle"

def test_contacts():
    linkedin = LinkedInMessage(COMPANY_NAME, EXECUTOR)
    contacts = linkedin.contacts

    expected = {
        "name": "Rafael Estrada",
        "job_position": "IT manager at Antamina",
        "image": "NT",
        "page_profile": "https://www.linkedin.com/in/rafael-estrada-a6a6226?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAEo3XIB0ScJAZUi81HQSwr7Of0PJmV4wTw",
        "action": "Enviar mensaje",
        "country": "Perú",
        "company_name": "Antamina",
        "company_page": 96,
    }
    assert contacts[0] == expected

def test_select_message():
    linkedin = LinkedInMessage(COMPANY_NAME, EXECUTOR)

    msg = linkedin.select_message("andres")
    expected = "Hola andres!, Represento a Int-elle Corporation de canadá y somos especialistas en desgaste para el sector minero industrial. Diseñamos y fabricamos productos, piezas y recubrimientos de alta resistencia contra el desgaste. Me gustaría conozcas nuestros productos, conectamos?. Saludos.\n"
    assert msg == expected


def test_save_contacts_to_csv_file():
    data = [
        {"name": "Noah", "cargo": "Gerente", "status": "contactado"},
        {"name": "José Juan", "cargo": "Ingeniero", "status": "pendiente"}
    ]
    new_file_name = "test_data_2"
    save_to_csv(new_file_name, data)

    v2_path = Path().absolute()
    expected_dir_path = Path(v2_path, "result", f"{new_file_name}.csv")

    assert expected_dir_path.exists()
