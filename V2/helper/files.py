from pathlib import Path
from helper.txt_file import txt_file_contact
from helper.csv_file import csv_file_contact

def read_file_content(file) -> str:
    """Función para leer un archivo con decodificador utf-8"""

    txt = ""
    try:
        with file.open(encoding="utf-8") as f:
            txt = f.read()

        return txt
    except Exception as e:
        print("error"*10)
        print(e)


def match_file_by_name(position: str, files: list) -> str:
    """Función para recorrer archivos y seleccionar el que haga match con el name"""

    for file in files:
        file_name = file.stem
        is_buyer = position in ["compras", "logistica", "logística"]

        if file_name == "compras" and is_buyer:
            return file

        if file_name == "mantenimiento" and not is_buyer:
            return file


def match_file_and_get_content(position: str, files: str) -> str:
    """Función que seleccionar el archivo correcto, extrae el contenido y lo retorna"""
    return read_file_content(match_file_by_name(position, files))


def get_message_dir_path(executor):
    abs_path = Path().absolute().parents[1]
    return Path(abs_path, "LinkedIn_messages", "messages", executor)

def get_contacts_from_file(file: str):
    ext = file.suffix 

    if ext == ".csv":
        return csv_file_contact(file)
    else:
        return txt_file_contact(file)
