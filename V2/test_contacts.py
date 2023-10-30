
from Class.Contacts import Contacts
from pathlib import Path

COMPANY_NAME = "test_company_2.csv"


def test_contacts_path():
    """Probar la ruta en la que se encuentran los datos"""
    contact = Contacts()
    contact.set_company_name(COMPANY_NAME)
    # se ejecuta get_source_path() automaticamente

    jupyter_path = Path().absolute().parents[1]
    expected_dir_path = Path(jupyter_path, "scraping-linkedin", "V2", "result", COMPANY_NAME)

    assert expected_dir_path == contact.contacts_source


def test_select_company_data():
    contact = Contacts()
    contact.set_company_name(COMPANY_NAME)
    # se ejecuta get_source_path() automaticamente

    expected = COMPANY_NAME
    assert expected == f"{contact.company_name}.csv"
    assert expected == contact.company_dir_path.stem


def test_get_contacts_files():
    """Busca en la carpeta result de scrapping-linkedin y cuenta la cantidad de archivos que existen"""

    contact = Contacts()
    contact.set_company_name(COMPANY_NAME)
    # se ejecuta get_source_path() automaticamente
    contact.get_contacts_files()
    assert len(contact.files) == 1 


def test_build_contact_obj():
    contact = Contacts()
    contact.set_company_name(COMPANY_NAME)
    contact.get_source_path()
    contacts = contact.build_contact()

    expected = {
        "name": "Rafael Estrada",
        "job_position": "IT manager at Antamina",
        "image": "NT",
        "page_profile": "https://www.linkedin.com/in/rafael-estrada-a6a6226?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAEo3XIB0ScJAZUi81HQSwr7Of0PJmV4wTw",
        "action": "Enviar mensaje",
        "country": "Perú",
        "company_name": "Antamina",
        "company_page": 96,
        # "key_position": "compras"
    }
    assert contacts[0] == expected


def test_get_contacts_from():
    contact = Contacts()
    contacts = contact.get_contacts_from(COMPANY_NAME)
    first_contact = contacts[0]
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
    assert first_contact == expected


def test_first_3_contacts():
    contact = Contacts()
    contacts = contact.get_contacts_from(COMPANY_NAME)
    first_3_contacts = contacts[:3]
    assert len(first_3_contacts) == 3

