import itertools
from pathlib import Path
from helper.files import get_contacts_from_file


class Contacts:
    """Clase que busca los contactos de una compañía"""

    def __init__(self) -> None:
        self.contacts_source = None
        self.company_name = None
        self.company_dir_path = None
        self.files = None
        self.jupyter_path = Path().absolute().parents[1]

    def get_source_path(self) -> Path:
        """Función que construye la ruta para acceder al directorio de los contactos"""

        origin_path = "scraping-linkedin/V2/result"
        self.contacts_source = Path(self.jupyter_path, origin_path, self.company_name)
        return self.contacts_source

    def set_company_name(self, company_name: str) -> None:
        """Función que establece el nombre de la compañía usado para seleccionar 
        el directorio de contactos correcto"""

        self.company_name = company_name
        self.company_dir_path = self.get_source_path()

    def get_contacts_files(self) -> None:
        """Función para obtener un arreglo de archivos con los contactos"""
        
        def is_csv(file): return file.suffix == ".csv"
        def is_txt(file): return file.suffix == ".txt"

        self.files = [
            file for file in self.company_dir_path.iterdir() if is_txt(file) or is_csv(file)]

        print("="*50)
        print(f"Fueron encontrados {len(self.files)} archivos")
        print(f"en el directorio {self.company_dir_path}")
        print("="*50)

    def build_contact(self) -> list:
        """Función que recorreo los archivos, extrae la información del contacto y construye un objecto retornando una lista de objectos"""

        self.get_contacts_files()
        contacts = list(map(get_contacts_from_file, self.files))
        flatten_contacts = list(itertools.chain(*contacts))

        return flatten_contacts

    def get_contacts_from(self, company_name) -> list:
        self.set_company_name(company_name)
        return self.build_contact()
