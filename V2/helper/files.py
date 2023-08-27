from pathlib import Path


def read_file_content(file) -> str:
    """Función para leer un archivo con decodificador utf-8"""
    txt = ""
    with file.open(encoding="utf-8") as f:
        txt = f.read()

    return txt


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


def get_message_dir_path():
    abs_path = Path().absolute()
    return Path(abs_path, "LinkedIn_messages", "messages")
