class NotionContact:
    def __init__(self, contact: dict = {}) -> None:
        self.contact: dict = contact
        self.properties: dict = contact["properties"]

    def get_id(self) -> str:
        """Funcion que retorna el id Notion del contacto"""

        return self.contact["id"]
    
    def get_properties(self) -> dict:
        """Funcion que retorna el arreglo propiedades Notion del contacto"""

        return self.properties
    
    def page_profile(self) -> str:
        """Funcion que retorna la pagina de perfil de usuario de LinkedIn"""

        return self.contact["page_profile"]["url"]

    def get_url(self) -> dict:
        """Funcion que retorna la url Notion del contacto"""

        return self.contact["url"]
    
    def get_name(self) -> str:
        """Funcion para obtener el nombre del contacto"""

        return self.properties["name"]["title"][0]["plain_text"]
    
    def get_first_name(self) -> str:
        """Funcion para obtener el nombre del contacto"""

        name = self.get_name()
        return name.split(" ")[0]
    
    def get_page_profile(self) -> str:
        """Funcion para obtener el nombre del contacto"""

        return self.properties["page_profile"]["url"]
    
    def set_status(self, status: str = "") -> None:
        """Funcion para establecer el status del contacto
        de acuerdo con la accion ejecutada en su pagina de perfil"""

        self.contact.update({ "status": status })
    
    def get_status(self) -> None:
        """Funcion para obtener el status del contacto"""

        return self.contact["status"]
        