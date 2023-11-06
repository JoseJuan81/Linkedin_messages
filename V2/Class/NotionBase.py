import requests
import os

from enum import Enum

from Class.NotionContact import NotionContact

USER_EMAIL = os.getenv("USER_EMAIL")

class NotionContactStatus(Enum):
    CONECTING = "Mensaje de conexion enviado"
    FOLLOWING = "Siguiendo sin conectar"
    NOT_CONECTED = "No se puede hacer conexion"

class Notion:
    def __init__(self, database_id: str = "", key: str = "") -> None:
        self.api_key: str = key
        self.database_id: str = database_id
        self.contacts: list = []
        self.url_base = "https://api.notion.com/v1"

    def init_message(self) -> None:
        """Funcion para indicar que se ha iniciado la obtencion de datos
        desde Notion"""

        print("=="*40)
        print("inicia solicitud de contactos a Notion...")
    
    def end_message(self) -> None:
        """Funcion para indicar que se ha finalizado la obtencion de datos
        desde Notion"""

        print("Contactos conseguidos !!")
        print("=="*40)

    def update_contact(self, contact: dict = {}) -> None:
        """Funcion para atualizar contacto en notion"""
        
        url = f"{self.url_base}/pages/{contact.get_id()}"
        headers = dict([
            ("Authorization", self.api_key),
            ("Content-Type", "application/json"),
            ("Notion-Version", "2022-06-28")
        ])
        json_data = self.build_json_data(contact=contact)

        try:
            response = requests.patch(url, headers=headers, json=json_data)
            res = response.json()
            return res
        
        except Exception as err:
            print("!!"*40)
            print(f"Error al actualizar contacto: {contact.get_name()} en notion")
            print(err)
            print("!!"*40)

    def get_contacts(self) -> None:
        """Funcion para obtener los contactos desde Notion"""

        self.init_message()

        next_cursor = None
        has_more = True
        page = 1
        while has_more:
            print(f"pagina: {page}, next_cursor: {next_cursor}")
            notion_results, next_cursor, has_more = self.request_notion_data(cursor=next_cursor)
            self.contacts += self.get_notion_contacts_instance(notion_results)
            page += 1

        self.end_message()

        return self.contacts

    def get_notion_contacts_instance(self, data: list = []) -> list:
        """Function que extrae la data de los contactos de la consulta hecha a Notion"""

        return [NotionContact(page) for page in data]
    
    def request_notion_data(self, cursor: str | None = None) -> dict:
        """Funcion que ejecuta la solicitud de informacion a Notion"""

        url = f"{self.url_base}/databases/{self.database_id}/query"
        headers = dict([
            ("Authorization", self.api_key),
            ("Notion-Version", "2022-06-28"),
        ])
        data = { "filter": { "property": "Estado",  "select": { "is_empty": True } } }
        if cursor:
            data.update({ "start_cursor": cursor })
        
        try:
            response = requests.post(url, headers=headers, json=data)
            res = response.json()
            return (res["results"], res["next_cursor"], res["has_more"])
        except Exception as err:
            print("!!"*40)
            print("Error al obtener contactos desde notion")
            print(err)
            print("!!"*40)

    def build_json_data(self, contact: dict = {}) -> dict:
        """Funcion para construir el objeto que se enviara para actualizar
        al contacto"""

        schema = {
            "properties": {
                "Estado": {
                    "select": {
                        "name": contact.get_status()
                    }
                },
                "Integrante Planeta notion que contacto": {
                    "select": {
                        "name": USER_EMAIL
                    }
                }
            }
        }

        return schema