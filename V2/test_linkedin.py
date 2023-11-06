import pytest

from Class.LinkedIn import LinkedInMessage
from Class.enums.LinkedIn import Action

USER_NAME = "planeta_notion"

NOTION_DATABASE_ID = "190f2bf3894249158abc2eb920f41a34"
NOTION_API_KEY = "secret_zmSrhMzHk42dTAcpYegvuq7Jc6yTm0HNLBCNULHxSvZ"

@pytest.fixture(scope="module")
def linkedin_instance():
    linkedin = LinkedInMessage(database_id = NOTION_DATABASE_ID, key = NOTION_API_KEY)
    yield linkedin

@pytest.fixture(scope="module")
def linkedin_contacts():
    linkedin = LinkedInMessage(database_id = NOTION_DATABASE_ID, key = NOTION_API_KEY)
    linkedin.start()
    yield linkedin

def test_all_contacts(linkedin_contacts):
    linkedin = linkedin_contacts

    assert len(linkedin.contacts) > 800

def test_contacts(linkedin_contacts):
    linkedin = linkedin_contacts
    first, *_ = linkedin.contacts

    expected = {
        "name": "Rayedel Ortega",
        "page_profile": "https://www.linkedin.com/in/rayedelortega?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAACIMc9oBrsIPDr9vrpruLojJPF3wo6zgwjk",
    }
    assert first.get_name() == expected["name"]
    assert first.get_first_name() == "Rayedel"
    assert first.get_page_profile() == expected["page_profile"]

def test_get_buttons_in_profile_page(linkedin_contacts):
    linkedin = linkedin_contacts
    first, *rest = linkedin.contacts
    linkedin.scraper.go_to_page(first.get_page_profile())
    buttons = linkedin.scraper.get_page_profile_buttons()

    assert len(buttons) > 2


def test_buttons_in_contact_page(linkedin_contacts):
    linkedin = linkedin_contacts
    first, _, third, _, _, sixth, *rest = linkedin.contacts
    actions_first = linkedin.scraper.manage_contact_page(first.get_page_profile())
    actions_third = linkedin.scraper.manage_contact_page(third.get_page_profile())
    actions_sixth = linkedin.scraper.manage_contact_page(sixth.get_page_profile())

    assert type(Action.FOLLOW.value) == str
    assert Action.FOLLOW.value in actions_first
    assert Action.FOLLOW.value in actions_third
    assert Action.FOLLOW.value in actions_sixth

def test_right_message(linkedin_contacts):
    link = linkedin_contacts
    link.set_user(user=USER_NAME)
    first, *rest = link.contacts
    message = link.select_message(contact_name=first.get_first_name())

    expected = """¡Hola Rayedel!
Soy especialista en optimizar procesos usando Notion.
Si buscas mejorar la productividad de tu equipo, me encantaría mostrarte cómo
¿Te gustaría ver cómo podría beneficiar a tu empresa?"""

    assert message == expected