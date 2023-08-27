"""Módulo para envío de mensajes por LinkedIn"""
from Class.LinkedIn import LinkedInMessage

COMPANY_NAME = "antamina"

if __name__ == "__main__":
    message = LinkedInMessage(COMPANY_NAME)
    message.browser_start()
    message.send()
