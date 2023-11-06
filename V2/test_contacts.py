import pytest
import os

from Class.NotionBase import Notion
from Class.enums.LinkedIn import Action

NOTION_DATABASE_ID = "190f2bf3894249158abc2eb920f41a34"
NOTION_API_KEY = "secret_zmSrhMzHk42dTAcpYegvuq7Jc6yTm0HNLBCNULHxSvZ"

@pytest.fixture(scope='module')
def notion_instance():
    notion = Notion(database_id=NOTION_DATABASE_ID, key=NOTION_API_KEY)
    yield notion

def test_validating_request_notion_data(notion_instance):
    notion = notion_instance
    data = notion.request_notion_data()

    assert data["object"] == "list"
    assert type(data["results"]) == list
    assert type(data["next_cursor"]) == str
    assert type(data["has_more"]) == bool
    assert data["type"] == "page_or_database"
    assert data["page_or_database"] == {}


def test_validating_notion_contacts_instance(notion_instance):
    notion = notion_instance
    notion_data = notion.request_notion_data()
    contacts = notion.get_notion_contacts_instance(notion_data)
    first, *_ = contacts

    assert type(first.get_id()) == str
    assert type(first.get_properties()) == dict
    assert type(first.get_url()) == str
    assert type(first.get_name()) == str
    assert type(first.get_page_profile()) == str

def test_build_json_data(notion_instance):
    notion = notion_instance
    notion_data = notion.request_notion_data()
    contacts = notion.get_notion_contacts_instance(notion_data)
    first, *_ = contacts
    first.set_status(status=Action.FOLLOW)

    json_data = notion.build_json_data(first)
    result = json_data["properties"]["Estado"]["select"]["name"]

    assert Action.FOLLOW == result
