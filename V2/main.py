"""Módulo para envío de mensajes por LinkedIn"""
from Class.LinkedIn import LinkedInMessage

#COMPANY_NAME = "aceros_arequipa"

# El nombre del usuario debe ser igual al archivo .txt que tiene el mensaje
USER_NAME = "planeta_notion"

NOTION_DATABASE_ID = "190f2bf3894249158abc2eb920f41a34"
NOTION_API_KEY = "secret_zmSrhMzHk42dTAcpYegvuq7Jc6yTm0HNLBCNULHxSvZ"

if __name__ == "__main__":
    message = LinkedInMessage(database_id = NOTION_DATABASE_ID, key = NOTION_API_KEY)
    message.start()
    message.set_user(user=USER_NAME)
    message.send()
    message.end()
